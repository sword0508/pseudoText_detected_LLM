import requests
import json


url = "http://192.168.200.11:9004/v1/chat/completions"
headers = {
    "Authorization": "#VideoTag",
    "Content-Type": "application/json"
}

data = {
    "model": "Qwen2-72B-int4",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好，请给我将一个故事。"}
    ],
    "temperature": 0.7 
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print("响应内容:", response.json())
else:
    print("请求失败，状态码:", response.status_code)




# from transformers import AutoTokenizer, AutoModelForCausalLM
# import torch

# # 加载模型和tokenizer
# model_name = 'gpt2'  # 或者其他适合的模型
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)
# model.eval()

# def compute_logprobs(text):
#     inputs = tokenizer(text, return_tensors='pt')
#     with torch.no_grad():
#         outputs = model(**inputs, labels=inputs['input_ids'])
#         log_probs = outputs.logits.log_softmax(dim=-1)
#         # 获取每个位置上实际token的logprob
#         token_logprobs = log_probs.gather(2, inputs['input_ids'].unsqueeze(-1)).squeeze(-1)
#         return token_logprobs

# # 示例文本
# text = "这是一个测试文本。"
# logprobs = compute_logprobs(text)
# print("Log probabilities:", logprobs)
