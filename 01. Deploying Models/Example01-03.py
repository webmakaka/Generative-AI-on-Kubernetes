from vllm import LLM, SamplingParams

llm = LLM(
    model="Qwen/Qwen2.5-0.5B-Instruct-AWQ",
    max_model_len=2048,           # Критично: уменьшить с 32к до 2к
    gpu_memory_utilization=0.6,   # Оставить 40% видеопамяти системе
    enforce_eager=True,           # Отключить CUDA-графы (экономит ~1ГБ VRAM)
    trust_remote_code=True
)

sampling_params = SamplingParams(max_tokens=50)
results = llm.generate("LLMs are great for", sampling_params)

for result in results:
    print(f"\Result: {result.outputs[0].text}")
