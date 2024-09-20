# Function-Summarization-and-Search-Mechanism-


This project provides tools to analyze, summarize, and search through a code repository, with a focus on improving function-level documentation and navigation. Using Natural Language Processing (NLP), we generate human-readable summaries for each function and create a search mechanism to quickly locate specific elements, such as function dependencies, data types, and more.

# Features

1.Function Summarization:

Automatically summarize each function in the code repository, including its purpose, functionality, and dependencies.
Leverages NLP to enhance the quality of the summaries by utilizing function names, docstrings, and code structure.
Generates and stores Abstract Syntax Trees (AST) for future code analysis.

2.NLP-Enhanced Summarization:

Uses a pre-trained NLP model (facebook/bart-large-cnn) to generate concise, human-readable summaries of functions.
Summaries include key information about the function's name, docstring, purpose, and structure.

3.Search Mechanism:

Allows users to search the repository for specific elements like function names, data types, or keywords.
Provides a text-based search that matches user queries to function summaries.
Locates function implementations and tracks dependencies between functions.

Installation
1. Clone the Repository
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```
2. Install NLP Dependencies
This project uses the transformers library for NLP tasks. You can install it using:

```bash
pip install transformers
```
# Usage

1. Analyze and Summarize Functions
To analyze and summarize functions in your Python code, run the following script, specifying the path to your Python file:

```bash
python parse_nlpmodel.py
```
This will generate a function_metadata_nlp.json file containing the summaries, code snippets, ASTs, and more.

NOTE:- Put your python file in the analyze_code function


2. Customize Summarization
You can modify the summarization process by tweaking the NLP model or summarization parameters. By default, the project uses the facebook/bart-large-cnn model, but you can change the model in the parse_nlpmodel.py file.

3. Sample Function Metadata Format
Here is an example of what the metadata stored in function_metadata_nlp.json looks like:
```
json
{
    "calculate_area": {
        "name": "calculate_area",
        "docstring": "This function calculates the area of a circle.",
        "called_functions": ["math.pi"],
        "code": "def calculate_area(radius):\n    import math\n    return math.pi * radius ** 2",
        "summary": "This function, `calculate_area`, computes the area of a circle using the formula `area = pi * radius^2`.",
        "ast": "<AST representation>"
    }
}
```
## How It Works

Function Summarization:
-The code first parses each Python file using Python’s ast (Abstract Syntax Tree) module.
-Each function is summarized based on its name, docstring, and internal structure.
-We use an NLP model to enhance the summaries, making them concise and easier to understand.

Search Mechanism:
-After functions are summarized, a search mechanism is available to locate functions based on keywords or specific data types.
-The search matches the user query against the generated summaries, making it easy to navigate complex codebases.

Dependencies
-Python 3.x
-transformers library (for NLP)
-ast module (built-in)
