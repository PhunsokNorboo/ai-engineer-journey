def greet(name: str) -> str:
    return f"Hi, {name}!"

age: int = 26
scores: list[float] = [0.9, 0.7, 0.85]

print(greet("Phunsok"))

name = "Phunsok"
count = 3
print(f"{name} has {count} repos")
print(f"Pi is roughly {3.14159:.2f}")

nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
evens = [n for n in nums if n % 2 == 0]
lenghts = {word: len(word) for word in ["rag", "agent", "embedding"]}

print(squares)
print(evens)
print(lenghts)

from dataclasses import dataclass

@dataclass
class Document:
    title: str
    content: str
    score: float = 0.0

doc = Document(title="Intro to RAG", content="some text", score=0.87)
print(doc.title)
print(doc.score)

try:
    result = 10/0
except ZeroDivisionError as e: 
    print(f"Caught it; {e}")
finally:
    print("This runs no matter what")
