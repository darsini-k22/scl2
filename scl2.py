#linear interpolation
x0=float(input('Enter the x0 value: '))
x1=float(input('Enter the x1 value: '))
f0=float(input('Enter the f value of x0: '))
f1 = float(input('Enter the f value of x1: '))
pt = float(input('Enter the given point: '))
f=f0+((f1-f0)/(x1-x0))*(pt-x0)
print('The linear polynomial is: ',f0,'+',((f1-f0)/(x1-x0)),'*(x-(',x0,'))')
print('Estimated value using linear interpolation is: ',f)


#quadratic interpolation
x0=float(input('Enter the x0 value: '))
x1=float(input('Enter the x1 value: '))
x2=float(input('Enter the x2 value: '))
f0=float(input('Enter the f value of x0: '))
f1 = float(input('Enter the f value of x1: '))
f2 = float(input('Enter the f value of x2: '))
pt = float(input('Enter the given point: '))
b0=f0
b1=(f1-f0)/(x1-x0)
b2=(((f2-f1)/(x2-x1))-b1)/(x2-x0)
f=b0+b1*(pt-x0)+b2*(pt-x0)*(pt-x1)
print('The quadratic polynomial is: ',b0,'+(',b1,')*(x-(',x0,'))+(',b2,')(x-(',x0,'))*(x-(',x1,'))')
print('Estimated value using quadratic interpolation is: ',f)


#3 equation of parabola passing through the points

x0=float(input('Enter the x0 value: '))
x1=float(input('Enter the x1 value: '))
x2=float(input('Enter the x2 value: '))
f0=float(input('Enter the f value of x0: '))
f1 = float(input('Enter the f value of x1: '))
f2 = float(input('Enter the f value of x2: '))
b0=f0
b1=(f1-f0)/(x1-x0)
b2=(((f2-f1)/(x2-x1))-b1)/(x2-x0)
f=b0+b1*(pt-x0)+b2*(pt-x0)*(pt-x1)
print('The quadratic polynomial is: ',b0,'+(',b1,')*(x-(',x0,'))+(',b2,')(x-(',x0,'))*(x-(',x1,'))')

#4 newton's divided difference interpolation
#divided diff table and corresponding polynomial

def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;
 
# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
 
# Function for applying Newton's
# divided difference formula
def applyFormula(value, x, y, n):
 
    sum = y[0][0];
 
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);
     
    return sum;
 
# Function for displaying divided
# difference table
def printDiffTable(y, n):
    print('Iteration table: ')
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                               end = " ");
 
        print("");
 
# Driver Code
 
# number of inputs given
n = 4;
y = [[0 for i in range(10)]
        for j in range(10)];
x = [1.0,1.3,1.6,1.9,2.2 ];
 
# y[][] is used for divided difference
# table where y[][0] is used for input
y[0][0] = 0.7651977;
y[1][0] = 0.6200860;
y[2][0] = 0.4554022;
y[3][0] = 0.2818186;
y[4][0] = 0.1103623;
 
# calculating divided difference table
y=dividedDiffTable(x, y, n);
 
# displaying divided difference table
printDiffTable(y, n);
 
# value to be interpolated
value = 1.5;
 
# printing the value
print("\nValue at", value, "is",
        round(applyFormula(value, x, y, n), 2))

#5 newton's divided difference interpolation
#divided diff table and corresponding polynomial

def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;
 
# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
 
# Function for applying Newton's
# divided difference formula
def applyFormula(value, x, y, n):
 
    sum = y[0][0];
 
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);
     
    return sum;
 
# Function for displaying divided
# difference table
def printDiffTable(y, n):
    print('Iteration table: ')
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                               end = " ");
 
        print("");
 
# Driver Code
 
# number of inputs given
n = 4;
y = [[0 for i in range(10)]
        for j in range(10)]
x = [45,50,55,60,65 ];
 
# y[][] is used for divided difference
# table where y[][0] is used for input
y[0][0] = 114.84;
y[1][0] = 96.16;
y[2][0] = 83.32;
y[3][0] = 74.48;
y[4][0] = 68.48;
 
# calculating divided difference table
y=dividedDiffTable(x, y, n);
 
# displaying divided difference table
printDiffTable(y, n);
 
# value to be interpolated
#value =46;
value=63;
# printing the value
print("\nValue at", value, "is",
        round(applyFormula(value, x, y, n), 2))
        
        
#lagrange interpolation
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


#inverse lagrange interpolation
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


#newton's forward interpolation
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
        
 
#newtons bakward interpolation
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


#cubic spline interpolation method
import re
from sympy import Symbol

# Gauss Jordan Elimination
import math
def non_zero(row):
  for i in range(len(row)):
    if row[i] != 0:
      return i

def rref(matrix):
  rows = len(matrix)
  columns = len(matrix[0])
  non_zero_index = -1

  # Arrange the rows by leftmost non-zero entry
  matrix.sort(key = non_zero)
  for i in range(0, rows):
  # Making the first non-zero element 1
    for j in range(columns):
      if not math.isclose(matrix[i][j], 0.0):
        non_zero_index = j
        matrix[i] = [x / matrix[i][j] for x in matrix[i]]
        break

  # Making leading coefficient column corresponding values 0
    for j in range(rows):
      if j == i:
        continue
      else:
        ratio = matrix[j][non_zero_index] / matrix[i][non_zero_index]
        row = [x * ratio for x in matrix[i]]
        matrix[j] = [x - y for x, y in zip(matrix[j], row)]
  print("The given matrix in RREF is:")
  for row in matrix:
    print(row)
  return matrix

# Finding the augmented matrix
def augmented_matrix(eqn_list,eqn_count):
    aug_matrix=[]
    for i in eqn_list:
         val = re.findall(r'[\d\.\-\+]+',i)
         #print(val)
         val = [int(x) for x in val]
         aug_matrix.append(val)
    #print(aug_matrix)
    del aug_matrix[0][0]
    del aug_matrix[eqn_count-1][eqn_count]
    #print(aug_matrix)
    return aug_matrix



def eq(x,y,v,n):
  l=[]
  for i in range(1,n):
    temp=''
    temp+=str(1)
    temp+=str(v[i-1])
    temp+='+'
    temp+=str(4)
    temp+=str(v[i])
    temp+='+'
    temp+=str(1)
    temp+=str(v[i+1])
    temp+='='
    temp+=str(6*y[i-1]-12*y[i]+6*y[i+1])
    #print(temp)
    l.append(temp)
  return l





x_val=[1,2,3,4]
y=[1,2,5,11]
n=len(x_val)-1
v=['x','y','z','a','b']
eq_list=eq(x_val,y,v,n)
aug=augmented_matrix(eq_list,len(eq_list))
aug = rref(aug)
rank = len(aug)
zeros = [0] * len(aug[0])
solution = []
for row in aug:
  if row == zeros:
    rank -= 1
# Unique Solution
if rank == len(aug[0]) - 1:
  for i in range(len(aug) - 1, -1, -1):
    for j in range(len(aug[0]) - 1):
      if math.isclose(aug[i][j], 0.0):
        continue
      else:
        solution.insert(0, aug[i][len(aug[0]) - 1])
  print("Unique Solution:", solution)
# Infinite Solutions
elif rank < len(aug[0]) - 1:
  print("Infinite Solutions")
# No solution
else:
  print("No Solution")
solution.insert(0,0)
solution.append(0)
print(solution)
x = Symbol('x')
p=1.5
final_eq=[]
dif=[]
print('The equations are: ')
for i in range(n):
  d=1/6*(x_val[i+1]-x)**3*solution[i]+1/6*(x-x_val[i])**3*solution[i+1]+(x_val[i+1]-x)*(y[i]-(1/6*solution[i]))+(x-x_val[i])*(y[i+1]-(1/6*solution[i+1]))
  final_eq.append(str(d))
  print(d)
  dif.append(abs(i-int(p-1)))
