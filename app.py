from fastapi import FastAPI
from transformers import pipeline

## Create a new FASTAPI app instance
app=FastAPI()

# Initialize the text generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")

@app.get("/")
def home():
    return {"message": "Hello World"}


#define function to handle get request

@app.get("/generate")
def generate(text: str):
    ## use the pipeline to generate text from the given input
     output=pipe(text)

     return {"output":output[0]['generated_text']}



