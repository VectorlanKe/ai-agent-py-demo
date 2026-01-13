from pydantic_ai.mcp import MCPServerStdio
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.agent import Agent
from pydantic_ai.providers.ollama import OllamaProvider
from dotenv import load_dotenv

import fileTools


def main():
    load_dotenv()
    server = MCPServerStdio(
        'python', args=['mcpTools.py'], timeout=10
    )
    ollama_model = OpenAIChatModel(model_name='qwen3:8b',
                                   provider=OllamaProvider(base_url='http://192.168.40.21:11434/v1'))
    agent = Agent(ollama_model, instructions='简洁答复,一句话回答',
                  tools=[fileTools.read_file, fileTools.list_files,fileTools.rename_file],toolsets=[server])
    # result = agent.run_sync('“hello world”这个词是从哪里来的呢？')
    history = []
    while True:
        user_input = input("请输入问题：")
        result = agent.run_sync(user_input, message_history=history)
        history = list(result.all_messages())
        print(result.output)


if __name__ == '__main__':
    main()
