
# //Concatenate the string 'Thirty', 'Days', 'Of', 'Python'
# //to a single string, 'Thirty Days Of Python'.
def str(*name):
    a=''
    for i in name:
        a=a+" "+i
        print(a)
str("Thirty","Days","of","coding") 

def numbers(*numb):
    let=[]   
    for b in numb:
        if b not in let:
            let.append(b)   
            print(let) 
numbers(1,2,3,2,1,3,4,5,4) 

numberss=[45,12,13,78,3,52,7]
b=max(numberss) 
print(b)  


def number( *num):
    large=num[-1]
    for x in num:
        if x<large:
            large=x
            return large
large=print(number(45,12,13,78,3,52,7)) 
   
   
def yes(*numbb):
    j=numbb[0]
    for v in numbb:
        if v>j:
            j=v
            return j
j=print(yes(1,45,21,12))  

def panther(*numbuer):
    if len(numbuer)==0:
        return None
    minnum=min(numbuer) 
    maxnum=max(numbuer) 
    avg=sum(numbuer)/len(numbuer)    
    return(minnum,maxnum,avg) 
print(panther(1,2,3,4,5,6,7,8,9,10))  

