import ast
import json
import re
from transformers import pipeline


function_metadata = {}


summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class FunctionAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.current_function = None
    
    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.summarize_function(node)
        self.generic_visit(node)

    def summarize_function(self, node):
        docstring = ast.get_docstring(node) or "No docstring provided"
        
        
        called_functions = [n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)]

        
        function_body = ast.unparse(node)
        summary_text = self.generate_nlp_summary(node.name, docstring, function_body)
        
        summary = {
            'name': node.name,
            'docstring': docstring,
            'called_functions': called_functions,
            'code': function_body,
            'summary': summary_text,
            'ast': ast.dump(node)
        }
        
        function_metadata[node.name] = summary

    def generate_nlp_summary(self, func_name, docstring, code_body):
        clean_docstring = re.sub(r"\n\s*", " ", docstring)
        
        
        important_parts = f"Function name: {func_name}. Docstring: {clean_docstring}. Code: {code_body[:500]}..." 
        summary = summarizer(important_parts, max_length=100, min_length=30, do_sample=False)
        
        return summary[0]['summary_text']

    def save_metadata(self, filename):
        with open(filename, 'w') as f:
            json.dump(function_metadata, f, indent=4)


def analyze_code(file_path):
    with open(file_path, 'r') as f:
        code = f.read()
        tree = ast.parse(code)
        analyzer = FunctionAnalyzer()
        analyzer.visit(tree)
        analyzer.save_metadata('function_metadata_nlp.json')


analyze_code('your_python.py')

def search_by_keyword(keyword):
    results = []
    for func_name, metadata in function_metadata.items():
        if keyword.lower() in metadata['summary'].lower():
            results.append((func_name, metadata['summary']))
    return results

search_results = search_by_keyword('area')
for func, summary in search_results:
    print(f"Function: {func}\nSummary: {summary}\n")
