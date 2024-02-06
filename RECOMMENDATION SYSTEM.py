import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def recommend_movies(user_favorite_movie, movies_df):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genres'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    # Get the index of the user's favorite movie
    movie_index = movies_df[movies_df['Title'] == user_favorite_movie].index[0]

    # Get the pairwise similarity scores with the user's favorite movie
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)
    top_similar_movies = similar_movies[1:6]

    recommendations = []
    for idx in range(len(top_similar_movies)):
        movie_idx, score = top_similar_movies[idx]
        recommendations.append({
            'Movie': movies_df['Title'].iloc[movie_idx],
            'Rating': movies_df['Rating'].iloc[movie_idx],
            'Similarity Score': score
        })

    return recommendations

# Sample movies data with ratings
movies_data = {
    'MovieID': [1, 2, 3, 4, 5],
    'Title': ['Inception', 'The Shawshank Redemption', 'La La Land', 'Avengers: Endgame', 'The Dark Knight'],
    'Genres': ['Action|Adventure|Sci-Fi', 'Drama', 'Comedy|Romance|Musical', 'Action|Adventure|Sci-Fi', 'Action|Crime|Drama'],
    'Rating': [8.8, 9.3, 8.0, 8.4, 9.0]
}

movies_df = pd.DataFrame(movies_data)

# Get user input for their favorite movie
user_favorite_movie = input("Enter your favorite movie: ")

# Get movie recommendations
recommendations = recommend_movies(user_favorite_movie, movies_df)

# Print recommendations
print(f"Top 5 Recommendations for {user_favorite_movie}:")
for recommendation in recommendations:
    print(f"Movie: {recommendation['Movie']} (Rating: {recommendation['Rating']}), Similarity Score: {recommendation['Similarity Score']}")
