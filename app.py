import streamlit as st
import pickle
import pandas as pd

# Title
st.title('Movie Recommendation System 🎬')

# Load pickled data
mov_data = pickle.load(open('movies_dict.pkl', 'rb'))
move_data=pd.DataFrame(mov_data)
sim = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def rec(movies):
    movie_index = move_data[move_data['title'] == movies].index[0]
    dist = sim[movie_index]
    movie_list = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])[1:6]

    rec_mov = []
    for i in movie_list:
        rec_mov.append(move_data.iloc[i[0]].title)
    return rec_mov

# Dropdown for movie selection
option = st.selectbox("Select Your Movie", move_data['title'].values)

# Predict button
if st.button('Predict'):
    selected_movie = rec(option)
    st.subheader("Top 5 Recommended Movies:")
    for i in selected_movie:
        st.write(i)
