#!/usr/bin/env python
# coding: utf-8

# # 1 Variable
# 
# Excercise solution for variables

# 1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.
# 2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the behavior that you see.
# 3. Store the principal amount, rate of interest and time in different variables and then calculate the Simple Interest for 3 years 
# 

# In[ ]:


# creating variable named pi
pi = 22/7


# In[ ]:


print(pi)


# In[ ]:


# checking the datatype
type(pi)


# In[ ]:


# 2. creating for variable
for = 4


# SyntaxError occured because for is a reserved keyword in python. We cannot use reserved keywords for making variable names.
# 
# Solution for this is:

# In[ ]:


for_ = 4
print(for_)


# It did work this time

# In[ ]:


# 3. Calculate Simple Interest
principle_amount = 567.00
rate_of_interest = 5.6
time = 3


# Now let's calculate the simple intrest using simple math formula:
# 
# `simple interest  = P x R x T / 100`
# 
# where: 
#  
#     P = principle amount
#     R = rate of interest
#     T = time 
# 
# 

# In[ ]:


simple_interest = principle_amount * rate_of_interest * time / 100


# In[ ]:


print(simple_interest)


# In[ ]:


print(type(simple_interest))


# In[ ]:


# total amount after including interest

total_amount = principle_amount + simple_interest
print(total_amount)

