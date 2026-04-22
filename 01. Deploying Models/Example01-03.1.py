import os
import torch
import gc
from vllm import LLM, SamplingParams

# 1. Пропускаем прогрев для стабильности на 4ГБ
os.environ["VLLM_SKIP_WARMUP"] = "1"

llm = LLM(
    model="Qwen/Qwen2.5-0.5B-Instruct-AWQ",
    max_model_len=2048,
    gpu_memory_utilization=0.5,   # Снизил до 0.5, чтобы системе дышалось легче
    enforce_eager=True,
    trust_remote_code=True
)

sampling_params = SamplingParams(max_tokens=50)
results = llm.generate("LLMs are great for", sampling_params)

for result in results:
    # Исправлено: доступ к тексту первого варианта ответа
    print(f"\nResult: {result.outputs[0].text}")

# 2. Правильное завершение работы
del llm
gc.collect()
torch.cuda.empty_cache()
