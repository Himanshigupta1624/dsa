def reverse_string(s):
    result=""
    for char in s :
        result=char+result
    return result

def count_vowel_consotents(s):
    vowel="aeiouAEIOU"
    v=c=0
    for char in s :
        if char.ialpha():
            if char in vowel:
                v+=1
            else:
                c+=1
    return v,c

def min_max(arr):
    min=max=arr[0]
    for x in arr:
        if x<min:
            min=x
        if x>max:
            max=x
    return min,max

def fibonacci(n):
    a,b=0,1
    while a<=n:
        print(a,end="")
        a,b=b,a+b
    print()
def fibnocci_rec(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibnocci_rec(n-1)+fibnocci_rec(n-2)  

def fact(n):
    return 1 if n == 0 else n * fact(n-1)

def freq(s):
    d={}
    for char in s:
        if char in d:
            d[char]+=1
        else:
            d[char]=1
    return d
print(freq("hello world"))

def remove_duplicates(arr):
    seen,result=set(),[]
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result
def sum_of_squares(n):
    s=0
    while n:
        s+=n%10
        n//=10
    return s

def second_largest(arr):
    first=second=float('-inf')
    for x in arr:
        if x>first:
            second,first=first,x
        elif first>x>second:
            second=x
    return second

def merge(a,b):
    i=j=0
    result=[]
    while i <len(a) and j<len(b):
        if a[i]<b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1
    return result + a[i:] +b[j:]   

def flatten(lst):
    result=[]
    for x in lst:
        if isinstance(x,list):
            result.extend(flatten(x))
        else:
            result.append(x)
    return result        
# isinstance(obj, Class) tests whether obj is an instance of Class or of a subclass of Class.
# isinstance(x, list) returns True for actual list objects (and subclasses), False for tuples, strings, numbers, etc.
# Reason to prefer isinstance over type(x) == list: isinstance supports subclasses and is more flexible. type(x) == list is a strict type equality and will reject subclass instances.
# If you want to treat other sequence types (e.g., tuple) as flattenable, check isinstance(x, (list, tuple)) or use 
           