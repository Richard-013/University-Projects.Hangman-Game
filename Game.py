import random as rand

class Game():
    '''Holds setup functions and key gameplay data such as the word being guessed'''
    def __init__(self):
        self.word = self.wordSelect()
        self.wordLength = len(self.word)
        self.unguessedLetters = self.wordLength

    playerWins = False
    guessWrong = False
    
    def wordSelect(self):
        '''Selects a word from the wordList file and stores it to be used in the game'''

        #wordNum range starts from 1 to ensuure that the source URL in the wordList file is never selected as the word
        wordNum = rand.randint(1, 1000)
        wordList = open("wordList.txt", "r")

        for i in range(wordNum+1):
            if i == wordNum:
                word = wordList.readline()
                word = word[:-1]
            else:
                wordList.readline()

        wordList.close()
        return word

    def splitWord(self, word):
        wordListed = []
        for letter in word:
            wordListed.append(letter)

        return wordListed

    def beginGame(self):
        print("The word is " + str(self.wordLength) + " letters long")
        print(self.unguessedLetters*"_ ")

    def letterGuess():
        letterGuessed = input("What is your guess? ")

    def wordGuess():
        wordGuessed = input("What is your guess? ")
        if wordGuessed == runGame.word:
            playerWins = True
        else:
            guessDown = True

    def gameWon():
        pass
