# GPT-based Chatbot

## Introduction
This project is a simple chatbot powered by OpenAI's GPT models. It provides an interface for users to interact with a conversational AI agent locally. The chatbot leverages OpenAI's advanced language models to understand and respond to user queries.

## Features
- Interactive chat interface.
- Powered by OpenAI's GPT-3.5 (or specify your model).
- Easy to use and integrate.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.6 or higher.
- Access to OpenAI's API (API key required).

## Setup
To set up the chatbot on your local machine, follow these steps:

1. **Clone the Repository:**
Run: git clone https://github.com/pythoniszen/gpt-api-chatbot.git


2. **Install Dependencies:**
Run: "pip install openai==0.28" to be able to use the code as it is
written based on an older version of the openai api code. Newer versions
require different syntax than what is used in this program.

3. **API Key Configuration:**
Place your open ai api key generated from openai in the main.py file. The
key should be placed in line 3 in between the "" where it says "your-api-key".

## Usage
To start the chatbot, run: python3 chatbot.py while in the project directory.
Follow the on-screen prompts to interact with the chatbot.

## Customization
You can customize the chatbot by modifying the `chatbot.py` file. Adjust parameters like `model`, `temperature`, and `max_tokens` as per your requirements.

## Contributing
Contributions to this project are welcome! Please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the [MIT License](LICENSE).

## Disclaimer
This project is not officially associated with OpenAI. It uses OpenAI's API for demonstration purposes. Be sure to comply with OpenAI's use case policies when using their API.

## Contact
For any queries or assistance, feel free to open an issue in the repository or contact at pythoniszen@gmail.com.
