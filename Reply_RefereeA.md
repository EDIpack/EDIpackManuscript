<!--We make use of MarkDown in this reply to ease integration with Scipost scheme. 


This comment can be used to learn some of the MD syntax:

long line <double space before new line like \\ in Latex> 
new line
 
# chapter ,## section, ### subsection,...

italic:
*text*

bold:
**text**

blockquote:
> text

highlighted:
==text==

inline math:
$latex math$

display math as for latex doc:
$$
latex math
$$ 

OR

\begin{latex environment, i.e. equation}
latex math
\end{latex environment, i.e. equation}

list:
*
*

enumareted list:
1.
2. 

comments:
see this comment itself

-->



We thank the referee for their time and work in reviewing our
manuscript. Here below we address point by point all the issues raised
in their reports.


<!-- *Exact diagonalization (ED) plays a vital role in the study of quantum impurity problems. In this work, the authors present an ED library and describe its usage in considerable detail. While it builds upon the previous EDIpack library, the manuscript introduces sufficient new developments to warrant a separate publication. Notably, several significant extensions and improvements are included, such as a unified framework for zero- and finite-temperature calculations for a wide range of impurity models; access to the full complex frequency plane; access to the Fock space and the ability to evaluate quantities like reduced density matrices; support for inequivalent impurities; integration with other programming languages and scientific libraries; and compatibility with widely used software suites such as TRIQS and w2dynamics.* -->


> *Overall, the paper is well written and highly detailed, allowing new users to install and utilize the library with ease. Furthermore, the comprehensive DMFT tests, demonstrated through a variety of examples and accompanied by corresponding scripts, provide excellent starting points for newcomers. I believe this work makes a valuable contribution to the community and am therefore pleased to recommend its publication in SciPost.*

We thank the referee for their constructive assessement of our work and for recognizing its value in a more general context. We deeply appreciate their recommendation.  


> *On page 3, a large portion of paragraph 3, which introduces DMFT, lacks citations. For example, the authors mention the success of DMFT in capturing key features of various materials, including Mott insulators, heavy fermion compounds, and unconventional superconductors. It would be helpful to include relevant references here to guide interested readers toward further reading.
*

We totally agree with the referee comment. In the revised version we amended to this issue, including several references to DMFT in each of the mentioned subjects. Although it is nearly impossible to   

> *Perhaps a sentence like “Section 6 provides the conclusions” was intended at the end of Section 1 but was inadvertently omitted?*

Reply:



> *Were the spin indices omitted in Eq. (3)? Or do the indices i,j,k,l represent “flavors” that is, combined spin and orbital indices—rather than orbitals alone? The same question applies to the display equation of $H^{int}$ on page 13. This could be confusing to readers, especially since the spin index is also not explicitly shown in the format of the <UMATRIX\_FILE>.restart file described on the same page.*

Reply: 



> *The last display equation on page 10 seems incorrect, since the creation and annihilation operators do not appear to result in any particle being created or annihilated.*

Reply: 


> *In Sec. 3.3, it appears that users must manually select one of the three provided symmetry configurations to perform block-diagonalization. Is there a plan to extend the code to automatically detect all relevant symmetries—especially in cases where orbitals or sites possess additional symmetries that would allow further block-diagonalization of the matrix?*

Reply: 

> *On page 43, it is mentioned that the spectrum obtained from ED is “inherently spiky”. What is the value of the broadening parameter used in these simulations? Including this information in the main text may improve the clarity and reproducibility of the paper.*

Reply: 

> *"$J_x \rightarrow J_X$" and "$J_p \rightarrow J_P$" in the second paragraph of page 13*

Reply: 

> *“store” $\rightarrow$  “stored” in the last line of page 13*

Reply: 

> *"As discussed" $\rightarrow$ "As will be discussed" at the beginning of Sec. 3.5.2*

Reply: 

> *"$\vec{B_\sigma}$" $\rightarrow$ "$\vec{B}_\sigma$" in the sentence "The values are given by all integers $B_\sigma$ corresponding to..." of page 14*

Reply:  

> *for the display equation of $C(z)$ on page 16, summation index $m$ has lower and upper bounds, while index $n$ does not, although they are dummy variables for the same thing. Same for Eq.~(14)*

Reply: 


> *should be no indentation for the sentence right after the first display equation on page 17*

Reply: 

> *"$w(\mathcal{A})_{mn}^\nu$" $\rightarrow$ "$w_{mn}^\nu(\mathcal{A})$" in the second line after Eq.~(14)*

Reply: 

> *"This example two main goals" $\rightarrow$ "This example has two main goals" on page 46.*

Reply: 



