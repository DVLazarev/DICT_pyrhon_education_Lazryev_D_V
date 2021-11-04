import random
print("HANGMAN")

wordlist =['css', 'javascript', 'java', 'python', 'html', 'php']
secret = random.choice(wordlist)
guesses = ''
turns = 5

while turns > 0:
     missed = 0
     for letter in secret:
         if letter in guesses:
             print (letter,end=' ')
         else:
           print ('_',end=' ')
           missed= missed + 1

     print
     letter = []
     wrong_letter = []



     def de_sh():
         for letter1 in secret:
             if letter1 in letter:
                 print(letter1, end='')
             else:
                 print('_', end='')
                 if letter1 in letter:
                     print("You've already guessed this letter.")
                     if letter1 in wrong_letter:
                         print("You've already guessed this letter.")


     def playing():
         life = 8
         while life > 0:
             print('')
             letter1 = input("Input a letter: ")
             if len(letter1) == 0 or len(letter1) > 1:
                 print('You should input a single letter')
                 print('')
                 de_sh()
                 continue
             if letter1.capitalize() == letter1:
                 print('Please enter a lowercase English letter')
                 print('')
                 de_sh()
                 continue

     if missed == 0:
         print ('\nYou win!')
         break

     guess = input('\nguess a letter: ')
     guesses += guess

     if guess not in secret:
         turns = turns -1
         print ('\nThat letter doesnt appear in the word')
         print ('\n',turns, 'more turns')
         if turns < 5: print ('\n  |  ')
         if turns < 4: print ('  O  ')
         if turns < 3: print (' /|\ ')
         if turns < 2: print ('  |  ')
         if turns < 1: print (' / \ ')
         if turns == 0:
             print ('\n\nThe answer is', secret)


