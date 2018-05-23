# SS10 hangman ----------------
import random

def hangman(word):
    wrong = 0
    stages = [
        '',
        '_____     ',
        '|         ',
        '|    |    ',
        '|    o    ',
        '|   /|\   ',
        '|   / \   ',
        '|         '
    ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('hangman started.')
    
    while wrong < len(stages) - 1:
        print('\n')
        msg = 'predict a character: '
        char = input(msg)
        if char in rletters:
            c_index = rletters.index(char)
            board[c_index] = char
            rletters[c_index] = '$'
        else:
            wrong += 1
        
        print(' '.join(board))
        
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        
        if '_' not in board:
            print('you won.')
            print(' '.join(board))
            win = True
            break
    
    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('you lost. the answer is {0}'.format(word))

Word = ['Ham', 'Ion', 'Good']
Num = random.randint(0,2)
hangman(Word[Num])