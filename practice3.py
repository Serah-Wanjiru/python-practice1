# //Concatenate the string 'Thirty', 'Days', 'Of', 'Python' 
# //to a single string, 'Thirty Days Of Python'.
name='Thirty','Days','Of','python' 
l=''
for i in name:
    l=l + ' '+ i
    print(l)
    
# //Write a Python program to check if a given string 
# //is a palindrome or not.
str="level"
str=str.lower().replace("","")
if str==str[::-1] :
    print("it is palindrome")
else:
    "not palindrome" 
    
# //Change Python for Everyone to Python for All using the 
# //replace method or other methods.
name="python for everyone" 
print(name.replace("python for everyone","python for all")) 

# //Split the string 'Coding For All' using space as the separator (split()) .
name="coding for all"
print(name.split())

# //Write a function that takes a list of 
# //numbers as input and returns
# //the sum of all the numbers in the list.
def sumnumbers(numbers):
    l=0
    for i in numbers:
        l+=i
    return l
numbers=[23,12,11,15,16]
print(sumnumbers(numbers)) 

# //Write a function that takes a string as input and returns
# //the string reversed.
def reversestring(str):
    m=str[::-1]    
    return m  
str="mentorship"
# print(reversestring(str))  
# //Write a function that takes 
# //two numbers as input and returns
# //the greatest common divisor 
# //(GCD) of the two numbers. 
def findGCD(a,b):
    while b!=0:
        a,b=b,a%b
    return a
print(findGCD(8,16)) 
# //Write a function that takes a list of integers as input and 
# //returns a new list with only the even numbers from the original
# //list. 
def findeven(*numbers):
    l=[]
    for y in numbers:
        if y%2==0:
            l.append(y)  
    return l
print(findeven(11,12,13,14,15,16,17))
# //Write a function that takes a list of strings as input
# //and returns a new list 
# //with only the strings that have a length greater than 5.
def findlongstring(*strs):
    k=[]
    for e in strs:
        if len(e)>5:
            k.append(e)
    return k
            
print(findlongstring("mentorship","length","watermelonsugar","car","merry"))
# //Write a function that takes a string as 
# //input and returns True if the string is
# //a palindrome, and False otherwise.
def ifpalindrome(name):
    name=name.lower().replace(" ","")
    if name==name[::-1]:
        return True
    else:
        return False

print(ifpalindrome("mum")) 
# //Write a function that takes a string as input and
# //returns a new string with all the vowels removed.
def removevowels(string):
  
    l='aeiouAEIOU'
    for i in l:
        string=string.replace(i, '')       
    return string
n=(removevowels("i love coding" )) 
print(n)
# Write a function that takes a list of strings as input and 
# returns a new list with the strings sorted in alphabetical order.
def sortlist(strings):
   
   return sorted(strings)
strings=["zakia","mary","jane","ann","brenda","serah"]
print(sortlist(strings)) 
# //Write a function that takes a list
# //of numbers as input and returns the average (mean)
# //value of the numbers in the list. 
def numavg(numbers):
    k=sum(numbers)/len(numbers)
    return k
print(numavg([11,12,13,14,15,16,17,18]))
# //Write a function that takes a string as input and
# //returns a new string with all the words in reverse order. 
def reversestrings(strings):
    s=strings[::-1]
    return s
strings="i love coding"
print(reversestrings(strings))
# //Write a function that takes a list of numbers as input and 
# //returns a new list with the numbers sorted in descending order.
def decending(numbers):
    return sorted(numbers,reverse=True)
print(decending([12,45,34,22,89,56,34]))

# //Write a function that takes a list of strings as input 
# //and returns a new list with all the strings converted 
# //to uppercase.
def changestrings(namess):
    l=[]
    for n in namess:
        l.append(n.upper())
    return l
namess=["zakia","mary","jane","ann","brenda","serah"]
print(changestrings(namess))     

     
        
            
    
   
    
    

 
                
       


       
       
   