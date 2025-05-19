import re

def extract_hashtags(text):
    pattern = r'#\w+'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        hastags = file.read()
    print("Hashtags:", extract_hashtags(hastags))