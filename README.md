Failure Code Prediction App

This GitHub repository contains code for a Python application that predicts a "Failure Code" based on input text data. The application uses machine learning techniques to make predictions. Specifically, it includes the following components:
Data Preparation: The code reads input data from a CSV file (data.csv) and converts non-string values to strings for consistency. Data is confidential and can't be shared.
Text Vectorization: The input text features are vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) vectorization.
Machine Learning Model: The code uses a Random Forest Classifier for prediction. The model is trained on the vectorized input data.
Gradio Interface: The application utilizes the Gradio library to create a user-friendly interface. Users can input text, and the model predicts a "Failure Code" based on the provided text.
Failure Code Categories: The prediction can fall into one of the following categories: "Software," "Computer," "Microscope," "Hardware," or "Others," depending on the model's output.

Usage :
To use this application, run the code and launch the Gradio interface. Enter your input text, and the model will generate a corresponding "Failure Code."
Feel free to explore, modify, and improve upon this code for your specific needs. If you have any questions or suggestions, please don't hesitate to reach out.
Enjoy using the Final Response Prediction App!
