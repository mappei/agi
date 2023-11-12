import os
import openai

# 加载 .env 到环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务
openai.api_key = os.getenv('OPENAI_API_KEY') # 设置 OpenAI 的 key
openai.api_base = os.getenv('OPENAI_API_BASE') # 指定代理地址

'''
ChatCompletion仅支持0.28.1以及之前的版本

在此之后的代码中我们将使用最近的依赖包
'''
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "hi"
        }
    ],
)

# print(response['choices'][0]['message'].get("content"))
print(response)