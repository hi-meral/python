
class TicTacToe:

    def __init__(self):
        self.cells =  {1 : ' ', 2: ' ', 3 : ' ',
                4 : ' ',  5 : ' ' , 6 : ' ',
                7 : ' ', 8 : ' ', 9 : ' '}

        self.choices = list(self.cells.keys())

        self.player = 'X'

    def getBoard(self):

        cntr = 0;
        for i in range(1,4):
            j = i+cntr
            m = j+3
            
            while j < m:
                print(self.cells[j],end=" | ")
                j += 1
            
            print(end="\n")

            cntr += 2

    def takeTurn(self):

        place = int(input(f'Where do you want to place {self.player} from {self.choices} ? : '))

        if(place not in self.choices):
            print('Wrong Place')
        else:
            
            self.cells[place] = self.player
            self.getBoard()

            if(self.wonGame()):
                return False

            self.choices.remove(place)
            
            self.switchPlayer()

        return True

    def switchPlayer(self):
        if(self.player == 'X'):
            self.player = '0'
        else:
            self.player = 'X'

    def wonGame(self):

        if(self.cells[1] == self.cells[4] == self.cells[7] and self.cells[1]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[2] == self.cells[5] == self.cells[8] and self.cells[2]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[3] == self.cells[6] == self.cells[9] and self.cells[3]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[1] == self.cells[2] == self.cells[3] and self.cells[1]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[4] == self.cells[5] == self.cells[6] and self.cells[4]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[7] == self.cells[8] == self.cells[9] and self.cells[7]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[1] == self.cells[5] == self.cells[9] and self.cells[1]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(self.cells[3] == self.cells[5] == self.cells[7] and self.cells[3]!=" "):
            print(f'Player {self.player} won the game!')
            return True
        elif(all(v != ' ' for v in self.cells.values())):
            print("Its a tie!!!")
            return True

        return False

ttt = TicTacToe()

ttt.getBoard()

final = True
while final != False:
    final = ttt.takeTurn()
else:
    print("Game Over!!!")
            


