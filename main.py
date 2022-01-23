#Step 1 
import random
import hangman_art
import hangman_word

word_list = hangman_word.word_list
print(hangman_art.logo)
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

chosen_word = word_list[random.randint(0,2)];
stages = hangman_art.stages


i = 7;

print(chosen_word)
wordArr = [];



for _word in chosen_word:
    wordArr.append('_')

while  '_'  in wordArr:
  guess = input('Please guess a letter.').lower();
  strArr = [i for i, ltr in enumerate(chosen_word) if ltr == guess]
  currentWord = wordArr
  selectI = 0
  if(guess in chosen_word):
    for _index in strArr:
      if(wordArr[_index] == '_'):
        wordArr[_index] = guess
        selectI = 1
        break;
  if (selectI == 0):
    i -= 1
    print(stages[i])
   
  if(i == 0):
    print("You Loose!")
    break;
  print(wordArr)

def _find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

if i != 0:
  print("You Win!")



