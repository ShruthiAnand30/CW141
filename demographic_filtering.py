import pandas as pd
import numpy as np
df = pd.read_csv("final.csv")
m = df['vote_count'].quantile(0.9)
C = df['vote_average'].mean()
q_movies = df.copy().loc[df["vote_count"]>=m]

def weighted_rating(x,m = m,C = C):
  v = x["vote_count"]
  R = x["vote_average"]
  return (v / (v+m)) * R + (m / (v+m)) * C
q_movies["score"] = q_movies.apply(weighted_rating,axis = 1)
q_movies = q_movies.sort_values("score",ascending = False )
output = q_movies[["original_title","poster_link","release_date","vote_count", "vote_average", "overview"]].head(10).values.tolist()