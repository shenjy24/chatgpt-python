import openai
# import tiktoken


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def chatgpt(content):
    """调用OpenAi的聊天接口"""
    openai.api_key = "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"
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
    message = completion.choices[0].message.content
    print(message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(num_tokens_from_string("tiktoken is great!", "gpt2"))
    print(chatgpt("pip常用指令"))
