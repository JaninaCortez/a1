#!/usr/bin/env python
# coding: utf-8

# # Task 1

# 1.	Write a Regular Expression that will match a date that follows the following standard “YYYY-MM-DD”.

# In[ ]:


import re

pattern = "^\d{4}[-](0[1-9]|1[0-2])[-](0[1-9]|[12][0-9]|3[01])$"
user_input = input()
if(re.search(pattern, user_input)):
    print("Matched!")
    
# Reference: https://www.linkedin.com/learning/learning-regular-expressions-2011/matching-dates?u=2175986


# 2.	Write a Regular Expression that will match a North American phone number.

# In[ ]:


import re

phn = "\d{3}-\d{3}-\d{4}"
user_input = input()

if re.search(phn, user_input):
    print("Matched!")
else:
    print("None!")


# 3.	Write a Regular Expression that will match an email address.

# In[ ]:



import re
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu)"
user_input = input()
if(re.search(pattern, user_input)):
    print("valid email")


# In[ ]:


#3 - Another way to execute the code

import re
pattern = "^\w+@\w+\.\w{3}$"
user_input = input()

if re.search(pattern, user_input):
    print("Valid Email")
    
# Reference: https://www.linkedin.com/learning/learning-regular-expressions-2011/matching-email-addresses?u=2175986


# 4.	Write a program to calculate distance so that it takes two Points (x1, y1) and (x2, y2) as arguments and displays the calculated distance, using Class.

# In[ ]:


import math

class distance:
    
    def __init__(self,x1,x2,y1,y2):   #initilizating of class
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def calc(self,x1,y1,x2,y2):     #creating the Function with distancce parameter
        total_distance=math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2) * 1.0)
        return total_distance


# In[ ]:


new=distance(0,0,0,0)   #creating the Object


# In[ ]:


new.calc(3, 4, 4, 3)


# 5. Create random vector of size 50 and replace the maximum value by 0 and minimum value by 100

# In[ ]:


import numpy as np

vector1=np.random.random(50)      #creating the random vector
print(vector1)
vector1[vector1.argmax()] = 0      #replacing the value by max 0 and min 100
vector1[vector1.argmin()] = 100
print("Maximum value replaced by 0:")
print("Minimun value replaced by 100")
print(vector1)


# # Task 2

# 1.	Create below matrix using scipy.

# In[ ]:


# using numpy
import numpy as np
#data = np.zeros(shape=(10,10))
#
#for i in range(0, 10):
#    for j in range(0, 10):
#        if i == j:
#            data[i,j] = 2
#        if i == j + 2 or i + 2 == j :
#            data[i,j] = 1
#            
#print(data)


#using scipy
from scipy.sparse import coo_matrix


m = coo_matrix((10, 10)) #create a 10x10 coo matrix 

m = m.todok() # convert to dok matrix to be able to update it
for i in range(10): # update the dok matrix
    for j in range(10):
        if i == j:
            m[i, j] = 2          # if i and j are equal the data for that point is 2
        if i == j+2 or i+2 == j:
            m[i, j] = 1          # if there is a difference of 2 between i and j, value of that point is 1
            
m = m.tocoo() # convert back to coo
print(m.toarray()) #convert to array and print


# 2.	Reproduce given plot by correcting the below code.

# In[ ]:


from pylab import *

n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2 * X)

plot (X, Y+1, color='blue', alpha=1.00)
fill_between(X, 1, Y + 1, color='blue', alpha=.25)


plot (X, Y-1, color='blue', alpha=1.00)
fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)  #filling the area below (Y - 1) < -1 with red color

show()


# # Task 3

# Write a python code which can get data from Twitter and show in the console

# In[ ]:


import tweepy

consumer_key = 'OIEsYhC1xjyAjMus9jdZ3dAPe'
consumer_secret = 'sH51YdfsIssoaWjADFP6zUYYS6rX0sGCsdoXqV6zc4lG8KlUo1'
access_token = '1301043779638419456-PVcfo9R78IYVwFFasXs2pWkQewODno'
access_token_secret = '01ssgMKtHhsPh2etmi8QSDLBNslOYOVJ3bSNL7xfUZO9Y'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)
screen_name = input("Enter Twitter Id:",)

# fetching the tweets
timeline_tweets = api.user_timeline(screen_name,count=5)

# printing the tweets
for tweet in timeline_tweets:
        print("Tweet:",tweet.text)
        print("Tweet Date:",tweet.created_at)


# In[ ]:




