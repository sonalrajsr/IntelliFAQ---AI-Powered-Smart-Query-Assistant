import markdown
import os

def render_markdown(file_path):
    """
    Reads a markdown file and returns its HTML representation.
    """
    if not os.path.exists(file_path):
        return "File not found"
    
    with open(file_path, 'r') as md_file:
        content = md_file.read()
        html_content = markdown.markdown(content)
        return html_content
