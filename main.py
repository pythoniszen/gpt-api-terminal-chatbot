import openai

openai.api_key = "your-api-key"

# Predefined messages that set the persona or context
persona = [
    {"role": "system", "content": "You are a helpful and knowledgeable assistant."},
    {"role": "assistant", "content": "Hello! I'm here to help you. Feel free to ask me anything."}
]

def chat(prompt, chat_history=[]):
    # Combine the predefined persona with the chat history and current prompt
    messages = persona + chat_history + [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    # Append the latest response to the chat history
    chat_history.append({"role": "assistant", "content": response.choices[0].message.content.strip()})

    return response.choices[0].message.content.strip(), chat_history

if __name__ == "__main__":
    chat_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        
        response, chat_history = chat(user_input, chat_history)
        print("Bot:", response)
