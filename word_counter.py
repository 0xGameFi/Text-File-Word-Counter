# word_counter.py

def word_count(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            return len(text.split())
    except FileNotFoundError:
        return "File not found."

# Sample usage
file_name = input("Enter the filename: ")
print(f"Word count: {word_count(file_name)}")
