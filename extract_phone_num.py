import re

def extract_phones(nums):
    regex_pattern = r'(?:\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})'
    return re.findall(regex_pattern, nums)


if __name__ == "__main__":
    with open('test_input.txt', 'r') as file:
        phone_number = file.read()
    print("Phone Numbers:", extract_phones(phone_number))