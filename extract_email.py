import re

def extract_emails(text):
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    return re.findall(pattern, text)

if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        emails = file.read()
    print("Emails:", extract_emails(emails))
