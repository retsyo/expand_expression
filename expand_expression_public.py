from sympy import *

__version__ = '2018.12.21'

def latexMatrix2Array(strLatex):
    res = strLatex.replace(r'\begin{matrix}', r'\begin{array}{r}')
    res = res.replace(r'\end{matrix}', r'\end{array}')

    return res

class T_Rotate(object):
    idx = 0

    def __init__(self, theta, useRad=False, reset=False):

        if reset == True:
            T_Rotate.idx = 0

        self.eq = '''Matrix([
        [cos(theta{0}), -sin(theta{0}), 0],
        [sin(theta{0}), cos(theta{0}), 0],
        [0, 0, 1]
    ])'''.format(T_Rotate.idx).replace('\n', '')

        self.eq1_0 = sympify(self.eq)
        self.eq1 = latex(self.eq1_0).replace(r'\frac', r'\dfrac')

        # 传进来的是 字符串，转换为 表达式
        if useRad: #  可以实现显示 xx rad、xx°吗？
            self.theta = sympify(theta)
        else:
            self.theta = rad(sympify(theta))

        print('theta = ', theta)
        print('sympify(theta) = ', sympify(theta))
        with evaluate(False):
            if useRad:
                self.eq2 = self.eq1_0.subs({'theta{0}'.format(T_Rotate.idx): sympify(theta)})
            else:
                self.eq2 = self.eq1_0.subs({'theta{0}'.format(T_Rotate.idx): sympify('rad(%s)' % theta)})

        T_Rotate.idx += 1


class T_LOG(object):
    idx = 0

    def __init__(self, x, reset=False):
        if reset == True:
            T_LOG.idx = 0

        self.eq = 'log(x{0})'.format(T_LOG.idx)
        self.eq1_0 = sympify(self.eq)

        with evaluate(False):
            self.eq2 = self.eq1_0.subs({'x{0}'.format(T_LOG.idx): sympify(x)})

        T_LOG.idx += 1

fOut = open('test.md', 'w')

def latexExpression(expr):
    with evaluate(False):
        z1 = sympify(expr).subs({i.name: sympify(globals()[i.name].eq) for i in sympify(expr).free_symbols})

        z2 = sympify(expr).subs({i.name: sympify(globals()[i.name].eq2) for i in sympify(expr).free_symbols})

    z3 = simplify(z2)
    z4 = z3.evalf()

    res = (
        '\n\n$$'
        + r'\begin{align}'
        + '\n%s &= ' % expr
        + latexMatrix2Array(latex(z1))
        + r'\\' +'\n' + '&='
        + latexMatrix2Array(latex(z2))
        + r'\\' +'\n' + '&='
        + latexMatrix2Array(latex(z3))
        + r'\\' +'\n' + '&='
        + latexMatrix2Array(latex(z4))
        + '\n'
        + r'\end{align}$$'
        + '\n\n'
    )

    return res.replace(r'\frac', r'\dfrac')


T1 = T_Rotate('pi/6 + pi/2', useRad=True)
fOut.write(latexExpression('T1'))
fOut.write('\n\n')

T1 = T_Rotate('pi/6', useRad=True)
T2 = T_Rotate('-50')

fOut.write(latexExpression('T1 * T2'))
fOut.write('\n\n')

T3 = T_Rotate('-20')
fOut.write(latexExpression('T3'))
fOut.write('\n\n')

fOut.write(latexExpression('T1 + T2'))
fOut.write('\n\n')

L = T_LOG('sin(pi/3) * 2 + 1')
fOut.write(latexExpression('L'))
fOut.write('\n\n')

L1 = T_LOG('2')
L2 = T_LOG(' 3')
L3 = T_LOG(' 5')
fOut.write(latexExpression('L1 + L2 + L3'))
fOut.write('\n\n')

L4 = T_LOG('30')
fOut.write(latexExpression('L4'))
fOut.write('\n\n')

fOut.close()

