import gradio as gr
import joblib

# LOAD YOUR SAVED MODEL AND VECTORIZER 

try:
    model = joblib.load('best_model.joblib')
    vectorizer = joblib.load('vectorizer.joblib')
    print("Model and vectorizer loaded successfully.")
except FileNotFoundError:
    print("Error: Model or vectorizer files not found.")
    print("Please make sure 'best_model.joblib' and 'vectorizer.joblib' are in the correct folder.")
    exit()

# DEFINE THE PREDICTION FUNCTION 

def predict_claim_validity(claim_text):
    
    # 1. Prepare the input
    claim_list = [claim_text]
    
    # 2. Transform the text
    claim_vec = vectorizer.transform(claim_list)
    
    # 3. Get prediction and probabilities
    prediction = model.predict(claim_vec)[0]
    probabilities = model.predict_proba(claim_vec)[0]
    
    # 4. Format the output
    if prediction == 1:
        label = "Real (Evidence-based)"
        confidence = probabilities[1]
    else:
        label = "Fake (Misinformation)"
        confidence = probabilities[0]
        
    return {label: confidence}

# CREATE THE GRADIO INTERFACE

# Text box
input_textbox = gr.Textbox(
    lines=3, 
    placeholder="Enter a Remedy here...", 
    label="Medical Claim"
)

# Label with confidence bars
output_label = gr.Label(
    num_top_classes=2, 
    label="Prediction"
)

# Example inputs
examples = [
    "Vaccines are a safe and effective way to prevent infectious diseases.",
    "Drinking vitamin C will cure the common cold.",
    "Washing hands with soap and water reduces the spread of germs.",
    "Drinking herbal tea will reverse heart disease.",
    "Eating garlic supports cardiovascular health.",
    "Drinking fennel tea may help reduce bloating."
]

# Interface
app = gr.Interface(
    fn=predict_claim_validity,  
    inputs=input_textbox,        # Input
    outputs=output_label,        # Output
    title="VERA - Verifying Remedies Assertions",
    description="To combat the proliferation of online health misinformation, I introduce VERA, a novel machine learning model designed to assess the evidential basis of unconventional home remedies.",
    examples=examples,
    theme="soft" 
)

# LAUNCH THE APP
if __name__ == "__main__":
    print("Launching...")
    app.launch()
