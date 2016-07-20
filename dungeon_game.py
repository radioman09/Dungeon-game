import random

print("Welcome to the dungeon!")
print("Enter QUIT to quit")

CELLS = [(0,0),(0,1),(0,2),
         (1,0),(1,1),(1,2),
         (2,0),(2,1),(2,2)]

def get_locations():
    # monster = random location
    monster = random.choice(CELLS)
    # door = random location
    door = random.choice(CELLS)
    #start = random location
    start = random.choice(CELLS)
    #if monster, start ,door are the same do it again
    if monster == start == door:
        get_locations()

    #retrun monster, door, start
    return monster, door, start

def move_player(player, move): 
    #get player's current location
    x,y = player
    # if move is LEFT y-1
    if move == "LEFT":
        y -=1
    # if move is RIGHT y+1
    elif move == "RIGHT":
        y+=1
    # if move is UP x-1
    elif move == "UP":
        x-=1
    # if move is DOWN x+1
    elif move == "DOWN":
        x+=1
    return x,y

def get_moves(player):
    moves = ['LEFT','RIGHT','UP','DOWN']
    #player = (x,y)
    
    #if players y = 0, remove left
    if player[1] == 0:
        moves.remove('LEFT')
    #if players x = 0 remove up
    if player[0] == 0:
        moves.remove('UP')
    #if players y = 2 remove right
    if player[1] == 2:
        moves.remove('RIGHT')
    #if players x = 2 remove down
    if player[0] == 2:
        moves.remove('DOWN')
    return moves

def draw_map(player):
    print(' _ _ _')
    tile = '|{}'

    for idx, cell in enumerate(CELLS):
        if idx in [0,1,3,4,6,7]:
            if cell == player:
                print(tile.format('X'), end = '')
            else:
                print(tile.format('_'), end = '')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))

monster, door, player = get_locations()


while True:
    moves = get_moves(player)
    
    print("You are curently in room{}".format(player))# fill in with player position
    draw_map(player)
    print("You can move {}".format(moves)) #fill with available moves
    

    move = input("> ")
    move = move.upper()
    if move == "QUIT" or move == "Q" or move == "EXIT":
        break
          
    #if its a good move, change the players position
    if move in moves:
          player = move_player(player,move)
    else:
          print("Walls are hard, stop walking into them")
          continue
    if player == door:
          print("you escaped!")
          break
    elif player == monster:
          print("game over, you lose!")
          break
    #if its a bad move, don't change anything.
    #if the new player position is the door, they win
    #if the new player position is the montser they lose
    #otherwise continue














