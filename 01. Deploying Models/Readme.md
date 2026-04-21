# 01. Deploying Models

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

<br/><br/>

---

<br/>

<a href="https://aiops.ru/">Предложить инженеру работу / подработку на проекте с kubernetes, microservices, machine learning, big data, golang</a>
