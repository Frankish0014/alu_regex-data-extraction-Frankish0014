import re

def extract_times(text):
    pattern = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        content = file.read()
    print("Times:", extract_times(content))