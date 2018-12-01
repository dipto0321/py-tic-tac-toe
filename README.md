# TIC-TAC-TOE

This is a tic-tac-toe terminal based game develop in python

### Screencast

---

![Python Tic Tac Toe](tictactoe_20181128_215323.gif)

[Demo video](https://www.youtube.com/watch?v=WXxYzQ2ZHbg)

# Code Plane

1.  1-d Array contains all input
2.  array legends will be [1 2 3 4 5 6 7 8 9]
3.  showing formates

```
    1 | 2 | 3

    4 | 5 | 6

    7 | 8 | 9
```

4.  There will be 2 player I mean Human vs Human (Human vs Computer will be updated version)
5.  Ask for players choice maybe 1st letter of their name or anything they choose. Default will be "o" and "x"

```
 formate will be something like that
 "Insert Player 1 name (default = "Player 1")" // Optional
 "Insert Player 1 char (default = "o")" //Optional
 "Insert Player 2 name (default = "Player 2")" // Optional
 "Insert Player 2 char (default = "x")" //Optional
 should be check that both input must be uniqe
```

6.  Maybe also show an msg about game start (and || or) ask for input cell number from 1-9 [check validation]
7.  after input show the table with input
    example : suppose player 1 input is 5 then it will be show that board

```

                1 | 2 | 3
                ---------
                4 | x | 6
                ---------
                7 | 8 | 9

```

> just need to be replace with legends same for player 2 suppose input is 1

```
    o | 2 | 3

    4 | x | 6

    7 | 8 | 9
```

8.  Game continue untile anyone won or draw
9.  After ending the game it show the game status like who won? and [how many steps he played for won (Optional)] or if draw then just end the game
10. Maybe without ending we should ask users "wanna play again?" if no then quit app

# Visualization

```

                                      Tic-Tac-Toe
                                  =====================
                                      created date
                                    -----------------
                                          Authors

===========================================================================================
Insert Player 1 name (default = "Player 1") John
Insert Player 1 char (default = "o") x
Insert Player 2 name (default = "Player 2") Jenny
Insert Player 2 char (default = "x")" o

Best of luck John[x] and Jenny[0]

1 | 2 | 3

4 | 5 | 6

7 | 8 | 9

John insert cell number between 1 to 9 : 5

1 | 2 | 3

4 | x | 6

7 | 8 | 9

Jenny insert cell number between 1 to 9 : 1

o | 2 | 3

4 | x | 6

7 | 8 | 9

John insert cell number between 1 to 9 : 1
SORRY! Already have. Please choose another one
John insert cell number between 1 to 9 : 2

o | x | 3

4 | x | 6

7 | 8 | 9

Jenny insert cell number between 1 to 9 : 8

o | x | 3

4 | x | 6

7 | o | 9

.
.
.

o | x | o

x | x | o

x | o | o

Game status : Match Draw!
x | x | o

x | x | o

x | o | x

Game status : John win!

Wanna play again? no
Thanks for playing!

```

---

# Algorithm [Plain Text]

1.  One game class where we put all the methods initialize with players name and char
2.  Class variables player1_name, player2_name, player1_char, player2_char, player1_cell, player2_cell, init
3.  Methods start_game, draw_board, cell_choose, game_state_check,update_array,end_game
    start_game

    - Show wish string
    - create 1-d array with 1-9 legends when init is true
    - call draw_board
    - call cell_choose

    > draw_board

    > creating board from 1-d array in below format

    ```
    1 | 2 | 3

    4 | x | 6

    7 | 8 | 9
    ```


    > cell_choose

    1. ask p1 inputs
    2. assigns all of inputs in class variable
    3. update array
    4. draw_board
    5. ask p2 inputs
    6. assigns all of inputs in class variable
    7. update array
    8. draw_board
