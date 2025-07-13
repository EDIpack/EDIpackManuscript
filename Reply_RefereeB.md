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



> *This paper presents the current status in an exact diagonalisation impurity solver EDIpack. It provides a detailed exposition of the multiple interfaces as well as a number of tutorial-style examples that provide details that will be appreciated to new users of the package. I believe that providing robust and well-tested computer codes, as well as high quality documentation, are a big service to the community. I wholeheartedly recommend this work for publication.*

Reply: 


> *On p. 8, function {\tt ed\_set\_Hloc} is introduced, but without much further information. Maybe the reader could be referred to some later section where its use is illustrated.*

Reply: 

> *On p. 9, the discussion about the phonon cutoff sounds potentially a bit misleading. The cutoff is surely problem dependent, and there are (generalized) cases where the shift A\_m cannot be considered as a free parameter.*

Reply: 

> *I find the discussion at the end of page 11 somewhat unclear, especially the terminology. Is this a discussion of consecutive indexing vs. occupation number representation?*

Reply: 

> *The motivation of including the code on p. 12 is unclear. What is the intention here?*

Reply: 

> *Parenthesis missing in the equation at the bottom of p. 12.*

Reply: 

> *Bottom of p. 13: "are store" -> "are stored"*

Reply: 

> *Top of p. 14: What is global share, what are istart, ishift, iend? I suppose this is Fortran-specific.*

Reply: 

> *p. 16: GFmatrix is said to be a critical component for high-speed execution. Maybe it could be describe in more detail? In what way is it efficient? What does it mean it is multi-layed? In passing, it would be nice if the capitalization would be uniform, e.g. GFmatrix vs. gfmatrix (I understand that Fortran compiler does not care, but the human reader perhaps does).*

Reply: 


> *A trick for computing off-diagonal functions is presented on p. 21. Doesn't this require switching to complex-valued floating points even in cases where the Hamiltonian is purely real?*

Reply: 

> *In Eq. (18), is Z the same on both sides of approximation sign?*

Reply: 

> *Are the code listings on p. 25 and p. 26 of sufficient interest to readers?*

Reply: 

> *p. 28: "as the nonsu2 and superc diagonalizations entail nontrivial subtleties in optimizing the off-diagonal components of X". What are these subtleties?*

Reply: 

> *As a general coding comment: would it be possible to remove use of global variables?*

Reply: 

> *p. 40: I find the discussion of parallelism in Julia wrapper unnecessary. Such information does not necessarily age well. This belongs to a readme file.*

Reply: 

> *p. 41: "an comprehensive" -> "a", "fo manipulating" -> for*

Reply: 

> *p. 41: The code listing mentions Wband and de, but I don't see where this is coming from.*

Reply: 

> *p. 42: "provides access to well-tested functions". This is unclear. Functions doing what?*

Reply: 

> *p. 46: This example two main goals: missing "has"?*

Reply: 

> *p. 47: generate_kgrid is confusingly complex. There must be a simpler way to accomplish this.*

Reply: 

> *p. 57: Is the footnote necessary? Will it be of interest to the expected readers of this paper?*

Reply: 


