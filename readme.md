# What?
a function to express the 4 steps of math calculation in markdown format:
step 1, list the formula
step 2, replace the variants with specified values
step 3, simplify the result of step 2
step 4, evaluate the result to float

# How?
```python
T1 = T_Rotate('pi/6 + pi/2', useRad=True)
fOut.write(latexExpression('T1'))
```
will write a markdown file which can be rendered as (no, you can not read it on github easily, please use a good markdown editor)

$$
\begin{align}
T1 &= \left[\begin{array}{r}\cos{\left (\theta_{0} \right )} & - \sin{\left (\theta_{0} \right )} & 0\\\sin{\left (\theta_{0} \right )} & \cos{\left (\theta_{0} \right )} & 0\\0 & 0 & 1\end{array}\right]\\
&=\left[\begin{array}{r}\cos{\left (\dfrac{\pi}{6} + \dfrac{\pi}{2} \right )} & - \sin{\left (\dfrac{\pi}{6} + \dfrac{\pi}{2} \right )} & 0\\\sin{\left (\dfrac{\pi}{6} + \dfrac{\pi}{2} \right )} & \cos{\left (\dfrac{\pi}{6} + \dfrac{\pi}{2} \right )} & 0\\0 & 0 & 1\end{array}\right]\\
&=\left[\begin{array}{r}- \dfrac{1}{2} & - \dfrac{\sqrt{3}}{2} & 0\\\dfrac{\sqrt{3}}{2} & - \dfrac{1}{2} & 0\\0 & 0 & 1\end{array}\right]\\
&=\left[\begin{array}{r}-0.5 & -0.866025403784439 & 0\\0.866025403784439 & -0.5 & 0\\0 & 0 & 1.0\end{array}\right]
\end{align}
$$

# More?
You can define your own functions in class. There are 2 in this release: `T_Rotate` and `T_LOG`

**But I am also seeking for a more common method without supplying every functions by the user**

# License
You can use this function freely only if you mention that "Free expand_expression.py by Li Jun is used. Which can be download from https://github.com/retsyo/expand_expression"

# Bug?
1. please note the parameters are passed as a string not number/expression/sympy's expression
2. if you find more bugs please report/fix it




