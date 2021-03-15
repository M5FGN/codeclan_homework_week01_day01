guess = input('Make your guess: ')
word = 'secret'

while guess != word:
    print('Unfortunately, You Guessed Wrongly')
    guess = input('Make a new guess: ')
else:
    print('Well Done - You Guessed Correctly')