# chess-game

# Mind dump

MVC?

#### Model: 
Chess board

- Position of the Figures and marked Fields
    2 dimensional Array
    with dictionary - figure, marked_by_white, marked_by_black


- Whos turn is it?
    Boolean -> Black/White

- Currently in check 
    Boolean -> Yes/No


Future:
- Timer for each player
    2 timers ->

- List of figures that where taken (and calculate )
    list of figures 


#### View:
Some frontend I'm probably never gonna finish

- tba

#### Controller:
Game logic

1. Check if any legal moves are left for player
    if no and in check -> loose
    if no and not in check -> draw
    if yes -> 2. 

2. take input of piece to move 
    if not valid -> "wrong piece try again"
    if valid -> 3. 

3. show all legal moves for that piece (fun *1)
    if no valid moves -> "no moves" -> 2. 
    if valid move available -> 4.      

4. get input of move
    if illegal move enter -> "illegal move" -> 2. 
    if legal move enter -> 5. 

5. move piece to new position (fun #2) 
    -> 1. 




Functions:

*1 Show legal move for that piece (postition, type of piece, board)
    For all:    - in borders
                - not in same colored pieces
                - no checks afterwards
    
    Pawn:       - Forward 2 - if in og row -> set en_peasent = true
                - Forward 1 - if no pieces in front
                - DiagonallyLeft/Right 1 - if otherpieces there

*2 Possbible actions moved piece (position, type of piece, board)
    - remove piece from board
    - set check king to true
    - rochade 


*3 Possible moves
    *3.01 Forward(color, max_steps)
    *3.02 Backwards(color, max_steps)
    *3.03 Left(color, max_steps)
    *3.04 Right(color, max_steps)
    *3.05 DiagonallyForward(color, max_steps)
    *3.06 DiagonallyBackwards(color, max_steps)
    *3.07 DiagonallyLeft(color, max_steps)
    *3.08 DiagonallyRight(color, max_steps)
    Knight:
    *3.09 K_RightForward(color)
    *3.10 K_RightBackwards(color)
    *3.11 K_LeftBackwards(color)
    *3.12 K_LeftForward(color)

  
  







