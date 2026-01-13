from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.agent import Agent
from pydantic_ai.providers.ollama import OllamaProvider
from dotenv import load_dotenv

import tools


def main():
    load_dotenv()
    ollama_model = OpenAIChatModel()
    # result = agent.run_sync('“hello world”这个词是从哪里来的呢？')
    history = []
    while True:
        user_input = input("请输入问题：")

if __name__ == '__main__':
    main()
