import transformers

model_id = "Qwen/Qwen2.5-0.5B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    device_map="auto",
    torch_dtype="auto",
)

messages = [
    {"role": "user", "content": "Write a short poem about Kubernetes."}
]

result = pipeline(messages, max_new_tokens=128)
print(result[0]["generated_text"][-1]["content"])
