# 01. Deploying Models

**NVIDIA GeForce GTX 1650**

<br/>

```shell
$ mkdir -p ~/projects/dev/ml/
$ cd ~/projects/dev/ml/
$ git clone https://github.com/webmakaka/Generative-AI-on-Kubernetes.git
$ cd Generative-AI-on-Kubernetes/
```

<br/>

```shell
$ pip install uv
$ uv venv --python=python3.12
$ source .venv/bin/activate
$ cd 01.\ Deploying\ Models/
$ uv pip install -r requirements.txt
```

<br/>

## “It Works on My Machine”

<br/>

### Example 01

<br/>

```shell
// OK!
$ python Example01-01.py
```

<br/>

**response:**

```
Kubernetes: A powerful framework,
A flexible, scalable solution to manage.
It's a container orchestration system,
That automates deployment and scaling.

With it, you can scale your apps as needed,
And ensure that they run smoothly.
From microservices to monolithic applications,
Kubernetes is the key to managing them all.

It scales across multiple clouds and data centers,
And makes sure that your infrastructure stays in sync.
With its automated rolling updates and auto-scaling,
Kubernetes is the future of cloud computing.

So let's embrace Kubernetes, and make our systems strong,
And secure our applications with this power.
For without it,
```

<br/>

### Example 02

```shell
uvicorn Example01-02:app --reload
```

<br/>

```shell
$ curl -X POST "http://localhost:8000/generate" \
     -H "Content-Type: application/json" \
     -d '{"text": "What is the capital of France?"}' | jq .
```

response:

```shell
{
  "text": "What is the capital of France? The capital of France is Paris. It is the largest city in Europe and one of the most populous cities in the world. The French government has its headquarters, as well as many important departments, in the heart of the city. \n\nParis is known for its beautiful architecture, rich history, and vibrant culture. It is also home to many famous landmarks such as Notre-Dame Cathedral, Eiffel Tower, Louvre Museum, and the Palace of Versailles.\n\nIn addition to these major attractions, Paris is a popular tourist destination, with millions of visitors each year. Its unique blend of old-world charm and modern amenities makes it an attractive place for people from all over the world to visit and explore."
}
```

<br/>

### vLLM

<br/>

```shell
$ uv pip install vllm==0.17.1
```

<br/>

```shell
wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda_12.1.0_530.30.02_linux.run

chmod +x cuda_12.1.0_530.30.02_linux.run
sudo ./cuda_12.1.0_530.30.02_linux.run --toolkit --silent --override

echo 'export PATH=/usr/local/cuda-12.1/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc

source ~/.bashrc


$ nvcc --version
nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2023 NVIDIA Corporation
Built on Tue_Feb__7_19:32:13_PST_2023
Cuda compilation tools, release 12.1, V12.1.66
Build cuda_12.1.r12.1/compiler.32415258_0
```

<br/>

```shell
// OK!
$ python Example01-03.1.py
```

```shell
// FAIL!
VLLM_USE_V1=0 VLLM_ATTENTION_BACKEND=TORCH_SDPA vllm serve Qwen/Qwen2.5-0.5B-Instruct-AWQ \
--port 8080 \
--max-model-len 2048 \
--gpu-memory-utilization 0.7 \
--enforce-eager
```

```shell
// Original
$ vllm serve \
--port=8080 \
--model=/mnt/models \
--served-model-name=meta-llama/Meta-Llama-3-8B
```

<br/>

```shell
// FAIL!
$ curl http://localhost:8080/v1/completions \
-H "Content-Type: application/json" \
-d '{
      "model": "meta-llama/Meta-Llama-3-8B",
      "prompt": "LLMs are great for",
      "max_tokens": 10,
      "temperature": 0
    }'
```

<br/>

### Hugging Face Text Generation Inference

<br/>

```shell
# start the server
$ text-generation-launcher \
--port 8080 \
--model-id /mnt/models

# invoke the model using TGI API
$ curl localhost:8080/generate_stream \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "inputs": "LLMs are great for",
  "parameters": {"max_new_tokens": 10}
}'

# invoke the model using OpenAI-compatible API
$ curl localhost:3000/v1/chat/completions \
-H 'Content-Type: application/json' \
-X POST \
-d '{
  "model": "tgi",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "LLMs are great for"}
  ],
  "max_tokens": 10
}'
```

<br/>

## Other Model Servers

### llama.cpp

<br/><br/>

---

<br/>

<a href="https://aiops.ru/">Предложить инженеру работу / подработку на проекте с kubernetes, microservices, machine learning, big data, golang</a>
