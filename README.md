# Markdown to Html

Markdown, with its simplicity and readability, has become a popular choice for content creation. However, in the web environment, HTML remains a dominant format. This utility bridges this gap, offering a seamless way to transform Markdown files into HTML, recursively navigating through directories.

## The Utility in Action
This utility, let's call it "MDtoHTMLRec," goes beyond a simple one-to-one conversion. Its recursive nature allows it to delve into subdirectories, converting Markdown files within each folder. This proves invaluable when dealing with projects organized into a hierarchy of directories.

### Features and Benefits
1. Recursive Operation
Traverse through the entire directory structure, ensuring no Markdown file is left untouched.
2. Customizable Configuration
Tailor the utility to your specific needs with customizable configuration options.
Define output paths, HTML templates, and styling preferences.
3. Error Handling
Robust error handling ensures smooth execution even when encountering unexpected situations.
Detailed logs provide insights into the conversion process.
4. Python & markdown2 flavor
This utility is built on top of python using `markdown2` library. This markdown flavor is pretty configurable.

Installation and Usage
To get started with MDtoHTMLRec, follow these simple steps:

## Installation:

bash

```
git clone <>
pip install markdown2
```

### How to Run

```
mdtohtmlrec --input_folder /path/to/markdown_folder --output_folder /path/to/html_output
```


## Advanced Configuration:

Explore additional options such as templates, styles, and parallel processing for more advanced usage.

## Conclusion
In the world of web development, the journey from Markdown to HTML should be smooth and efficient. The MDtoHTMLRec utility streamlines this process, offering a recursive approach that aligns with the organization of modern projects. Enhance your workflow, save time, and ensure consistency in your web content by adopting this versatile utility.

Thank you. Happy coding! 🚀✨


