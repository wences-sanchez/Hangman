import random

print('H A N G M A N')

secret_words = ['python', 'java', 'kotlin', 'javascript']
secret_chosen_word = random.choice(secret_words)
typed_word = input('Guess the word:')

if typed_word == secret_chosen_word:
    print('You survived!')
else:
    print('You lost!')
