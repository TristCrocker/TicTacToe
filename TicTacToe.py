class Players:

    Name = ' '
    Symb = ' '

player1 = Players()
player2 = Players()
TicTacToe = {}
switch = {}
Choice = ' '
play = ' '
row = ' '
col = ' '
maxi = 11
count = 1
wincount1 = 0
wincount2 = 0
winnerhoriz = 3
winnervert = 3
winnerdiag = 3
player1.Symb = 'X'
player2.Symb = 'O'


TicTacToe = {'T': {'L' : ' ', 'M' : ' ', 'R' : ' '},
             'C': {'L' : ' ', 'M' : ' ', 'R' : ' '},
             'B': {'L' : ' ', 'M' : ' ', 'R' : ' '},

          }

def winnershoriz(wincount1, wincount2):

    for row in TicTacToe:

        wincount1 = 0
        wincount2 = 0
        for col in TicTacToe[row]:


            if TicTacToe[row][col] == 'X':

                wincount1 += 1


                if wincount1 == 3:
                    return 1

            if TicTacToe[row][col] == 'O':

                wincount2 += 1


                if wincount2 == 3:

                    return 2

def winnersvert(wincount1, wincount2, row):

    for col in TicTacToe[row]:

        wincount1 = 0
        wincount2 = 0
        for row in TicTacToe:


            if TicTacToe[row][col] == 'X':

                wincount1 += 1


                if wincount1 == 3:
                    return 1

            if TicTacToe[row][col] == 'O':

                wincount2 += 1


                if wincount2 == 3:

                    return 2

def winnersdiag(wincount1, wincount2):

    for row in TicTacToe:
        for col in TicTacToe[row]:

            if TicTacToe['C']['M'] == 'X':

                 if (TicTacToe['T']['L'] == 'X' and TicTacToe['B']['R'] == 'X') or (TicTacToe['T']['R'] == 'X' and TicTacToe['B']['L'] == 'X'):

                     wincount1 = 3

                     if wincount1 == 3:
                         return 1

            if TicTacToe['C']['M'] == 'O':

                if (TicTacToe['T']['L'] == 'O' and TicTacToe['B']['R'] == 'O') or (TicTacToe['T']['R'] == 'O' and TicTacToe['B']['L'] == 'O'):

                    wincount2 = 3

                    if wincount2 == 3:
                        return 2

while (Choice != 'Y') and (Choice != 'N'):

    Choice = input('Would you like to play? Type Y or N').upper()

    if Choice == 'Y':

        player1.Name = input('Please input player one''s name: ')
        player2.Name = input('Please input player two''s name: ')

        for i in range (2,maxi):

            count += 1



            play = (str(input('Where would you like to play?'))).upper()
            row = play[:1]
            col = play[1:]



            try:

                mod = count%2
                if mod == 0:

                    TicTacToe[row][col] = player1.Symb

                else:

                    TicTacToe[row][col] = player2.Symb

                print('    ', TicTacToe['T']['L'], '|', TicTacToe['T']['M'], '|', TicTacToe['T']['R'], '\n    ---+---+---\n',
                      '   ',  TicTacToe['C']['L'], '|', TicTacToe['C']['M'], '|', TicTacToe['C']['R'], '\n    ---+---+---\n',
                      '   ',  TicTacToe['B']['L'], '|', TicTacToe['B']['M'], '|', TicTacToe['B']['R'])

                winnerhoriz = winnershoriz(wincount1, wincount2)
                winnervert = winnersvert(wincount1, wincount2, row)
                winnerdiag = winnersdiag(wincount1, wincount2)

                if winnerhoriz == 1 or winnerhoriz == 2 or winnervert == 1 or winnervert == 2 or winnerdiag == 1 or winnerdiag == 2:
                    break

            except KeyError:


                print('Invalid Input, Try Again')
                count += 1
                maxi += 1







    if winnerhoriz == 1 or winnervert == 1 or winnerdiag == 1:

        print(player1.Name, ' Wins!!')
        exit()

    elif winnerhoriz == 2 or winnervert == 2 or winnerdiag == 2:

        print(player2.Name, ' Wins!!')
        exit()

    else:

        print('Draw!')
        exit()

