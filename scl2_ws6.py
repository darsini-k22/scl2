#1 derivatives
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

######################################################################

#2 Trapezoidal Method
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

###################################################################

#3 Simpson's 1/3 Rule

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

##############################################################

#4 Simpson's 3/8 Rule
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
