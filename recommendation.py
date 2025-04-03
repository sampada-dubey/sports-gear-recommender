import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load the dataset
data = pd.read_csv("data/sports_gear.csv")

# Combine relevant columns into a single 'features' column
data['features'] = data['Sport'] + ' ' + data['Type'] + ' ' + data['Material']

# Transform features using TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(data['features'])

# Calculate cosine similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend_gear(gear_name, num_recommendations=3):
    if gear_name not in data['Name'].values:
        return ["Gear not found in the database."]
    
    # Find the index of the input gear
    idx = data[data['Name'] == gear_name].index[0]
    
    # Calculate similarity scores
    similarity_scores = list(enumerate(cosine_sim[idx]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    
    # Fetch top recommendations
    recommendations = []
    for i in sorted_scores[1:num_recommendations+1]:
        recommendations.append(data['Name'].iloc[i[0]])
    
    return recommendations
