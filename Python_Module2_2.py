
# coding: utf-8

# In[19]:


for i in range (1, 6):
    str = "*"
    for j in range (1, i):
        str = str + "*"
    print(str)

length = len(str)
for j in range (1, len(str) + 1):
    print(str[:length])    
    length -= 1
    

