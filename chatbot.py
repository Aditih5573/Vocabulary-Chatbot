import os
import requests
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# OpenAI API Key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Vocabulary API (free example API)
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/{}"

# Define tool to fetch vocabulary word
@tool
def get_vocabulary_word(word: str) -> str:
    """Fetches a vocabulary word's definition and example from an API."""
    try:
        url = API_URL.format(word)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        example = data[0]["meanings"][0]["definitions"][0].get("example", "No example available")

        return f"Word: {word}\nDefinition: {meaning}\nExample: {example}"
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    # Create LLM
    llm = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")

    # Create agent with tool
    agent = create_react_agent(llm, tools=[get_vocabulary_word])

    # Conversation loop
    print("🤖 Vocabulary Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("🤖 Bot: Goodbye! Keep learning new words! 📚")
            break

        # Send user input to chatbot
        response = agent.invoke({"messages": [HumanMessage(content=user_input)]})
        print(f"🤖 Bot: {response['messages'][-1].content}")

if __name__ == "__main__":
    main()
