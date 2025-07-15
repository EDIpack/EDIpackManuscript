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
manuscript. In the following, we address point by point all the issues raised
in their reports.


<!-- *Exact diagonalization (ED) plays a vital role in the study of quantum impurity problems. In this work, the authors present an ED library and describe its usage in considerable detail. While it builds upon the previous EDIpack library, the manuscript introduces sufficient new developments to warrant a separate publication. Notably, several significant extensions and improvements are included, such as a unified framework for zero- and finite-temperature calculations for a wide range of impurity models; access to the full complex frequency plane; access to the Fock space and the ability to evaluate quantities like reduced density matrices; support for inequivalent impurities; integration with other programming languages and scientific libraries; and compatibility with widely used software suites such as TRIQS and w2dynamics.* -->


> *Overall, the paper is well written and highly detailed, allowing new users to install and utilize the library with ease. Furthermore, the comprehensive DMFT tests, demonstrated through a variety of examples and accompanied by corresponding scripts, provide excellent starting points for newcomers. I believe this work makes a valuable contribution to the community and am therefore pleased to recommend its publication in SciPost.*

We thank the referee for their constructive assessment of our work and for recognizing its value in a more general context. We deeply appreciate their recommendation.  


> *On page 3, a large portion of paragraph 3, which introduces DMFT, lacks citations. For example, the authors mention the success of DMFT in capturing key features of various materials, including Mott insulators, heavy fermion compounds, and unconventional superconductors. It would be helpful to include relevant references here to guide interested readers toward further reading.
*

We agree with this comment of the referee. Although it is impossible to do justice to the wide literature accumulated over the years, we have made concerted efforts to incorporate key references that reflect the breadth and depth of research in this field. In the revised version, we have included several citations pertinent to DMFT across the discussed subjects, ensuring that foundational and more recent contributions are acknowledged. This approach aims to provide a balanced overview while addressing the referee's insightful comment. 


> *Perhaps a sentence like “Section 6 provides the conclusions” was intended at the end of Section 1 but was inadvertently omitted?*

We sincerely appreciate the referee's prompt attention to this matter. We must admit that we "inadvertently" overlooked a reference to Section 6, i.e. the conclusions, at the end of the introduction when discussing the manuscript's structure. We resolved this issue in the revised text by including the sentence:   
*"In Sec. 6 we present some concluding remarks and considerations."*



> *Were the spin indices omitted in Eq. (3)? Or do the indices i,j,k,l represent “flavors” that is, combined spin and orbital indices—rather than orbitals alone? The same question applies to the display equation of $H^{int}$ on page 13. This could be confusing to readers, especially since the spin index is also not explicitly shown in the format of the <UMATRIX\_FILE>.restart file described on the same page.*

Thanks for this insightful comment. Indeed, both in Eq.(3) and in the display equation of $H^{int}$ on page 13, the indices $i, j, k, l$  represent "flavors",  corresponding to the combined spin and orbital indices rather than orbitals alone. We acknowledge that this could potentially be confusing, especially given the absence of explicit spin indices in the format of the <UMATRIX\_FILE>.restart file described on the same page.

To clarify this, we have revised the manuscript to explicitly state that the indices denote combined spin and orbital components. Additionally, we will add a note to the relevant sections to highlight this point, ensuring that the readers can interpret the equations and file formats correctly.

We appreciate your attention to this detail and believe that your suggestion will enhance the clarity of our presentation.



> *The last display equation on page 10 seems incorrect, since the creation and annihilation operators do not appear to result in any particle being created or annihilated.*

We express our gratitude to the referee for bringing to our attention the discrepancy in the equations for the bosonic operators. In the revised manuscript, we have rectified this error by modifying the expressions on the right-hand side of the equations to account for the change in the bosonic number. 




