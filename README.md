**VERA - Verifying Remedies Assertions**

This project is a machine learning web app designed to assess the evidential basis of unconventional home remedies and combat the proliferation of online health misinformation.

The model was trained on the train_data.csv dataset and is deployed as an interactive web app using Gradio.

[Link to your live Hugging Face Space app]

**About The Project**

This repository contains all the code for the project, including:

1. The Jupyter Notebook used for data cleaning, analysis, and model comparison.

2. The saved (serialized) machine learning model and vectorizer.

3. The app.py file that runs the user-facing Gradio web app.

**Models Comparison**

During the analysis, three different models were trained and evaluated. The model with the best performance (based on AUC and F1-Score) was chosen for the final app.

**Model_________________Accuracy__________AUC Score__________F1-Score (Real)**

**SVM**____________________0.9612____________0.9938______________0.9616

**LR**______________________0.9523____________0.9907______________0.9531

**Random Forest**________0.9482____________0.9905______________0.9486

