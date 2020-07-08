import streamlit as st
from utils import load_model, generate, wrap_text
import time
import json
from model_list import *

# model, tokenizer = load_model()
@st.cache(allow_output_mutation=True)
def loader(model_name):
    return load_model(model_name)


def main():
    st.title("Easy Text Generator")
    st.write("Use text generation models with just a few clicks")
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

    model_list = list(model_dict.keys())

    model_selectbox = st.sidebar.selectbox("Model", model_list)
    model_select = model_dict[model_selectbox]
    context = st.sidebar.text_area("Starting text")
    if st.sidebar.button("Generate"):
        model, tokenizer = loader(model_select)
        start_time = time.time()
        if context:
            sample = generate(model,tokenizer,input_text=context,max_length=max_length)
        else: 
            sample = generate(model,tokenizer,max_length=max_length)
        # Show done with balloons
        st.balloons()
            
        end_time = time.time()

        print(end_time-start_time)
    else:
        sample = ['']

    # Fix up line wrapping
    # max_length = 80
    # split_text = sample[0].split('\n')
    # for line in split_text:
        # if len(line) > max_length:
            # import textwrap
            # text_lines = textwrap.wrap(sample[0], width=80)
            # sample[0] = '\n'.join(text_lines)
            # break
    sample[0] = wrap_text(sample[0], length=80)
    st.text(sample[0])
    
    
main()
