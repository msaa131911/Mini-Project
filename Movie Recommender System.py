import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv(r'E:\ALL_IN_ONE\DATA\tmdb_5000_movies.csv')
credits = pd.read_csv(r'E:\ALL_IN_ONE\DATA\tmdb_5000_credits.csv')

#credits.head(1)['cast'].values
#movies['original_language'].value_counts()


# 2. MERGE DATASET
movies = movies.merge(credits, on='title')

movie = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

movie.isnull().sum()
movie.dropna(inplace=True)
movie.isnull().sum()
movie.duplicated().sum()
movie.iloc[0].genres

def convart(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L
#convart('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')

#ast.literal_eval('[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')

movie['genres']=movie['genres'].apply(convart)
#movie.head()
movie['keywords']=movie['keywords'].apply(convart)
#movie.head()

def convart3(obj):
    L=[]
    counter=0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter+=1
        else:
            break
        
    return L

movie['cast']=movie['cast'].apply(convart3)
#movie.head()
def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
             L.append(i['name'])
     
             break
          
    return L
movie['crew']=movie['crew'].apply(fetch_director)
movie.head()

#movie['overview']=movie['overview'].apply(lambda x:x.split())
#movie.head()
movie['genres']=movie['genres'].apply(lambda x:[i.replace(" ","")for i in x])
movie['keywords']=movie['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
movie['cast']=movie['cast'].apply(lambda x:[i.replace(" ","")for i in x])
movie['crew']=movie['crew'].apply(lambda x:[i.replace(" ","")for i in x])
movie['overview'] = movie['overview'].apply(lambda x: x.split())
#movie.head()
movie['tags']=movie['overview']+movie['genres']+movie['keywords']+movie['cast']+movie['crew']
movie.head()

new_df=movie[['movie_id',"title",'tags']]
#print(new_df)
new_df['tags']=new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags']=new_df['tags'].apply(lambda x:x.lower())
new_df.head()


cv=CountVectorizer(max_features=5000,stop_words='english')
vector = cv.fit_transform(new_df['tags']).toarray()#.shape
#print(vector)


ps=PorterStemmer()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags']=new_df['tags'].apply(stem)

cv.get_feature_names_out()


similarity = cosine_similarity(vector)
#print(similarity[0][0])
sorted(list(enumerate(similarity[0])),reverse=True,key=lambda x:x[1])[1:6]

def recommend(movie):
    movie_index=new_df[new_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movie_list:
        print(new_df.iloc[i[0]].title)

#recommend('Avatar')

input_movie = input("Enter the movie name: ")
recommend(input_movie)