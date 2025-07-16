import streamlit as st
import pickle
import pandas as pd
import requests

mov_data=pickle.load(open('movie_dict.pkl', 'rb'))
movie=pd.DataFrame(mov_data)
sim=pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommondation')


def fetch_poster(mov_id):

    api_key = "7173a16e14115b2280b24e1d21f3100a"
    #mov_id = 550  # Example TMDB movie ID

    url = f"https://api.themoviedb.org/3/movie/{mov_id}?api_key={api_key}&language=en-US"
    res = requests.get(url)

    data = res.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def rec(movies):
    movies_index=movie[movie['title']==movies].index[0]
    dist=sim[movies_index]
    movie_list=sorted(list(enumerate(dist)),reverse=True, key=lambda x:x[1])[1:6]

    rec_mov=[]
    rec_poster=[]
    for i in movie_list:
        mov_id=movie.iloc[i[0]].movie_id
        rec_mov.append(movie.iloc[i[0]].title)
        rec_poster.append(fetch_poster(mov_id))
    return rec_mov, rec_poster



option=st.selectbox ("Select Your Movvie",movie['title'].values)

if st.button('Predict'):
   #selected_movie=rec(option)
    #for i in selected_movie:
        #st.write(i)
    name,poster=rec(option)

    col1, col2, col3, col4, col5 = st.columns(5)


    with col1:

        st.text(name[0])
        st.image(poster[0])
    with col2:

        st.text(name[1])
        st.image(poster[1])
    with col3:

        st.text(name[2])
        st.image(poster[2])
    with col4:

        st.text(name[3])
        st.image(poster[3])
    with col5:

        st.text(name[4])
        st.image(poster[4])
