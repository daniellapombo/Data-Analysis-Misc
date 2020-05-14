# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:27:52 2020

@author: danie
"""
import numpy as np
import pandas as pd
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

#Code is inpsired by https://www.datacamp.com/community/tutorials/wordcloud-python

txt_doc = pd.read_csv('Work Values.txt')
print(txt_doc)
print(txt_doc.shape)
print(txt_doc.iloc[:,0])

#Prep data for WordCloud input format
txt = ''
for word in txt_doc.iloc[:,0]:
    new = ' '+ word
    txt += new

print(txt)
# Create and generate a word cloud image:
wordcloud = WordCloud(width = 6000, height = 3000, 
                background_color ='white',  
                min_font_size = 40, margin = 0).generate(txt)

## Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
plt.savefig('workValuesWordCloud.png')