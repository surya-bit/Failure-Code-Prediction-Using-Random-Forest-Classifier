# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

################################################ Final Response prediction
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df=pd.read_csv('data.csv')
# Convert any non-string values to string
df = df.astype(str)

X = df['input']
y = df['output']

# Vectorize the input text features
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

randomfores = RandomForestClassifier()
randomfores.fit(X_train, y_train)

import gradio as gr

def generate(text):
    results = model.predict(text)
    input_vec = vectorizer.transform([text])
    output = randomfores.predict(input_vec)
    results=str(results[0])[-4]
    if results == "S":
      results = "Software"
    elif results== "C":
      results= "Computer"
    elif results == "M":
      results="Microscope"
    elif results== "H":
      results="Hardware"
    else:
      results="Others"


    input_vec = vectorizer.transform([text])
    output = randomfores.predict(input_vec)
    final_response = output
    failure_code= results

    generated_output ="Failure Code: " + failure_code+ "                                                                                                                                                                                                                                     "+ "Final Response:"+ final_response


    return generated_output


demo = gr.Interface(
    fn=generate,
    inputs=gr.inputs.Textbox(lines=10, label="Input Text"),
    outputs=gr.outputs.Textbox(label="Generated Text")
)

demo.launch()
