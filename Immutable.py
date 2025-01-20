#integer
from statsmodels.sandbox.tsa.example_arma import x_acf

a=5
initial_location=id(a)
a=6
initial_location2=id(a)
a=7
initial_location3=id(a)
print(initial_location)
print(initial_location2)
print(initial_location3)

#floate datatype
a1=5.66
initial_location11=id(a1)
a2=6.33
initial_location22=id(a2)
a3=7.33
initial_location33=id(a3)
print(initial_location11)
print(initial_location22)
print(initial_location33)

#string
X="hello"
f_l=id(X)
X="world "
L_l=id(X)
print(f_l)
print(L_l)
 