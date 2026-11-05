paragraph = """Python is a programming language.
This Python course teaches basic programming concepts.
Students can learn Python easily through this course."""

print("Length:", len(paragraph))

print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

print("Preview:", paragraph[:50])

print(paragraph.replace("Python", "PYTHON"))

paragraph = paragraph.lower()
print(paragraph)

paragraph = paragraph.strip()
print(paragraph)

words = paragraph.split()
print(words)

if "course" in paragraph:
    print("The word 'course' is found.")

message = "The course description is {} characters long and has {} words.".format(len(paragraph), len(words))

print(message)