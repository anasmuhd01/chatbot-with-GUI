import openai

class ChatBot():
    def __init__(self):
        openai.api_key = "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"

    def get_respoce(self, user_input):
        responce = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return responce


if __name__ == "__main__":
    chatbot = ChatBot()
    respoce = chatbot.get_respoce("tell me about you")
    print(respoce)
