with open("README.md") as f:
    text = f.read()

print(text)

lines = text.splitlines()
words = text.split()

print(f"Number of lines: {len(lines)}")
print(f"Number of words: {len(words)}")

unique_words = set(words)
print(f"Number of unqiue words {len(unique_words)}")

try:
    with open("README.md") as f:
        text = f.read()

    print(text)

    lines = text.splitlines()
    words = text.split()

    print(f"Number of lines: {len(lines)}")
    print(f"Number of words: {len(words)}")

    unique_words = set(words)
    print(f"Number of unqiue words {len(unique_words)}")
except FileNotFoundError:
    print("Couldn't find README.md - is it in this folder?") 