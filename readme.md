# Semantic Question Generation and Ranking Tool

This project demonstrates a semantic search and ranking technique using Cohere's `rerank` model and Groq's platform for generating insightful, contextually relevant questions based on a user-provided topic. The project is designed to analyze a topic and generate high-quality, thought-provoking questions, then rank them based on relevance.


## Project Overview

The project generates questions based on a user-provided topic and ranks them using semantic search techniques with Cohere's `rerank` model. It leverages:
- **Groq's platform** to create questions.
- **Cohere's rerank model** to rank generated questions based on relevance and insight.

### Key Features
- Generates insightful questions encouraging critical thinking on a topic.
- Ranks the questions to provide the most relevant ones.
- Demonstrates the use of semantic search and ranking techniques.


## Prerequisites
- Python 3.x
- Access to Groq API (API key required)
- Access to Cohere API (API key required)


## Installation

### 1. Clone the repository
```bash
git clone https://github.com/SamnangGit/semantic-search.git
cd semantic-search
```

### 2. Create a Virtual Environment

#### For macOS/Linux:
```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate   # For bash/zsh
# OR
source venv/bin/activate.fish   # For fish shell
# OR
source venv/bin/activate.csh    # For csh/tcsh
```

#### For Windows:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# In Command Prompt:
venv\Scripts\activate.bat
# OR in PowerShell:
venv\Scripts\Activate.ps1
```

### 3. Install required dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root with:
```
GROQ_API_KEY=your_groq_api_key_here
COHERE_API_KEY=your_cohere_api_key_here
```

### Notes:
- To deactivate the virtual environment when you're done, simply run:
  ```bash
  deactivate
  ```
- Make sure you always activate the virtual environment before running the project
- If you see permission errors on Windows PowerShell, you might need to run:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```


## Function Explanations

Below is an explanation of each function in the project and what it does.

### 1. `make_request(prompt, model)`

**Purpose**: Sends a request to Groq's language model to generate questions based on the given prompt.

- **Parameters**:
  - `prompt`: The formatted prompt string containing the topic and guidelines for generating questions.
  - `model`: The specific Groq model used for generating questions (e.g., `'llama-3.1-8b-instant'`).
  
- **Process**:
  - Initializes a connection with Groq using the API key.
  - Sends a chat completion request using the provided `prompt` and `model`.
  - Extracts and returns the generated content (questions).

**Returns**: A string containing the generated questions based on the input topic.

---

### 2. `rerank_response(user_prompt, doc)`

**Purpose**: Uses Cohere's `rerank` model to rank the generated questions based on relevance to the user's topic.

- **Parameters**:
  - `user_prompt`: The original topic prompt provided by the user.
  - `doc`: A list of generated questions to be ranked.
  
- **Process**:
  - Initializes a Cohere client using the API key.
  - Calls the `rerank` function on the `doc` list, using the `user_prompt` as the query.
  - Retrieves the top-ranked questions based on Cohere's `rerank` model.

**Returns**: A ranked list of questions, with the most relevant questions appearing first.

---

### 3. `main()`

**Purpose**: Orchestrates the process of generating and ranking questions using different models.

- **Process**:
  - Loops over each model in the `models` list.
  - Calls `make_request()` with the `prompt` and current model to generate questions.
  - Appends each model's response to the `responses` list.
  - Calls `rerank_response()` to rank the questions in `responses` based on relevance.
  - Prints the ranked response.

**Note**: The main function serves as the entry point of the script.

---

### 4. `if __name__ == "__main__": main()`

**Purpose**: Ensures the `main()` function runs only if the script is executed directly.

- **Process**: Checks if the script is being run directly (not imported as a module). If true, it calls `main()` to start the program.

---

