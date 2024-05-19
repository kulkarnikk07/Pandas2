# Pandas2
# 1 Problem 1 : Article Views I	(	https://leetcode.com/problems/article-views-i/  )

import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    #df = df.drop_duplicates(subset = ['author_id'], inplace = False) # when inplace = False then it will store the new result in new variable
    df.drop_duplicates(subset = ['author_id'], inplace = True) #duplicates will be removed in the same dataframe
    df.sort_values(by = ['author_id'], inplace = True)
    return df[['author_id']].rename(columns={'author_id':'id'})

# 2 Problem 2 :Invalid Tweets	(	https://leetcode.com/problems/invalid-tweets/ )

import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15 ]
    return df[['tweet_id']]  