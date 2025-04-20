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
### Simple Average rating Vs. Weighted Average Rating
The plot demonstrates that average rating alone is not ideal for global recommendations, as many movies with very few votes still appear in the top 20, making the results unreliable. Additionally, the chart highlights the typical long tail distribution in ratings systems: a small number of movies receive most of the votes, while the majority receive very few.
![image](https://github.com/user-attachments/assets/c676f237-0fbe-4750-b2e6-564d6e9a813e)

![image](https://github.com/user-attachments/assets/f61f1199-b6f5-44a0-9f51-09a95823186a)

### TFIDF vs Count Vectorizer

![image](https://github.com/user-attachments/assets/f986ea22-e941-4e16-b35b-cdd24b352e21)
![image](https://github.com/user-attachments/assets/efec95d7-6077-481a-b81c-c1387db45606)
Comparing TF-IDF and Count Vectorizer shows that TF-IDF emphasizes unique words, resulting in more meaningful and diverse clusters, as seen in the scattered t-SNE plot. In contrast, Count Vectorizer is sensitive to common words, grouping documents with similar word counts together, which produces a more structured and less varied t-SNE pattern. The elbow plot for TF-IDF suggests an optimal cluster number at k=4, while Count Vectorizer shows a steep drop with an optimal k=2, reflecting its tendency to form fewer, broader clusters.


![image](https://github.com/user-attachments/assets/24f70bf0-69a2-4426-9dfd-7f7f82d41543)
![image](https://github.com/user-attachments/assets/ad1bf1b2-3c19-4e3f-acf6-6a52a4ca77a5)


![image](https://github.com/user-attachments/assets/21ed9a15-049b-4204-b8ff-41d36f4cf65c)
![image](https://github.com/user-attachments/assets/d6b7790b-fd8d-4754-91f1-27adde4f6c4f)



## Discussion and Future Work
TF-IDF was selected for its effectiveness in recommending movies that are semantically relevant, as it highlights distinctive terms and identifies the closest matches. In the future, we plan to explore deploying the Python Flask application on AWS cloud.
