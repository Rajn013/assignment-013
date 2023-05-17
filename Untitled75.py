#!/usr/bin/env python
# coding: utf-8

# Can you create a programme or function that employs both positive and negative indexing? Is there any repercussion if you do so?
# 

# In[1]:


def access_element(sequence, index):
    positive_index = index
    negative_index = -index
    print("Positive index:", sequence[positive_index])
    print("Negative index:", sequence[negative_index])


# In[6]:


#for example
list = [1, 2, 3, 4, 5]
access_element(list, 1)


# Q2. What is the most effective way of starting with 1,000 elements in a Python list? Assume that all elements should be set to the same value.
# 

# In[12]:


#The most effective way to create a Python list with 1,000 elements, all set to the same value, is by using list comprehension with the desired value repeated 1,000 times. This approach is efficient and concise

#for example:-


list = [5]* 1000


# In[13]:


list


# Q3. How do you slice a list to get any other part while missing the rest? (For example, suppose you want to make a new list with the elements first, third, fifth, seventh, and so on.)
# 

# In[10]:


list = [1,2,3,4,5,6,7,8,9,10]
new_list = list[1::2]


# In[11]:


new_list


# Q4. Explain the distinctions between indexing and slicing.
# 

# 
# Indexing retrieves a single element using the index inside square brackets, while slicing extracts a subset of elements by specifying a range of indices using square brackets with the colon operator.

# Q5. What happens if one of the slicing expression's indexes is out of range?
# 

# If any index in a slicing expression is outside the valid range, Python handles it without raising an error and returns either an empty sequence or as many elements as possible within the valid index range.

# Q6. If you pass a list to a function, and if you want the function to be able to change the values of the list—so that the list is different after the function returns—what action should you avoid?
# 

# To allow a function to change the values of a list passed as an argument, you should avoid reassigning the list itself to a new object or creating a new list with the same variable name inside the function. Instead, modify the elements of the list directly within the function.

# Q7. What is the concept of an unbalanced matrix?
# 

# The concept of an unbalanced matrix typically refers to a matrix that does not have an equal number of rows and columns. In other words, the number of rows and columns in the matrix is unequal.
# 
# An unbalanced matrix can arise in various scenarios, such as when dealing with irregular data structures or when working with specific mathematical or computational operations that require differently sized dimensions.

# In[ ]:




