
import simpleguitk as simplegui

canvas_height=400
canvas_width =400
game_height  =320
game_width   =320
player_mark  ="0"
game_area    =[[" "," "," "],[" "," "," "],[" "," "," "]]
block_width  = (game_height-80) // 3
game_on      = True
last_player  =""

#winning logic
def won_or_not():

    for i in range(0,3):
        if game_area[i][0] != " ":
            if game_area[i][0]==game_area[i][1]==game_area[i][2]: #if all same in a row
                return True

    for j in range(0,3):
        if game_area[0][j] != " ":
            if game_area[0][j]==game_area[1][j]==game_area[2][j]: #if all same in a column
                return True

    if game_area[0][2] == game_area[1][1] == game_area[2][0] and game_area[0][2] != " ": #if all same in right diagonal
        return True

    elif game_area[0][0] == game_area[1][1] == game_area[2][2] and game_area[0][0] != " ": #if all same in left diagonal
        return True

    else:
        return False

def click_area(pos):
    global game_on,last_player
    if game_on==True:   #if game_on is true
        if pos[0] <= 320 and pos[0] >= 80 and pos[1] <= 320 and pos[1]>=80: #adjustments to make it fit for this game_area.
            if pos[0] % block_width != 0 and pos[1] % block_width != 0:     #Note:-see if the click was on line or not
                row = (pos[1]-80) // block_width                            #values between 0,1,2
                column = (pos[0]-80) // block_width         				#values between 0,1,2
                if game_area[row][column] == " ": 							#to check empty space or not
                    game_area[row][column] = player_mark                    #set player_mark if space is empty
                    if not won_or_not():                                    #if game not finish,continue.
                        next_turn()
                    else:
                        last_player = player_mark                           #if game is finished, stop and displet winner
                        game_on=False

#Event handlers

def draw(canvas):

    canvas.draw_line([80,160],[game_width,160],2.7,"white")
    canvas.draw_line([80,240],[game_width,240],2.7,"white")
    canvas.draw_line([160,80],[160,game_height],2.7,"white")
    canvas.draw_line([240,80],[240,game_height],2.7,"white")
    canvas.draw_text("Player '"+str(player_mark)+"' turn",[5,360],20,"lawngreen")  #print players mark
    canvas.draw_text("TIC TAC TOE",[102,35],32,"Gold","sans-serif")
    canvas.draw_text("Winner :'"+str(last_player)+"'",[290,360],20,"lawngreen")

    for row in range(0,3):                   #using nested loop to print the player_mark
        for column in range(0,3):
            canvas.draw_text(game_area[row][column],[column * block_width + 80 + 20 , row * block_width + 80 + 60 ],50,"gold") #extra 80 is added to adjust according to this game_area

def next_turn():
    global player_mark

    if player_mark=="0":
        player_mark="X"

    else:
        player_mark="0"


def restart():
    global game_area, player_mark, game_on, last_player
    game_area = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    player_mark = "0"
    game_on = True
    last_player=""

#adding key function
def keydown(key):
    if key == simplegui.KEY_MAP["space"]:
        restart()


# Frame

frame = simplegui.create_frame("Tic-Tac-Toe", canvas_width, canvas_height)

# Register Event Handlers

frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click_area)
info = frame.add_label("Press SPACE to restart or click below")
frame.add_button("RESTART", restart)
frame.set_keydown_handler(keydown)


# Start
frame.start()
