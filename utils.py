from transformers import AutoTokenizer, AutoModelWithLMHead
import random
import os
import json
import yaml

models = []

with open("models.yml", "r") as stream:
    out = yaml.load(stream)
    model_list = out['Models']
    for model in model_list:
        models.append(model)


def load_model(model_dir=None):
    """Loads the saved model from disk if the directory exists.
    Otherwise it will download the model and tokenizer from hugging face.  
    Returns 
    a tuple consisting of `(model,tokenizer)`
    """    

    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelWithLMHead.from_pretrained(model_dir)
    return model, tokenizer


def generate(model, tokenizer, input_text=None, num_samples=1, max_length=1000, top_k=50, top_p=0.95):
    print(f"Top_k: {top_k}")
    print(f"Top_p: {top_p}")

    model.eval()
    
    if input_text:
        input_ids = tokenizer.encode(input_text, return_tensors='pt')
        output = model.generate(
            input_ids= input_ids,
            do_sample=True,   
            top_k=50, 
            max_length = max_length,
            top_p=0.95, 
            num_return_sequences= num_samples
        )
    else:
        output = model.generate(
            bos_token_id=random.randint(1,50000),
            do_sample=True,   
            top_k=50, 
            max_length = max_length,
            top_p=0.95, 
            num_return_sequences=num_samples

        )

    decoded_output = []
    for sample in output:
        decoded_output.append(tokenizer.decode(
            sample, skip_special_tokens=True))

    return decoded_output

def wrap_text(text, length=80):
    split_text = text.split('\n')
    for line in split_text:
        if len(line) > length:
            import textwrap
            text_lines = textwrap.wrap(text, width=length)
            text = '\n'.join(text_lines)
            break
            return text
    
    return text
