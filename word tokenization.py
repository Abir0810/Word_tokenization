#!/usr/bin/env python
# coding: utf-8

# In[1]:


from nltk.tokenize import sent_tokenize , word_tokenize


# In[2]:


ex_text="hello there, how are you doning ?weather is great today and i love python"


# In[4]:


print(sent_tokenize(ex_text))


# In[5]:


print(word_tokenize(ex_text))


# In[8]:


for i in word_tokenize(ex_text):
      print(i)


# In[9]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[10]:


example_sentence = "This is an example showing off stop word filtration"


# In[17]:


stop_words = set(stopwords.words("english"))


# In[18]:


print(stop_words)


# In[19]:


words=word_tokenize(example_sentence)


# In[20]:


filtered_sentence=[]


# In[21]:


for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)
        print(filtered_sentence)


# In[22]:


filtered_sentence=[w for w in words if w in stop_words]


# In[23]:


print(filtered_sentence)


# In[26]:


from nltk.stem import PorterStemmer


# In[27]:


from nltk.tokenize import word_tokenize


# In[28]:


ps=PorterStemmer()


# In[29]:


edx_words=["python","pythoner","pythoning","pytoned","pythonly"]


# In[31]:


for w in edx_words:
    print(ps.stem(w))


# In[32]:


n_text="it is very important to be pythonly while you are pythoning with the python. All pythoners have pythonly once"


# In[34]:


words=word_tokenize(n_text)


# In[36]:


for w in words:
    print(ps.stem(w))


# In[ ]:




