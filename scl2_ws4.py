#1 linear interpolation
x0=float(input('Enter the x0 value: '))
x1=float(input('Enter the x1 value: '))
f0=float(input('Enter the f value of x0: '))
f1 = float(input('Enter the f value of x1: '))
pt = float(input('Enter the given point: '))
f=f0+((f1-f0)/(x1-x0))*(pt-x0)
print('The linear polynomial is: ',f0,'+',((f1-f0)/(x1-x0)),'*(x-(',x0,'))')
print('Estimated value using linear interpolation is: ',f)

###########################################################

#2 quadratic interpolation
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

###########################################################

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

###########################################################

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

###########################################################

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
