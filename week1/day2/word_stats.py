try:
    with open("README.md") as f:
        text = f.read()

    print(text)

    lines = text.splitlines()
    words = text.split()

    print(f"Number of lines: {len(lines)}")
    print(f"Number of words: {len(words)}")

    if words:
        avg_len = sum(len(w) for w in words) / len(words)
        print(f"Average word length: {avg_len:.2f} characters")

    unique_words = set(words)
    print(f"Number of unique words: {len(unique_words)}")
except FileNotFoundError:
    print("Couldn't find README.md - is it in this folder?") 