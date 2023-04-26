# def add_numbers(num1,num2,num3):
#     result=num1+num2+num3
#     return result
# result=add_numbers(100,200,100)
# print("sum ",result)

# def multiply(numb1,numb2,numb3,numb4):
#     hello=numb1*numb2*numb3*numb4
#     return hello
# hello=multiply(10,10,10,10)
# print("product",hello)

# def greet(name,statement):
#     print("Hello",name,statement)
# greet("Serah","what a you doing now")    
    
# def year_of_birth(name,age):
#     year=2023-age 
#     print(f"Hello {name} you were born in {year}")
# year_of_birth("Serah",18)    
# # //default arguments(s) 
# def big_country(country):
#     print(f"Hello you are from {country}")
# big_country("kenya")  

# //Concatenate the string 'Thirty', 'Days', 'Of', 'Python' 
# //to a single string, 'Thirty Days Of Python'.
namess=["Thirty","Days","Of","Python"]
ans=' ' 
for z in namess:
    
    ans=ans+' '+z
    
    print(ans)
# //Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
g=["Coding","For","All"] 
m=' ' 
for k in g:
    
    m=m+ ' '+ g
    print(m)
    
  
def swap(list):
    get=list[-1],list[0] 
    list[0],list[-1]=get
    return list
newlist= [12,34,22,45,67,64] 
print(swap(newlist)) 
listt=[1,2,3,1,4,3,5,6,2]
l=[]
for i in listt:
    if i not in l:
        l.append(i)
print(l)  

naames=["apple","oranges","lemon","apple","oranges"]
k=[]
for n in naames:
    if n not in k:
        k.append(n)
print(k)  

nj=["i","love","coding"]
mn=''
for j in nj:
    mn=mn+" "+j
print(mn)    

    
     
  
          
    
     