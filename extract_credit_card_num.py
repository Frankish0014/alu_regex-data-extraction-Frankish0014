import re

def extract_credit_cards(text):
    pattern = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        content = file.read()
    print("Credit Card Numbers:", extract_credit_cards(content))