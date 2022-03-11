import random

# welcome user
name = input("What is your name? ")
print("Hello, " + name, "let's play Hangman!")
print("You have to correctly guess a word by entering letters.")
print("Try not to get hanged though, since you've got a limited amount of chances.")
print("Good luck " + name,"!")

# optional words
words = ["informatica", "informatiekunde", "spelletje", "aardigheidje", "scholier", "fotografie", "waardebepaling", "specialiteit", "verzekering", "universiteit", 'heesterperk']

# hangman graphics that will be displayed
hangman_graphics = ['__\n |\n',
                   '__\n |\n O',
                   '__\n |\n O\n/|',
                   '__\n |\n O\n/|\ ',
                   '__\n |\n O\n/|\ \n/ \ '
                   ]

# legenda
number_mistakes = 0
letters_guessed = []
number_mistakes_allowed = len(hangman_graphics)
word = random.choice(words)
letters_word = list(word)
wrong_letters = []

# number of letters in the word
print()
print('The word has {} letters'.format(len(letters_word)))

# main loop
while True:
  while number_mistakes < number_mistakes_allowed:
    print()
    print('Wrong letters: ', end= '')
    for letter in wrong_letters:
      print("{}, ".format(letter), end= '')
    print()
    # less guesses because user entered a wrong character
    print('Guesses left: {}'.format(number_mistakes_allowed - number_mistakes))
    guess = input('Enter a letter: ')
    while guess in letters_guessed or guess in wrong_letters:
      print()
      # multiple entered letters
      print('You have already entered this letter, try again')
      guess = input('Enter a letter: ')
    if len(guess) != 1 or not guess.isalpha():
      print()
      print("Invalid input. Try a letter of the alphabet")

    # number of mistakes made
    if guess not in letters_word:
      max_number_mistakes = 5
      number_mistakes += 1
      wrong_letters.append(guess)

    # printing the word in the game
    print()
    print('Word: ', end='')

    # showing correctly guessed letters in the word
    for letter in letters_word:
      if guess == letter:
        letters_guessed.append(guess)

    for letter in letters_word:
      if letter in letters_guessed:
        print(letter + ' ', end='')
      # showing incorrectly guessed letters as dashes
      else:
        print('_ ', end='')

    # printing the hangman graphics with every mistake made
    print()
    if number_mistakes:
      print(hangman_graphics[number_mistakes - 1])
    print()
    # organizing the game, so it eyes uncluttered
    print('.............................................')

  # able to keep entering letters if you haven't made the maximum amount of mistakes
  if number_mistakes <= number_mistakes_allowed:
    guess = input('Enter a letter = ')

  # end of the game -> win or loose
  if number_mistakes == number_mistakes_allowed:
    print()
    print("__\n |\n* *\n/|\ \n/ \ ")
    print("You have been hanged :(")
    print("The correct word is:", word)
  if guess == word:
    print()
    print("Congratulations, you won!")

  # re-executing game when first round ends
  endgame = input("Do you want to play again? Enter y if yes, n if no").lower()
  if endgame == y:
    print()
    print("Let's play Hangman again!")
  continue
