# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "C:\\Users\\Michel\\OneDrive\\Bureau\\MIT1\\exo_mit\\projet 1\\words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    s=True
    i=0
    secret_word1 =list(secret_word)
    while i<len(secret_word1) and s==True:
      if secret_word1[i] in letters_guessed:
        i+=1
      else:
        s = False
    return s
    

    # FILL IN YOUR CODE HERE AND DELETE "pass"


def get_guessed_word(secret_word, letters_guessed):
    secret_word2 = list(secret_word)
    i=0
    resultat = []
    while i < len(secret_word2):
      if secret_word2[i] in letters_guessed:
        resultat.append(secret_word2[i])
      else:
          resultat.append("_ ")
      i += 1
    resultat1 =''.join(resultat)
    return resultat1 
    
'''   
secret_word= 'pomme'  
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's'] 
print(get_guessed_word(secret_word, letters_guessed))
'''
def get_available_letters(letters_guessed):
  string1=[string.ascii_lowercase]
  for i in range(len(letters_guessed)):
    if letters_guessed[i] in string1:
      string3=string1.replace(string1[i],"") 
      string2=''.join(string3)    
  return string2
    
    
def hangman(secret_word):
    guesses_left = 6
    letters_guessed = []
    
    print("Bienvenue dans le jeu du Pendu !")
    print("Je pense à un mot qui contient", len(secret_word), "lettres.")
    
    while True:
        print("-------------")
        print("Il te reste", guesses_left, "essais.")
        available_letters = get_available_letters(letters_guessed)
        print("Lettres disponibles :", available_letters)
        
        guess = input("Devine une lettre :").lower()
        
        if guess in secret_word:
            letters_guessed.append(guess)
            print("Bonne devinette !")
        else:
            guesses_left -= 1
            print("Mauvaise devinette...")
        
        word_guessed = get_guessed_word(secret_word, letters_guessed)
        print("Mot deviné :", word_guessed)
        
        if is_word_guessed(secret_word, letters_guessed):
            print("Félicitations, tu as deviné le mot !")
            break
        
        if guesses_left == 0:
            print("Désolé, tu as épuisé tous tes essais. Le mot était", secret_word)
            break



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
  
    if len(my_word) != len(other_word):
        return False
    
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
            return False
        if my_word[i] == "_" and other_word[i] in my_word:
            return False
    
    return True



def show_possible_matches(my_word):
  
        matches = []
        for word in wordlist:
            if match_with_gaps(my_word, word):
                matches.append(word)
        if len(matches) == 0:
            print("Aucun mot possible trouvé.")
        else:
            print("Mots possibles:")
            for match in matches:
                print(match)




def hangman_with_hints(secret_word):
    
    # Initialise le nombre de tentatives restantes
    guesses_remaining = 6
    # Liste pour stocker les lettres devinées
    letters_guessed = []
    while guesses_remaining > 0:
        # Affiche le mot avec des lettres non devinées remplacées par des _
        display_word = get_guessed_word(secret_word, letters_guessed)
        print("Mot actuel:", display_word)
        print("Tentatives restantes:", guesses_remaining)
        letter = input("Devinez une lettre: ")
        if letter == "*":
            show_possible_matches(display_word)
        elif letter in letters_guessed:
            print("Vous avez déjà deviné cette lettre. Veuillez réessayer.")
        else:
            letters_guessed.append(letter)
            if letter in secret_word:
                print("Bonne devinette!")
                if is_word_guessed(secret_word, letters_guessed):
                    print("Félicitations! Vous avez deviné le mot correctement:", secret_word)
                    return
            else:
                print("Mauvaise devinette!")
                guesses_remaining -= 1
    print("Game Over. Vous avez épuisé toutes vos tentatives. Le mot était:", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

