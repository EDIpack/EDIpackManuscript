program ed_holstein
  USE EDIPACK2
  USE SCIFOR
  USE DMFT_TOOLS
  USE MPI
  USE SF_MPI
  implicit none
  integer                                     :: i,iloop,Le,Nso,Nsom,Mnambu
  logical                                     :: converged, phsym
  !Bath:
  integer                                     :: Nb,print_mode
  real(8),allocatable                         :: Bath(:),Bath_(:)
  !The local hybridization function:
  complex(8),allocatable                      :: Weiss(:,:,:,:,:,:),Weiss_(:,:,:,:,:,:)
  complex(8),allocatable                      :: Smats(:,:,:,:,:,:),Sreal(:,:,:,:,:,:)
  complex(8),allocatable                      :: Gmats(:,:,:,:,:,:),Greal(:,:,:,:,:,:)
  complex(8),allocatable                      :: Gtest(:,:)
  !hamiltonian input:
  complex(8),allocatable                      :: Hloc(:,:,:,:)
  real(8),dimension(2)                        :: Wband,de
  real(8),dimension(:,:),allocatable          :: Dbands
  real(8),dimension(:,:,:),allocatable        :: Ebands ![Nso][Le]
  real(8),dimension(:,:),allocatable          :: H0     ![Nso]
  !variables for the model:
  real(8)                                     :: ts, wmixing
  character(len=16)                           :: finput
  logical                                     :: mixG0,scflag
  !
  !MPI Vars:
  integer                                     :: irank,comm,rank,size2,ierr
  logical                                     :: master

  call init_MPI()
  comm = MPI_COMM_WORLD
  call StartMsg_MPI(comm)
  rank = get_Rank_MPI(comm)
  size2 = get_Size_MPI(comm)
  master = get_Master_MPI(comm)
  

  !Parse additional variables && read Input
  call parse_cmd_variable(finput,"FINPUT",default="inputED.in")
  call parse_input_variable(Le,"LE",finput,default=500)
  call parse_input_variable(wmixing,"WMIXING",finput,default=1.d0)
  call parse_input_variable(mixG0,"mixG0",finput,default=.false.)
  call parse_input_variable(ts,"TS",finput,default=0.25d0,comment="In bethe lattice ts=0.5d*D where D is the half bandwidth")
  call parse_input_variable(PHSYM,"PHSYM",finput,default=.false.)
  
  !
  !
  call ed_read_input(trim(finput))
  !
  !Add DMFT CTRL Variables:
  call add_ctrl_var(Norb,"norb")
  call add_ctrl_var(Nspin,"nspin")
  call add_ctrl_var(beta,"beta")
  call add_ctrl_var(xmu,"xmu")
  call add_ctrl_var(wini,'wini')
  call add_ctrl_var(wfin,'wfin')
  call add_ctrl_var(eps,"eps")

  if(bath_type/="normal")stop "Wrong setup from input file: non normal bath"
  if(Norb/=1)stop "Wrong setup from input file: Norb!=1"
  scflag=.false.;Mnambu=1;
  if(ed_mode=="superc")then
     scflag=.true.; Mnambu=2
  else if(ed_mode=="normal")then
     scflag=.false.; Mnambu=1
  else
     stop "Wrong setup from input file: ed_mode"
  end if

  Nso=Nspin*Norb
  Nsom=Nso*Mnambu
  
  !Allocate Weiss Field:
  allocate(Weiss(2,Nspin,Nspin,Norb,Norb,Lmats)); Weiss=0.d0
  allocate(Weiss_(2,Nspin,Nspin,Norb,Norb,Lmats)); Weiss_=0.d0
  allocate(Smats(2,Nspin,Nspin,Norb,Norb,Lmats)); Smats=0.d0
  allocate(Gmats(2,Nspin,Nspin,Norb,Norb,Lmats)); Gmats=0.d0
  allocate(Sreal(2,Nspin,Nspin,Norb,Norb,Lreal)); Sreal=0.d0
  allocate(Greal(2,Nspin,Nspin,Norb,Norb,Lreal)); Greal=0.d0
   
  !Build Hamiltonian structure:
  Wband(1) = 2.d0*ts !Half-bendwidth
  !
  allocate(Ebands(Mnambu,Nso,Le))
  allocate(Dbands(Nso,Le))
  !
  Ebands(1,1,:) = linspace(-Wband(1),Wband(1), Le,mesh=de(1))
  Ebands(2,1,:) = -linspace(-Wband(1),Wband(1), Le,mesh=de(1))
  !
  !Writing bethe Density of states
  do i=1,Le
     Dbands(1,i) = dens_bethe(Ebands(1,1,i),D=Wband(1))*de(1)
  end do
  !
  allocate(Hloc(Nspin,Nspin,Norb,Norb))
  allocate(H0(2,Nso))
  Hloc = zero
  H0   = zero
  !
  print_mode=3
  Nb=ed_get_bath_dimension()
  allocate(Bath(Nb))
  allocate(Bath_(Nb))
  call ed_init_solver(bath)
  allocate(Gtest(2,Lmats))
  
  !set Hloc (recently changed)
  call ed_set_Hloc(hloc)

  !DMFT loop
  iloop=0;converged=.false.
  do while(.not.converged.AND.iloop<nloop)
     iloop=iloop+1

     call start_loop(iloop,nloop,"DMFT-loop")

     !> Solve the impurity problem, retrieve matsubara self-energy
     call ed_solve(bath)
     
     !> Retrieve impurity self-energies (normal, anomalous)
     call ed_get_sigma(Smats(1,:,:,:,:,:),axis='m',type='n')
     if(scflag) call ed_get_sigma(Smats(2,:,:,:,:,:),axis='m',type='a')

     !> Get Weiss to be fitted
     if(scflag)then
        call dmft_get_gloc(Ebands,Dbands,H0,Gmats,Smats,axis="mats")
        call dmft_weiss(Gmats(1,:,:,:,:,:),Gmats(2,:,:,:,:,:), &
             Smats(1,:,:,:,:,:),Smats(2,:,:,:,:,:), &
             Weiss(1,:,:,:,:,:),Weiss(2,:,:,:,:,:) )
     else
        call dmft_get_gloc(Ebands(1,:,:),Dbands,H0(1,:),Gmats(1,:,:,:,:,:),Smats(1,:,:,:,:,:),axis="mats")
        call dmft_weiss(Gmats(1,:,:,:,:,:), &
             Smats(1,:,:,:,:,:), &
             Weiss(1,:,:,:,:,:) )
     end if

     !> Write the local Green's function:
     call dmft_write_gf(Gmats(1,:,:,:,:,:),"Gloc",axis="mats",iprint=print_mode)
     if(scflag)call dmft_write_gf(Gmats(2,:,:,:,:,:),"A_Gloc",axis="mats",iprint=print_mode)
     !> Write the Weiss field:
     call dmft_write_gf(Weiss(1,:,:,:,:,:),"Weiss",axis="mats",iprint=print_mode)
     if(scflag)call dmft_write_gf(Weiss(2,:,:,:,:,:),"A_Weiss",axis="mats",iprint=print_mode)

     if(mixG0)then
        if(iloop>1)Weiss = wmixing*Weiss + (1.d0-wmixing)*Weiss_
        Weiss_=Weiss
     endif

     !error stop
     !Fit the new bath, starting from the old bath + the supplied Weiss
     select case(ed_mode)
     case default
        stop "ed_mode!=Normal/Superc"
     case("normal")
        call ed_chi2_fitgf(Weiss(1,:,:,:,:,:),bath)
     case("superc")
        call ed_chi2_fitgf(Weiss(1,:,:,:,:,:),Weiss(2,:,:,:,:,:),bath)
     end select
     !
     print*," Here check bath:"
     print*,"bath",bath
     if(phsym) call enforce_phsym(bath)
     !
     if(.not.mixG0)then
        if(iloop>1)Bath = wmixing*Bath + (1.d0-wmixing)*Bath_
        Bath_=Bath
     endif
     !
     !Now it is pretty general
     !Same spirit of ed_fit_replica
     Gtest(:,:) = Weiss(:,1,1,1,1,:)
     !
     select case(ed_mode)
     case default
        stop "WRONG ed_mode IN check_convg"
     case("normal")
        converged = check_convergence_global(Gtest(1,:),dmft_error,nsuccess,nloop)
     case("superc")
        converged = check_convergence(Gtest(:,:),dmft_error,nsuccess,nloop)
     end select
     !
     call end_loop
  enddo

  !Compute local GFs
  call ed_get_sigma(Sreal(1,:,:,:,:,:),axis="r",type="n")
  if(scflag) call ed_get_sigma(Sreal(2,:,:,:,:,:),axis="r",type="a")
  call dmft_write_gf(Sreal(1,:,:,:,:,:),"Sreal",axis="real",iprint=print_mode)
  if(scflag) call dmft_write_gf(Sreal(2,:,:,:,:,:),"A_Sreal",axis="real",iprint=print_mode)

  call dmft_get_gloc(Ebands,Dbands,H0,Greal,Sreal,axis="real")
  call dmft_write_gf(Greal(1,:,:,:,:,:),"Gloc",axis="real",iprint=print_mode)
  if(scflag) call dmft_write_gf(Greal(2,:,:,:,:,:),"A_Gloc",axis="real",iprint=print_mode)

  !Compute Kinetic Energy
  call dmft_kinetic_energy(Ebands(1,:,:),Dbands,H0(1,:),Smats(1,:,:,:,:,:),Smats(2,:,:,:,:,:))

  call finalize_MPI()



contains


  subroutine enforce_phsym(bath)
    real(8), dimension(:)                  :: bath
    integer                                :: i1,i2,ib1,ib2,j
    real(8)                                :: mean
    select case(trim(ed_mode))
    case default
       stop "WRONG ed_mode in enforce_phsym"
    case("normal")
       do i1=1,(Nbath+1)/2
          !Ek
          mean = 0.5*( bath(i1) - bath(Nbath+1-i1) )
          bath(i1) = mean
          bath(Nbath+1-i1) = -mean
          !Vk
          mean = 0.5*( bath(i1+Nbath) + bath(Nbath+1-i1+Nbath) )
          bath(i1+Nbath) = mean
          bath(Nbath+1-i1+Nbath) = mean
       end do
    case("superc")
       do i1=1,(Nbath+1)/2
          !Ek
          mean = 0.5*( bath(i1) - bath(Nbath+1-i1) )
          bath(i1) = mean
          bath(Nbath+1-i1) = -mean
          !Dk
          mean = 0.5*( bath(i1+Nbath) + bath(Nbath+1-i1+Nbath) )
          bath(i1+Nbath) = mean
          bath(Nbath+1-i1+Nbath) = mean
          !Vk
          mean = 0.5*( bath(i1+2*Nbath) + bath(Nbath+1-i1 +2*Nbath) )
          bath(i1 +2*Nbath) = mean
          bath(Nbath+1-i1 +2*Nbath) = mean
       end do
    end select
  end subroutine enforce_phsym

  
end program ed_holstein



