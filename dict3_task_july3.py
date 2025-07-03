# 1. Invert a dictionary with list values (group keys by their values) 
# Input: 
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
# Output: 
# {1: ['a', 'c'], 2: ['b'], 3: ['d']} 
# (Hint: Use setdefault method) 

#without using Use setdefault method

# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
# res={}
# for x,y in d.items():
#     if y not in res:
#         res[y]=[x]
#     elif y in res:
#         res[y]+=[x]
# print(res)


#using set default()

# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3} 
# res={}
# for x,y in d.items():
#         res.setdefault(y,[]).append(x)
# print(res)

# # 2. Find Max and Min Value in Dictionary 
# # Input: 
# d = {'a': 10, 'b': 5, 'c': 15} 
# # Output: 
# # Max Value → 15 
# # Min Value → 5 

# d = {'a': 10, 'b': 5, 'c': 15} 
# res=[]
# for i in d.values():
#     res+=[i]
# print("max value =>",max(res))
# print("min value =>",min(res)) 

# 3. Create a dictionary using dictionary comprehension for the given list of numbers, 
# where: 
# • Each number is a key. 
# •  
# •  
# The value is "prime" if the number is prime. 
# The value is "notprime" if the number is not prime. 
# Output:   {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}
# a=int(input("enter"))  #10
# res={}
# for i in range (2,a+1):
#     for j in range(2,i):
#         if i%j==0:
#             res[i]="not a prime"
#             break      
#     else:
#         res[i]="is a prime number"
# print(res)
#                              (or)

# a={x:"prime" if all(x%y!=0 for y in range(2,x)) else "notprime" for x in range(2,10)}
# print(a)


# # 4. Create a dictionary from a list of words, keys as words, values as word lengths, but 
# # only for words   longer than 3 characters 
# a=["hi", "hello", "world", "is", "great"] 
# res={}
# for x in a:
#     if len(x)>3:
#         res[x]=len(x)
# print(res)

#          (or)

# # res={i:len(i) for i in a if len(i)>3}
# # print(res)

# Create a dictionary with uppercase letters as keys and their ASCII values as values use 
# dict     
#  a= ['a', 'b', 'c'] 
# Expected Output: 
# {'A': 65, 'B': 66, 'C': 67}

# a= ['a', 'b', 'c'] 
# res={}
# for i in a:
#     res[i.upper()]=ord(i)-32
# print(res)

# 6. Explain about setdefault function in dictionary data type ?


# 1. setdefault() tries to get the value for a given key.
# 2. If the key exists, it simply returns its current value.
# 3.If the key does not exist, it inserts the key with a specified default value, then returns that default.

# 📌 Syntax:
    
# dict.setdefault(key, default_value)

# 1. key: the key to look for.
# 2. default_value (optional): what to insert if the key isn’t already in the dictionary.If not specified, None is used as the default.

# Example:
    
# d = {'a': 10, 'b': 20}
# # Key exists:
# v1 = d.setdefault('a', 0)  # returns 10, d remains {'a': 10, 'b': 20}
# print(v1, d)

# # Key doesn't exist:
# v2 = d.setdefault('c', 99)  # inserts 'c': 99, returns 99
# print(v2, d)

# output:
# 10 {'a': 10, 'b': 20}
# 99 {'a': 10, 'b': 20, 'c': 99}



# # 7. Difference between d[key] and d.get(key)?

# ✅ d[key]
# 1. Accesses the value directly for the key key.
# 2. If the key exists, returns its value.
# 3. If the key does not exist, raises a KeyError exception.

# 🔹 Example:

# d = {'a': 1, 'b': 2}
# print(d['a'])       # 1
# print(d['c'])       # KeyError: 'c'

# ✅ d.get(key[, default])

# 1. Safely tries to get the value for key.
# 2. If the key exists, returns its value.
# 3. If the key does not exist, returns default (which defaults to None) instead of raising an error.

# 🔹 Example:

# d = {'a': 1, 'b': 2}
# print(d.get('a'))          # 1
# print(d.get('c'))          # None (no error)
# print(d.get('c', 99))      # 99 (custom default)
# ✅ Key differences:

# Feature            	 d[key]	                          d.get(key[, default])
# Key missing	      Raises KeyError	                 Returns None or default
# Default value	  Not possible	                     You can specify a default
# Typical usage	  When you're sure the key exists	 When key might not exist



# 8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with 
# examples.

# -------Shallow Copy--------
# A shallow copy creates a new outer object, but the nested (inner) objects are not copied.
# Instead, both the original and the copied object share the same inner objects (same memory reference).

# Example:

# import copy
# s=[[1, 2], [3, 4]]
# shallow=copy.copy(s)
# shallow[0][0]=99
# print("s:",original)  # [[99, 2], [3, 4]]
# print("shallow:",shallow)    # [[99, 2], [3, 4]]

# Explanation:
# 1. Only the outer list is copied.
# 2. The inner lists are the same in both.
# 3. So, a change in one affects the other.

# ------Deep Copy-------
# A deep copy creates a new object and also recursively copies all nested objects.
# Both outer and inner objects are completely separate and independent in memory.

# Example:
# import copy
# s=[[1, 2], [3, 4]]
# deep=copy.deepcopy(s)
# deep[0][0] = 99
# print("s:", s)  # [[1, 2], [3, 4]]
# print("Deep:", deep)          # [[99, 2], [3, 4]]

# Explanation:
# 1. Both outer and inner lists are copied.
# 2. So, changing the deep copy doesn't affect the original.

# Final Summary Table:
# Feature	               Shallow Copy	                 Deep Copy
# Definition	       Copies outer object only	       Copies outer and all nested objects
# Changes affect?	     Yes (for inner objects)	   No, both are fully independent
# Function used	        copy.copy()	                   copy.deepcopy()

