# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
text = open('common_words.txt','r').read()
word_cloud = WordCloud(background_color='white')
word_cloud.generate(text)
plt.imshow(word_cloud, interpolation = 'bicubic')
plt.axis('off')
plt.show()
