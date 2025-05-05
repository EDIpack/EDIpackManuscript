HERE   = `pwd`
EXE=ed_ahm_square
FC=mpif90
PLAT=gnu
DIREXE   = $(HERE)


define colorecho	
	@tput setaf 6
	@tput bold
	@echo $1
	@tput sgr0
endef


OBJS     = 
OBJS_DEB =





#NO NEED TO CHANGE DOWN HERE, only expert mode.
#########################################################################
GLOB_INC:=$(shell pkg-config --cflags edipack2 dmft_tools scifor)
GLOB_LIB:=$(shell pkg-config --libs edipack2  dmft_tools scifor)

ifeq ($(PLAT),intel)
FFLAG=-O2 -ftz
OFLAG=-O3 -ftz
DFLAG=-p -O0 -g -fpe0 -warn -warn errors -debug extended -traceback -check all,noarg_temp_created
FPPSERIAL =-fpp -D_
FPPMPI =-fpp -D_MPI
endif
ifeq ($(PLAT),gnu)
FFLAG = -O2 -ffree-line-length-none -fopenmp
DFLAG = -O2 -p -g -fimplicit-none -Wsurprising  -Waliasing -fwhole-file -fcheck=all -pedantic -fbacktrace -ffree-line-length-none -Wunused
OFLAG = -O3 -ffast-math -march=native -funroll-loops -ffree-line-length-none
FPPSERIAL =-cpp -D_
FPPMPI =-cpp -D_MPI	
endif


##$ Extends the implicit support of the Makefile to .f90 files
.SUFFIXES: .f90



all: FLAG:=${FFLAG} ${FPPMPI}
all: ${OBJS}
	@echo ""
	$(call colorecho,"compiling $(EXE).f90 ")
	@echo ""
	$(FC) $(FLAG) $(EXE).f90 -o $(DIREXE)/$(EXE) ${GLOB_INC} ${GLOB_LIB}
	@echo "Done"

debug: FLAG:=${DFLAG} ${FPPMPI}
debug: ${OBJS}
	@echo ""
	$(call colorecho,"compiling $(EXE).f90 ")
	@echo ""
	$(FC) $(FLAG) $(EXE).f90 -o $(DIREXE)/$(EXE) ${GLOB_INC} ${GLOB_LIB}
	@echo "Done"



serial: FLAG:=${FFLAG} ${FPPSERIAL}
serial: ${OBJS}
	@echo ""
	$(call colorecho,"compiling $(EXE).f90 ")
	@echo ""
	$(FC) $(FLAG) $(EXE).f90 -o $(DIREXE)/$(EXE) ${GLOB_INC} ${GLOB_LIB}
	@echo "Done"

serial_debug: FLAG:=${DFLAG} ${FPPSERIAL}
serial_debug: ${OBJS}
	@echo ""
	$(call colorecho,"compiling $(EXE).f90 ")
	@echo ""
	$(FC) $(FLAG) $(EXE).f90 -o $(DIREXE)/$(EXE) ${GLOB_INC} ${GLOB_LIB}
	@echo "Done"

.f90.o:	
	$(FC) $(FLAG) -c $< ${GLOB_INC} 


clean: 
	@echo "Cleaning:"
	@rm -f *.mod *.o *~
	@rm -fv  $(DIREXE)/$(EXE)



#########################################################################


