# Movie Recommendation System Using Flask Python App and Containerizing using Docker

## Table of Contents
* Background
* Project Overview
* Results
* Discussion and Future Work

## Background
I have always been fascinated by how recommendation systems work and how companies like Netflix, Spotify, YouTube, and Amazon seem to know exactly what products, movies, or songs to suggest to their users. Although I have previously worked on building recommendation systems, this time my focus is on testing, deploying, and visualizing a content-based recommender system using Flask, Docker, and simple HTML. 
This project will allow me to explore not only the core functionality of recommendation engines but also the practical aspects of bringing such a system to life in a real-world, interactive web application.

## Data Preparation, Cleaning and Processing
This stage of the project involved merging the movies dataset with the credits dataset, removing empty rows, and selecting features relevant to the recommendation task. Key attributes were extracted from each feature column and then combined into a single consolidated feature column (the "tags" column) to ensure standardization, dimensionality control, and effective feature engineering. Stemming was subsequently applied as an additional preprocessing technique to reduce words to their base forms.

## Model Building and Similarity Score Computation
A simple recommender was first designed. This recommender computes the weighted average rating for each movie and ranks them accordingly. The weighted average rating helps reduce popularity bias and can be used to recommend globally popular movies to users when there is no prior user-user or user-item interaction data available.

The content-based filtering model utilizes preprocessed movie features and applies CountVectorizer or TFIDF to convert words into numerical features, identifying which words are most significant based on their frequency. Term Freuency Inverse Document Frequency (TFIDF) counts the Term Frequency accounts for frequency of each word in a movie and the inverse document frequency counts the frequency ofn the words across the corpus. 

The TF-DF scores are then computed by multiplying the results of TF and IDF and the resulting scores shows the importance of each word across the entire document. Count vectorizer  on the other hand only accounts for the frequency of the occuring words. The cosine similarity scores are then computed using either TFIDF or count vectorizer For highly similar movies, the cosine similarity score approaches 1; for less similar movies, the score is closer to 0; and for completely dissimilar movies, the score is near -1.

## Testing and Containerzing
With the cosine similarity scores computed and the movie recommendation model built, both the similarity scores (saved as similarity.pkl) and the recommendation model (saved as model.pkl) were stored within a virtual environment. 

Flask—a widely used Web Server Gateway Interface (WSGI) framework—was leveraged to develop a Python-based web application for delivering interactive recommendations. The necessary dependencies were installed, an application file was created to define the app’s functionality, and a route was established to serve the Flask app’s webpage. Additionally, a templates folder was used to store the HTML files that would render the web interface hosting the application

After confirming that the Python app works locally through thorough testing, Docker was utilized to enhance scalability, portability, and ease of distribution. This approach ensures robust deployment and streamlined maintenance of the Python Flask application. A Dockerfile was created to instruct Docker on how to build the Docker image. Subsequently, the Docker image was built, and the container was run and tested successfully.

## Results
T-SNE and 


## Discussion and Future Work
