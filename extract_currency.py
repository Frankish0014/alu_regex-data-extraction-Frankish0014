import re

def extract_currency(text):
    pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        content = file.read()
    print("Currency Amounts:", extract_currency(content))