📚 **Vocabulary Chatbot**

A simple **interactive chatbot** that helps you learn new English vocabulary words using **OpenAI models** (via LangChain) and a free **dictionary API**.  
The chatbot can define words, provide example usages, and chat with you in natural language.

🚀 **Features**

- Built with **LangChain**, **LangGraph**, and **OpenAI GPT models**  
- Fetches real definitions and examples from [Free Dictionary API](https://dictionaryapi.dev/)  
- Command-line chatbot experience  
- Easy to set up with `.env` for API keys  
- Fully reproducible environment with **uv**

🛠 **Requirements**

- Python **3.12+**
- [uv](https://docs.astral.sh/uv/) package manager

⚙️ **Installation & Setup**

   1. Clone the repository: 
       ```bash
       git clone https://github.com/Adithih5573/Vocabulary-Chatbot.git
       cd project1

  2. Install dependencies with uv:
      ```bash
      uv snyc
      ```
      
      This will create a .venv folder and install exact versions from uv.lock.

  3. Activate the virtual environment:
       ```bash
       source .venv/bin/activate     # macOS/Linux
      .venv\Scripts\activate        # Windows

  4. Set up your environment file:
`      Create a .env file in the project root with:
     ```bash
     OPENAI_API_KEY=your_api_key_here

▶️ **Usage**

Run the chatbot from your terminal:
```bash
python chatbot.py
```

  Example interaction:

```bash
🤖 Vocabulary Chatbot (type 'exit' to quit)

You: Define ubiquitous
🤖 Bot: Word: ubiquitous
Definition: Present, appearing, or found everywhere
Example: His ubiquitous influence was felt by all the family.
```
To exit, type:
```bash
You: exit
🤖 Bot: Goodbye! Keep learning new words! 📚
```

📂 **Project Structure**
```
project1/
├── chatbot.py        # Main chatbot program
├── .env              # Stores your OpenAI API key
├── pyproject.toml    # Project metadata and declared dependencies
├── uv.lock           # Locked dependency versions for reproducibility
└── README.md         # Project documentation
```



