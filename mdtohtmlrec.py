import os
import argparse
import markdown2

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as markdown_file:
        markdown_content = markdown_file.read()
        converter = markdown2.Markdown(extras=["tables"])  # <-- here
        html_content = converter.convert(markdown_content)
    
    with open(output_file, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

def convert_folder_of_markdowns(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Walk through the directory and convert each Markdown file to HTML
    for root, _, files in os.walk(input_folder):
        for file in files:
            input_file_path = os.path.join(root, file)
            output_file_path = os.path.join(output_folder, os.path.relpath(input_file_path, input_folder)).replace(".md", ".html")
            
            # Ensure the output folder structure exists
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

            # Check if it's a Markdown file
            if file.lower().endswith('.md'):
                convert_markdown_to_html(input_file_path, output_file_path)
                print(f"Converted {file} to {os.path.splitext(file)[0]}.html")

## Reading commandline args and calling the main conversion script         
# Create ArgumentParser object
parser = argparse.ArgumentParser(description='Markdown to HTML Conversion Utility')

# Add input_folder and output_folder as command-line arguments
parser.add_argument('--input_folder', required=True, help='Path to the input folder containing Markdown files')
parser.add_argument('--output_folder', required=True, help='Path to the output folder for HTML files')

# Parse the command-line arguments
args = parser.parse_args()

# Access the arguments
input_folder = args.input_folder
output_folder = args.output_folder

# Print the values
print('Input Folder:', input_folder)
print('Output Folder:', output_folder)

convert_folder_of_markdowns(input_folder, output_folder)