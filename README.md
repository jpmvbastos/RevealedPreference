# RevealedPreference

This is a simple application to analyze data on observed choices made by individuals. 

It uses insights drawn from economic theory, especially the works of  Samuelson (1938), Houthakker (1950), Arrow (1959), Richter (1966) and Afriat (1967).

## Usage

### Definition 1 (Revealed Preference):

Given some vectors of prices and chosen bundles of quantities of goods $x_1,...,x_N$,  $(p^t, x^t)$ for _t_ = 1,...,_T_, we say that $x^t$ is directly revealed preferred to bundle _q_ if $p^tx^t\geq p^tx$. 

Function ```.revealpref``` can be used to check whether each of the following axioms hold:

### Weak Axiom of Revealed Preference (WARP):

If $p^tq^t \geq p^tx^s$ then $p^sq^s \geq p^sx^t$. 

### Strong Axiom of Revealed Preference (SARP):

Given a set of bundles $B_1, B_2,..., B_n$ where at least two of which are different. If $B_1$ is revealed preferred to $B_2$, $B_2$ to $B_3$, ... , and $B_{n-1}$ to $B_n$, then $B_n$ cannot be revealed preferred to $B_1$.


### Examples

Given a set of vectors of prices and quantities, such as: 

|     | p_1 | p_2 | p_3 |        
|-----|-----|-----|-----|        
| t=1 | 2   | 2   | 2   |        
| t=2 | 1   | 3   | 2   |        
| t=3 | 2   | 1.5 | 5   |  

and   

|     | x_1 | x_2 | x_3 |
|-----|-----|-----|-----|
| t=1 | 2   | 2   | 2   |
| t=2 | 3   | 1   | 2   |
| t=3 | 4   | 1   | 1.5 |

```python

import numpy as np
import pandas as pd

p0 = np.array([2,2,2])
p1 = np.array([1,3,2])
p2 = np.array([2,1.5,5])
prices = pd.DataFrame([p0,p1,p2])

q0 = np.array([2,2,2])
q1 = np.array([3,1,2])
q2 = np.array([4,1,1.5])
quantities = pd.DataFrame([q0,q1,q2])

revealpref(prices, quantities)
``` 


## Additional Resources
For a brief introduction to Revealed Preferences, [see Hal Varian's (2006) paper.](https://github.com/jpmvbastos/RevealedPreference/files/9491879/revpref.pdf)


For other algorithms for revealed preference analysis, [see Gerasimou et al., (2018)](https://github.com/jpmvbastos/RevealedPreference/files/9491853/10.21105.joss.01015-1.pdf)


## References

Afriat, S. N. (1967). The construction of utility functions from expenditure data. _International Economic Review_, 8(1), 67. doi:10.2307/2525382

Arrow, K. J. (1959). Rational choice functions and orderings. _Economica_, 26(102), 121. doi:10.2307/2550390

Gerasimou et al., (2018). Prest: Open-Source Software for Computational Revealed Preference Analysis. _Journal of Open Source Software_, 4 3(30), 1015. https://doi.org/10.21105/joss.01015

Houthakker, H. S. (1950). Revealed preference and the utility function. _Economica_, 17(66), 159. doi:10.2307/2549382

Samuelson, P. A. (1938). A note on the pure theory of consumer’s behaviour. _Economica_, 5(17), 61. doi:10.2307/2548836

Varian, H. R. (2006). Revealed Preference. Working paper.
