# //write a function that takes in two 
# //numbers and returns their sum.
def add(a,b):
    return a+b
print(add(12,11))
# //Create a function that takes in a list of numbers and returns 
# //the largest number in the list.
def number(*numbers):
   x= max(numbers)
   return x
print(number(23,14,56,15,11,78,56))
# //Write a function that takes in a string and returns 
# //the length of the string.
def length(name):
    return len(name)
print(length("serah"))
# //Create a function that takes in a list of strings and returns a new list with all
# //the strings in uppercase.
def strings(*names):
    l=[]
    for x in names:
        l.append(x.upper())
    return l
        
    
print(strings("serah","jane","caro")) 
def me(*namess):
    e=[]
    for p in namess:
        e.append(p.upper())
    return e 
print(me("esther","lynn","ann")) 
# //Write a function that takes in a list of numbers and returns 
# //the average of those numbers. 
def nuums(*numb):
    w=sum(numb)/len(numb)
    return w
print(nuums(12,13,14,15,16))
# //Create a function that takes in a string and counts the 
# //number of vowels in the string.
def countvowel(vowel):
    num_vowels =0
    for m in vowel:
        if m in "aeiouAEIOU":
           num_vowels +=1
    return num_vowels

x =countvowel ("i love coding")
print(x)
# //Write a function that takes in a list of strings and returns a new list with
# //all the strings sorted in alphabetical order.
def sorting(*naames):
    return sorted(naames)       
b=sorting("serah","lynn","brenda","ann") 
print(b) 

# //Write a function that takes in a list of numbers and returns a new list with 
# //only the even numbers from the original list. 
def findeven(*numberss):
    k=[]
    for j in numberss:
        if j%2==0:
            k.append(j)
    return k  
t=findeven(1,2,3,4,5,6,7,8)  
print(t) 

# //Write a function that takes in a list of
# //numbers and returns a new list with the numbers in reverse order. 
def reversenum(str):
    return str[::-1]
tl=reversenum("serah")  
print(tl)     
# //Write a function that takes in a list of numbers
# //and returns the product of all the numbers in the list.
def multiply(*product):
    u=1
    for q in product:
        u*=q
    return u
ty=multiply(56,23)  
print(ty) 
# //Create a function that takes in a list of strings and returns a new list with
# //only the strings that have more than five characters.
def yatch(*strr):
    for g in strr:
        if len(g)>5:
           return g
bi=yatch("serah","lynn","brenda","ann") 
print(bi) 

# //Write a function that takes in a list of numbers and
# //returns a new list with the numbers in reverse order.  
def reversenumb(*integers):
    return integers[::-1]
l=reversenumb(12,13,14,15,16)  
print(l)
# //Create a function that takes in a string and returns
# //the string with all the vowels removed.
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        s = s.replace(vowel, '')
    return s
        
xl =remove_vowels("i love coding")
print(xl)  

def l(m):
    k='aeiouAEIOU'  
    for ti in k:
        m= m.replace(ti, '') 
    return m
    
xll =l("i love  music")
print(xll)
# //Create a function that takes in a sentence and returns the 
# //sentence with all the words in reverse order.
def vm(hu):
    gh=hu.split()
    njk=''.join(reversed(gh))
    return njk
xll =vm("i love  music")
print(xll)
# //function that takes in a list of numbers and returns
# //a new list with the numbers squared.
def squarenum(*square):
   return[num**2 for num in square]
        
mk=squarenum(1,2,3,4,5,6)
print(mk) 

def mybirth(name,age):
    x=2023-age 
    print(f"Hello {name} you were born in {x} ")  
    
mybirth("serah",18)  

# //Write a function that takes an array of integers and returns
# //the sum of all the even numbers in the array. 
def sumeven(*even):
    g=0
    for i in even:
        if i%2==0:
         g=g+i 
    return g
k=sumeven(1,2,3,4,5,6)  
print(k) 

# //Write a function that takes an array of integers and returns
# //the sum of all the odd numbers in the array.
def sumodd(*odd):
    g=0
    for i in odd:
        if i%2!=0:
         g=g+i 
    return g
k=sumodd(1,2,3,4,5,6)  
print(k)  
# //Write a function that takes an array of integers and returns the
# //largest number in the array.
def largestnum(*num):
    k=max(num)
    return k
v=largestnum(12,34,56,33,11)
print(v)

# numb =(9,3,4,0,1,2,10,22)
def sortss(numb):
    numb.sort(reverse = True)
    return numb
print(sortss([2,0,1,5,3,9,7,5,8,7]))

        
       
    
       

          
    


        
    
    

    