> *In Sec. 3.3, it appears that users must manually select one of the three provided symmetry configurations to perform block-diagonalization. Is there a plan to extend the code to automatically detect all relevant symmetries—especially in cases where orbitals or sites possess additional symmetries that would allow further block-diagonalization of the matrix?*

We acknowledge the referee’s observation. Although the code currently necessitates manual selection of one of the provided symmetry configurations, we recognize the value of automating the detection of all relevant symmetries. Regrettably, we do not have any plans to incorporate automatic detection of all pertinent symmetries within the code. In the current setup, this would be feasible through an accurate analysis of the effective bath decomposition, as discussed in section 3.6, excluding simpler cases described by `bath_type=normal, hybrid`.

Nevertheless, we are actively exploring development avenues that aim to integrate more sophisticated conservation laws, which would further reduce the matrix dimensions. We are confident that these enhancements would improve code’s flexibility and efficiency in managing systems characterized by intricate symmetries.






> *On page 43, it is mentioned that the spectrum obtained from ED is “inherently spiky”. What is the value of the broadening parameter used in these simulations? Including this information in the main text may improve the clarity and reproducibility of the paper.*

We appreciate the referee's  observation. As briefly elaborated upon in the manuscript, the inherently "spiky" nature of the spectral function arises due to the finite size of the system under consideration. This finiteness results in a discrete set of poles contributing to the Källén-Lehmann spectral representation. To mitigate the singularities associated with these delta-like poles, a common practice involves applying a broadening technique using a Lorentzian function.

The extent of this broadening is controlled by the input parameter `eps`, which determines the width of the Lorentzian function. It is important to note that the value of `eps` is not fixed universally but rather is chosen based on the specific requirements of each case. In the particular examples discussed on page 43 of our manuscript, we have employed a broadening parameter of `eps = 0.01`, expressed in units of the half-bandwidth `D`.

In response to the referee's valuable suggestion, we have updated the manuscript to explicitly specify the value of this broadening parameter in all relevant examples that illustrate the behavior of the spectral function. We believe this addition enhances the clarity and reproducibility of our results, and we thank the referee for their constructive feedback.

> *for the display equation of $C(z)$ on page 16, summation index $m$ has lower and upper bounds, while index $n$ does not, although they are dummy variables for the same thing. Same for Eq. (14)*

We appreciate the referee's careful observation regarding the summation indices in the display equation of $C(z)$ on page 16 and Eq. (14). To maintain consistency and clarity, we have revised the manuscript to ensure that both indices $m$ and $n$ have clearly defined lower and upper bounds, as they represent dummy variables for the same summation. 

In particular, we now explicitly indicate the upper summation bound for $n$ by using the number $N_{\rm state\_list}$ of eigenstates contained in the `state_list` class and describing the lower end of the energy spectrum.   
Following the referee's observation, we propagated this correction to all the expressions involving a trace over the Hamiltonian spectrum. We appreciate the referee's attention to this detail.



> *"$J_x \rightarrow J_X$" and "$J_p \rightarrow J_P$" in the second paragraph of page 13*

> *“store” $\rightarrow$  “stored” in the last line of page 13*

> *"As discussed" $\rightarrow$ "As will be discussed" at the beginning of Sec. 3.5.2*

> *"$\vec{B_\sigma}$" $\rightarrow$ "$\vec{B}_\sigma$" in the sentence "The values are given by all integers $B_\sigma$ corresponding to..." of page 14*

> *"$w(\mathcal{A})_{mn}^\nu$" $\rightarrow$ "$w_{mn}^\nu(\mathcal{A})$" in the second line after Eq.~(14)*

> *"This example two main goals" $\rightarrow$ "This example has two main goals" on page 46.* 

> *should be no indentation for the sentence right after the first display equation on page 17*
>

We sincerely appreciate the referee's careful review and constructive feedback. In the revised manuscript, we have addressed all the indicated typos and corrections as suggested. We are grateful for the referee’s meticulous attention to detail, which has significantly contributed to improving the clarity and accuracy of our manuscript.

