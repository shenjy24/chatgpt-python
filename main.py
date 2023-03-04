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
    openai.api_key = ""
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": content}])
    message = completion.choices[0].message.content
    print(message)


def chat():
    openai.api_key = ''

    with open('chat.txt', 'a', encoding="utf-8") as f:
        while True:
            # 获取用户输入
            user_input = input("You: ")

            # 将用户输入写入文件
            f.write("You: " + user_input + "\n")

            # 判断用户是否输入 "exit"，如果是则退出聊天
            if user_input == "exit":
                break

            completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                      messages=[{"role": "user", "content": user_input}])
            message = completion.choices[0].message.content

            # 输出回复到命令行
            print(message)

            # 将回复写入文件
            f.write("Bot: " + message + "\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(num_tokens_from_string("tiktoken is great!", "gpt2"))
    print(chatgpt("pip常用指令"))
    # print(chatgpt("pip常用指令"))
    chat()
