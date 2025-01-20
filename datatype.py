#numaric datatype
from sqlalchemy.engine import TupleResult

age =34 #int datatype
print (age)

marks=88.9#float datatype
print(marks)

complex_number=10+20j
print(complex_number)


#string datatype
name="M Nafiul Alam"
print(name)

#Sequence datatype
#list datatype(order list ,index number )(muitable datatype)
city=["dhaka","rangpur","khulna"]
print(city)

citys=[200,200.66,"khulna"]
print(citys)
city1=["dhaka","rangpur","khulna","dhaka","rangpur"]
print(city1)
#only one value print
latter=["a","b","e","t","r"]
print (latter[3])

#tuple datatype(impmutable datatype)
number=("a","s","c","f","h","f")
number1=("a","s","c","f",3,2,6)
number2=("a","s","c","f",3,2,6,"a","s","c","f",3,2,6)
print(number)
print(number1)
print(number2[5])

#range data type
number4 =range (1,15)#starting by defult =0
print (number4)
print (*number4)
number5=range (0,16,3)
print(*number5)

#boolean type
#ture or false
isbanladeshi=True
print(isbanladeshi)

#None Type
#that means null
take=None
print(take)

#dictionary datatype(mapping datatype)
#ipomportant
person={
    'first_name':'kibria',#key-value
    'last_name':'alam',
    'age':34,
            'Isbangladeshi':True
}
print(person)
print (person['first_name'])
print(person['age'])

#set datatype
#set(spacific no index number )
unique_number ={1,3,4,5,5}#duplicate value avoid kore(index number is not work )
print(unique_number)

#frozenset-immutable
unique_number2=frozenset([1,3,4,5,5,])#duplicate data avoid,unoder data
print(unique_number2)
