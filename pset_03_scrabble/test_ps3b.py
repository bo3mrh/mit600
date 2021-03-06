from ps3a import *
import time
from perm import *
import itertools
import operator

#
#
# Problem #6: Computer chooses a word
#
#
def sortWordList(dict):
    keys = []
    keys = dict.keys()
    return keys.sort()

def comp_choose_word(hand, word_list):
    """
    Given a hand and a word_dict, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all possible 
    permutations of lengths 1 to HAND_SIZE.

    If all possible permutations are not in word_list, return None.

    hand: dictionary (string -> int)
    word_list: list (string)
    returns: string or None
    """
    #find word score for word_list store in dictionary
    dictWordList = {}
    for word in word_list:
        dictWordList[word] = get_word_score(word,handsize)

    sortedWordList = sorted(dictWordList.iteritems(), key=operator.itemgetter(1))
    
    # Create an empty list to store all possible permutations of length 1 to HAND_SIZE
    possiblePerm = []
    allLetters = ''

    # List of letters
    for letter in hand.keys():
        for j in range(hand[letter]): 
            allLetters += letter
    
    # For all lengths from 1 to HAND_SIZE (including! HAND_SIZE):
    for i in range(1,handsize):
        
        # Get the permutations of this length
        tempList = list(itertools.permutations(allLetters, i))

        # Add each permutation to possiblePerm list as a joined string
        for j in range(len(tempList)):
            possiblePerm.append(''.join(tempList[j]))
        
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    
    # Create a new variable to store the best word seen so far (initially None)  
    wordScore = None

    # For each possible word permutation:
    for word in possiblePerm:
        
        # If the permutation is in the word list:
        if word in word_list:
            
            # Get the word's score
            wordScore = get_word_score(word, handsize)
            
            # If the word's score is larger than the maximum score seen so far:
            if wordScore > maxScore:
                maxScore = wordScore
                
                # Save the current score and the current word as the best found so far
                bestWord = word

    print bestWord, maxScore
     
    if maxScore == 0:
        return None
    else:
        return bestWord
    

#
# Problem #7: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
    Allows the computer to play the given hand, following the same procedure
    as play_hand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. comp_choose_word returns None).
 
    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
#
# Problem #8: Playing a game
#
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using play_hand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using comp_play_hand.

    4) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "play_game not yet implemented." # <-- Remove this when you code this function

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    hand = deal_hand(handsize)
    comp_choose_word(hand, word_list)
