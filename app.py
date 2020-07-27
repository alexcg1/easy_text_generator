import streamlit as st
from utils import load_model, generate, wrap_text, models
# import time
import json

st.title("Easy Text Generator")
st.write("Use text generation models with just a few clicks")

model_names = []
for model_dict in models:
    for key, value in model_dict.items():
        model_names.append(key)

if "model_select" in locals():
    st.header(model_select)

st.sidebar.title("Options")

# Setup sidebar
max_length = st.sidebar.slider(
    """ Max Text Length 
    (Longer length, slower generation)""",
    50,
    1000
)

model_selectbox = st.sidebar.selectbox("Model", model_names)

for item in models:
    for key, value in item.items():
        if key == model_selectbox:
            model_data = value

model_select = model_data["path"]

context = st.sidebar.text_area("Starting text")
if st.sidebar.button("Generate"):
    model, tokenizer = load_model(model_dir=model_select)

    if context:
        sample = generate(model,tokenizer,input_text=context,max_length=max_length)
    else: 
        sample = generate(model,tokenizer,max_length=max_length)
    st.balloons()

else:
    sample = ['']

# Fix up line wrapping
sample[0] = wrap_text(sample[0], length=80)
st.text(sample[0])
