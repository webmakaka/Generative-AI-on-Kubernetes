from fastapi import FastAPI
from pydantic import BaseModel
import transformers

app = FastAPI()

class InputText(BaseModel):
    text: str

class OutputText(BaseModel):
    text: str

def get_pipeline():
    model_id = "Qwen/Qwen2.5-0.5B-Instruct"
    return transformers.pipeline(
        "text-generation",
        model=model_id,
        device_map="auto"
    )

pipeline = get_pipeline()

@app.post("/generate", response_model=OutputText)
async def generate_func(prompt: InputText):
    output = pipeline(prompt.text)
    return {"text": output[0]["generated_text"]}
