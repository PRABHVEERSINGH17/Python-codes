a = "Harry is good boy\nhe is not a bad boy"
print(a)
print("Hello\nWorld")
print("Column1\tColumn2")
print("She said: \"Python is fun!\"")
path = r"C:\Users\Name\Documents"
print(path)
print("\z")   # prints \z (with a warning)
print("Python\\nWorld\nPython\\tRocks")
s1 = "C:\newfolder\test.txt"
s2 = r"C:\newfolder\test.txt"
print(s1)
print(s2)
print("\u0041 \U00000042 \x43")
name = "Alex"
print(f"Hello\n{name}\tWelcome")
print("\q \z")
import re
pattern = "\\n"
text = "Hello\nWorld"
print(re.search(pattern, text))
print("Hello\rWorld")
