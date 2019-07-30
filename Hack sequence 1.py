#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=["neelesh",23,56,"ravi","sona"]
list


# In[14]:



for counter in list :
    if counter=="neelesh" :
        print("the name is found {}" .format(counter))
        break
else :
            print("the number is not in list")


# In[33]:


if "neelesh" in list:
 print("bingo")


# In[18]:


list.append("sadhana")


# In[19]:


list


# In[20]:


list.insert(1,45)


# In[21]:


list


# In[22]:


list.sort()


# In[1]:


list2=[68,34,21,98,32]
list2.sort()


# In[24]:


list2


# In[25]:


list3=["ravi","nad","johny","momy","random"]
list3.sort()


# In[26]:


list3


# In[31]:





# In[34]:


if "johnhy" in list3:
 print("yes he is")


# In[35]:


list3


# In[36]:


if "johny" in list3:
    print("yes bingo")


# In[3]:



if "johny" in list3:
    print("johny is there")
else:
    print("johny not in list")


# In[4]:


list3


# In[5]:


list


# In[6]:


names=["rekha","seema","nalini","priya","sonakshi"]
names


# In[7]:


if "seema" in names:
    print("seema found")
else:
    print("seema not found")


# In[9]:


name=input("enter the name to be founded")
if str(name) in names:
    print("the name is found {}".format(str(name)))
else:
    print("name is not found")


# In[12]:


name2=input("enter the name to be searched")
for c in names:
    if c==str(name2):
        print("bingo we found the name, which is: {}".format(str(name2)))
        break
else:
    print("sorry the asked name does not exists")


# In[23]:


name3=input("enter the name to be searched")
d=0;
for d in range(len(names)):
    if names[d]==str(name3):
        print("bingo name is found, which is {}".format(names[d]))
        break
else:
    print("name is not found")


# In[17]:


names


# In[18]:


names.insert(2,35)


# In[19]:


names


# In[1]:


dict={"neelesh":"123","ravi":"245"}


# In[2]:


dict


# In[3]:


dict["neelesh"]


# In[12]:



    clear


# In[14]:


def square(number):
    return number*number


# In[18]:


nos=square(7)
nos
print("the square of the number is {}".format(int(nos)))


# In[19]:


list=[56,32,67,89,32,65]


# In[20]:


list


# In[23]:


def add(num2):
    return num2*2
add(4)


# In[24]:


list(map(add,list))


# In[ ]:




