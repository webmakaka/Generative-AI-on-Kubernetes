import transformers
import torch
import os

# 1
model_id = "meta-llama/Llama-3.2-1B-Instruct"

# 2
pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    device_map="auto",
    torch_dtype=torch.bfloat16, # 3
    token=os.environ.get("HF_TOKEN") # 4
)

messages = [
    {"role": "user", "content": "Hey how are you doing today?"}
]

result = pipeline(messages, max_new_tokens=256)
# 5
print(result[0]["generated_text"][-1]["content"])