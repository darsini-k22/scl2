#1 lagrange interpolation
def lagrange_interpolation(x:list,y:list,xi:int,n:int):
    result=0.0
    for i in range(n):
        term=y[i]
        print(term)
        for j in range(n):
            if j!=i:
                term=term*(xi-x[j])/(x[i]-x[j])
        result=result+term
        print(result)
    return result


x=[5,6,9,11]
y=[12,13,14,16]

print(lagrange_interpolation(x, y, 10, 4))

####################################################################

#2 inverse lagrange interpolation
def inverse_lagranges_interpolation(n,x,y,yi):
    result=0
    for i in range(n):
        term=x[i]
        for j in range(n):
            if(i!=j):
                term=term*(yi-y[j])/(y[i]-y[j])
        result=result+term
        print('result',result)
    return result

x=[2,5,8,14]
y=[94.8,87.9,81.3,68.7]

print('Final value:',inverse_lagranges_interpolation(4, x, y, 85))

####################################################################

#3 newton's forward interpolation
def u_cal(u, n):
 
    temp = u;
    for i in range(1, n):
        temp = temp * (u - i);
    return temp;
 
# calculating factorial of given number n
def fact(n):
    f = 1;
    for i in range(2, n + 1):
        f *= i;
    return f;
 
# Driver Code
 
# Number of values given
n = 7
x = [ 3,4,5,6,7,8,9]
     
# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
        for j in range(n)]
y[0][0] =4.8
y[1][0] =8.4
y[2][0] =14.5
y[3][0] =23.6
y[4][0] =36.2
y[5][0] = 52.8
y[6][0]=73.9 
# Calculating the forward difference
# table
for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
 
# Displaying the forward difference table
for i in range(n):
    print(x[i], end = "\t");
    for j in range(n - i):
        print(y[i][j], end = "\t");
    print("");
 
# Value to interpolate at
#value = 3.5;
value=8.5
# initializing u and sum
sum = y[0][0];
u = (value - x[0]) / (x[1] - x[0]);
for i in range(1,n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i);
 
print("\nValue at", value,
      "is", round(sum, 6));
        
####################################################################

#4 newtons bakward interpolation
def u_cal(u, n):
    temp = u
    for i in range(n):
        temp = temp * (u + i)
    return temp
 
# Calculating factorial of given n
def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f
 
 
# Driver code
 
 
# number of values given
n = 7
x = [ 3,4,5,6,7,8,9]
 
# y is used for difference
# table and y[0] used for input
y = [[0.0 for _ in range(n)] for __ in range(n)]
y[0][0] =4.8
y[1][0] =8.4
y[2][0] =14.5
y[3][0] =23.6
y[4][0] =36.2
y[5][0] = 52.8
y[6][0]=73.9 
# Calculating the backward difference table
for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]
 
 
# Displaying the backward difference table
for i in range(n):
    for j in range(i + 1):
        print(y[i][j], end="\t")
    print()
 
# Value to interpolate at
value = 8.5
 
# Initializing u and sum
sum = y[n - 1][0]
u = (value - x[n - 1]) / (x[1] - x[0])
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)
 
print("\n Value at", value,  "is", sum)

####################################################################

#5 cubic spline interpolation 
from sympy import *
x = [1, 2, 3, 4]
y = [1, 5, 11, 8]
X0 = 1.5

h = x[1] - x[0]
n = len(x) - 1
X = symbols('X')
m = symbols('m0:%d' % (n + 1))
M = {0: 0, n: 0}
expr = []

for i in range(1, n):
    expr.append(m[i - 1] + 4 * m[i] + m[i + 1] - 6 * (y[i - 1] - 2 * y[i] + y[i + 1]) / h ** 2)
    for j in M:
        expr[i - 1] = expr[i - 1].subs(m[j], M[j])

sol = solve(tuple(expr), tuple(m))

for i in range(len(sol)):
    M[i + 1] = sol[m[i + 1]]

ind = 0
for ind in range(n + 1):
    if X0 <= x[ind]:
        break

Y = (x[ind] - X0) ** 3 * M[ind - 1] / (6 * h) + (X0 - x[ind - 1]) ** 3 * M[ind] / (6 * h) + (x[ind] - X0) / h * (y[ind - 1] - (h ** 2 * M[ind - 1]) / 6) + (X0 - x[ind - 1]) / h * (y[ind] - h ** 2 * M[ind] / 6)
print(Y) 
