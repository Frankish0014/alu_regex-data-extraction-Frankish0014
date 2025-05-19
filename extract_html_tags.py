import re

def extract_html_tags(text):
    pattern = r'<[^>]+>'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        content = file.read()
    print("HTML Tags:", extract_html_tags(content))