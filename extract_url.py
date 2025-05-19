import re

def extract_urls(text):
    pattern = r'https?://[^\s"]+'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        content = file.read()
    print("URLs:", extract_urls(content))