f_eq_index=dif.index(min(dif))
x=p
f_value=eval(final_eq[f_eq_index])
print('The value using cubic spline is: ',end=' ')
print(f_value)


#derivatives


def difference_table(y):
  for i in range(1,len(y)):
    for j in range(0,len(y)-i):
      y[j][i]=y[j+1][i-1]-y[j][i-1];


x_val=[1.0,1.1,1.2,1.3,1.4,1.5,1.6]
y1=[7.989,8.403,8.781,9.129,9.451,9.750,10.031]
y = [[0 for i in range(len(y1))]
        for j in range(len(y1))]
for i in range(len(y1)):
  y[i][0]=y1[i]

print('Iteration table is: ')
difference_table(y)
for i in range(len(y)):
  for j in range(len(y)):
    if(y[i][j]==0):
      pass
    else:
      print(round(y[i][j],3),end=' ')
  print('\n')  
x0=1.1
index=x_val.index(x0)
#print(index)
h=abs(x_val[0]-x_val[1])
print('First order dervative ',end=' ')
sum=0
for i in range(1,len(y)):
  if i%2==0:
    sum+=-1*(y[index][i])/i
  else:
    sum+=y[index][i]
print(sum/h)
print('Second order dervative ',end=' ')
sum=0
sum=(y[index][2]+y[index][3]+11/12*y[index][i]+5/6*y[index][i])/h**2;
print(sum)

# Trapezoidal Method

# Define function to integrate
def f(x):
    return 1/(1 + x**2)

# Implementing trapezoidal method
def trapezoidal(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        integration = integration + 2 * f(k)
    
    # Finding final integration value
    integration = integration * h/2
    
    return integration
    
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = trapezoidal(lower_limit, upper_limit, sub_interval)
print("Integration result by Trapezoidal method is: %0.6f" % (result) )


# Simpson's 1/3 Rule

# Define function to integrate
def f(x):
    return 1/(1 + x**2)

# Implementing Simpson's 1/3 
def simpson13(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    
    # Finding final integration value
    integration = integration * h/3
    
    return integration
    
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = simpson13(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 1/3 method is: %0.6f" % (result) )


# Simpson's 3/8 Rule
import math
# Define function to integrate
def f(x):
    return 1/math.exp(-x**2)

# Implementing Simpson's 3/8
def simpson38(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 3 * f(k)
    
    # Finding final integration value
    integration = integration * 3 * h / 8
    
    return integration
    
# Input section
lower_limit = float(input("Enter lower limit of integration: "))
upper_limit = float(input("Enter upper limit of integration: "))
sub_interval = int(input("Enter number of sub intervals: "))

# Call trapezoidal() method and get result
result = simpson38(lower_limit, upper_limit, sub_interval)
print("Integration result by Simpson's 3/8 method is: %0.6f" % (result) )

#tapezoidal and simpson method

def trapezoidal(t,v,h):
  sum=0
  for i in range(len(t)):
    if i==0:
      sum+=v[i]
    elif i==len(t)-1:
      sum+=v[i]
    else:
      sum+=2*v[i]
  return sum*h/2

def simpson(t,v,h):
  sum=0
  for i in range(len(t)):
    if i==0 or i==len(t)-1:
      sum+=v[i]
    elif i%2==0:
      sum+=2*v[i]
    else:
      sum+=4*v[i]
  return sum*h/3
t=[0,5,10,15,20,25,30,35,40]
v=[30,24,19.5,16,13.6,11.7,10.0,8.5,7.0]
h=abs(t[0]-t[1])
print('By trapezoidal method: ',end=' ')
print(trapezoidal(t,v,h))
print('By Simpson method: ',end=' ')
print(simpson(t,v,h))
