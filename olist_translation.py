#%%

import pandas as pd
from deep_translator import GoogleTranslator
import os

# %%

#set your own directory
os.chdir()

reviews = pd.read_csv('olist_order_reviews_dataset.csv')

reviews = reviews[['review_id','review_comment_title','review_comment_message']]

reviews = reviews.dropna()
# %%
reviews['review_comment_title'] = reviews['review_comment_title'].str.slice(0,5000)
reviews['review_comment_message'] = reviews['review_comment_message'].str.slice(0,5000)

#reviews['title_translated'] = GoogleTranslator(source='pt', target='en').translate(reviews['review_comment_title'])
def translate_try(x):
    try:
        return GoogleTranslator(source='pt', target='en').translate(x)
    except:
        return "Failed to translate"
    
#reviews['title_translated'] = reviews.apply(lambda row : translate_try(row), axis = 1)
# %%

reviews['title_translated'] = ''

for i in range(reviews.shape[0]):
    reviews['title_translated'].iloc[i] = translate_try(reviews['review_comment_title'].iloc[i])

# %%

reviews['content_translated'] = ''

for i in range(reviews.shape[0]):
    print(i)
    reviews['content_translated'].iloc[i] = translate_try(reviews['review_comment_message'].iloc[i])

# %%
reviews = reviews[['review_id','title_translated','content_translated']]
# %%
reviews.to_csv('reviews_translated.csv',index=False)
# %%
