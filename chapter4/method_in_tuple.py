a=(True,"dhanish",4.4,1,False)

print(a.count(False))
print(a.index("dhanish")) # it will only count the first occurance

#concatenation

var1=(1,"dhan",40.5)
var2=(1,"dhan",40,False)
concatenated_tuple=var1+var2
print(concatenated_tuple)

#repetition

b=("dhan",485, True)
print(b*2)

#Membership : to check whether the item exist


print(2 in a)
print(8 in b)

#length
a=(1,True,"dhanish",4.4)
print(len(a))

# to find minimum and max
a=(1,2,3,4.4)
print(min(a))
print(max(a))
print(sum(a))

# unpacking : Tuple can be unpacked into individual variables

my_tuple=(1,3,4)
a,b,c=my_tuple
print(a,b,c)# the value of my_tuple will be assigned to a,b,c
