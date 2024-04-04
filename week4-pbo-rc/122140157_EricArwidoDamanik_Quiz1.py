# Eric Arwido Damanik
# 122140157
# RC - Kuis 1

import random

class HangmanDraw:
    stage = ["""
            ------
            |    |
            |
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |
            |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   /
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |    |
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|
            |    |
            |   / \\
            |
        ------------
        """, """
            ------
            |    |
            |    O
            |  --|--
            |    |
            |   / \\
            |
        ------------
        """]
    
    @staticmethod
    def draw_stage_hangman(stage):
        # Menggambar stage hangman
        print(HangmanDraw.stage[stage])
        
class HangmanGame:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(self.words)
        self.sisa_tebakan = 6
        self.tebakan_benar = set()
        self.tebakan_salah = set()
        self.word_display = ['_' for _ in self.word]

    def show_word_display(self):
        # Menampilkan word yang sudah di tebak
        return ' '.join(self.word_display)
    
    def guess_word_display(self, letter):
        # Memproses tebakan
        if letter in self.word:
            self.tebakan_benar.add(letter)
            for idx, char in enumerate(self.word):
                if char == letter:
                    self.word_display[idx] = letter
            print("Correct")
        else:
            self.tebakan_salah.add(letter)
            self.sisa_tebakan -= 1
            print(f"Incorrect, You have {self.sisa_tebakan} attempts left")
    
    def end_game(self):
        #Memeriksa apakah game sudah berakhir atau belum
        return self.sisa_tebakan <= 0 or '_' not in self.word_display
    
    def win(self):
        #Memeriksa apakah pemain menang
        return '_' not in self.word_display
    
    def play(self):
        print("Welcome to Hangman Game!")
        while not self.end_game():
            print("The word is :", self.show_word_display())
            HangmanDraw.draw_stage_hangman(6 - self.sisa_tebakan)
            tebakan = input("Guess a letter: ").lower()
            self.guess_word_display(tebakan)

        if self.win():
            print("Congratulations! You Win. You have gueessed the word:", self.word)
        else:
            print("Game over! You Lose. The word is :", self.word)

words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

game = HangmanGame(words)
game.play()
