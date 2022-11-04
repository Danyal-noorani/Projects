from itertools import repeat
from random_word import RandomWords

wrong = 0
# Generating a word
r = RandomWords()
word = r.get_random_word()
# Creating Blanks
lst = []
lst.extend(repeat("_", len(word)))
used_let = ["a","e","i","o","u"]




def mans(wrongs):
    if wrongs == 6:
        man_Full = """
        __________
        |        |
        |        -
        |      |   |
        |        -
        |    ____|____
        |        |
        |        |
        |       / \\
        |      /   \\
        |    
        _
        """
        print(man_Full)

    elif wrongs == 5:
        man_leg1 = """
        __________
        |        |
        |        -
        |      |   |
        |        -
        |    ____|____
        |        |
        |        |
        |       / 
        |      /   
        |    
        _
        """
        print(man_leg1)
    elif wrongs == 4:
        man_hand2 = """
        __________
        |        |
        |        -
        |      |   |
        |        -
        |    ____|____
        |        |
        |        |
        |       
        |      
        |    
        _
        """
        print(man_hand2)
    elif wrongs == 3:
        man_hand1 = """
        __________
        |        |
        |        -
        |      |   |
        |        -
        |    ____|
        |        |
        |        |
        |       
        |      
        |    
        _
        """
        print(man_hand1)
    elif wrongs == 2:

        man_torso = """
        __________
        |        |
        |        -
        |      |   |
        |        -
        |        |
        |        |
        |        |
        |       
        |      
        |    
        _
        """
        print(man_torso)
    elif wrongs == 1:

        man_head = """
        __________
        |        |
        |        -
        |      |   |
        |        -
        |    
        |        
        |        
        |       
        |      
        |    
        _
        """
        print(man_head)

    elif wrongs == 0:
        man_empty = """
        __________
        |        |
        |        
        |      
        |        
        |    
        |        
        |        
        |       
        |      
        |    
        _
        """
        print(man_empty)

def vowel_check():
    index = 0
    for i in word:
        if "a" == i:
            lst[index] = "a"
        index += 1
    index = 0
    for i in word:
        if "e" == i:
            lst[index] = "e"
        index += 1
    index = 0
    for i in word:
        if "i" == i:
            lst[index] = "i"
        index += 1
    index = 0
    for i in word:
        if "o" == i:
            lst[index] = "o"
        index += 1
    index = 0
    for i in word:
        if "u" == i:
            lst[index] = "u"
        index += 1



while wrong<6:
    #Logic
    vowel_check()
    print("".join(lst))  # print out
    print("Used letters: "+",".join(used_let))
    letter = input('Enter Letter: ')
    used_let.append(letter)
    letter = letter.lower()
    index = 0
    isin = False

    for i in word:
        if letter == i:
            lst[index] = letter
            isin =True
        index += 1
    if isin == False:
        wrong+=1        #If wrong

    mans(wrong)
    if not "_" in lst:
        print("You Got it!!!") #when user gets the word
        break
    if wrong == 6:
        print("Game Over")
        print("The word was",word)
