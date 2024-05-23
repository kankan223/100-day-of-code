
#Typecasting in python 

a = '1'        # a string variable
b = '2'

print (a + b)

# it is an eplicite type conversion  ---->   user converts the data type
print (int(a) + int(b))        #typecasting is used to change the type of a variable

c = 1.5
d = 6
print (c + d)      #implicit conversion ----> python converts the data type

#multiline string can be written using ''' ''' or """ """
print("""I am a good programmer
Coz I don't have a life""")       #it can be used to write string without using escape characters


#--------------------------------------------------------------------------------------------------


#sting is like an array

name = "programmer"

print(name[0])        #the index in an array starts from 0 and ends in n-1 where n is the number of characters
print("\n")

#to print every character we can use a loop or write line 5 manually
for i in name:                   #for loop starts from 0 until the condition is true
    print(i)

print ("\n", len(name))          #used to find the length of the string

print (name[1:3])      # used to print the characters from index 1 but 3rd index is 
#                      # neglected .. prints 2 characters   
print (name[:3])       # if the starting index is not mentioned then it starts from 0
print (name[:])        # if the total number of characters is not mentioned then it replace 
#                      # with the lenght of the variable
print (name[0:-4])     # same as (name[ 0 : len(name) - 4])
print (name[-6:-3])    # same as (name[ len(name) - 6 : len(name) - 3])
