import random

print("HANGMAN-The game will be available soon.")
qwe1 = ["python", "java", "javascript", "php", "html", "css"]
qwe2 = random.choice(qwe1)
qwe0 = input("Guess the word:")
if qwe0 == qwe2:
    print("You survived!")
else:
    print("You lost!")





