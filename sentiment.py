import pandas as pd
from textblob import TextBlob

df = pd.read_csv('C:/Users/Admin/Desktop/Python/kaggle/youtube.csv')
sentiments = df['Text']
b=sentiments.head(10)


for i in b:
    print("Comment: ",i)
    blob = TextBlob(i)
    polarity = blob.sentiment.polarity
    print("Score: ",polarity)
    if polarity>0:
        print('sentiment: positive')
    elif polarity<0:
        print('sentiment: negative')
    else:
        print('sentiment: neutral')
    if polarity > 0.5:
        print('category: happy')
    elif polarity < -0.5:
        print('category: sad')
    elif polarity <0:
        print('category: rude')
    elif polarity >0:
        print('category: like')
    else:
        print('category: neutral')
    print("\n")















''' if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'
        '''
