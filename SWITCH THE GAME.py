#All variables are pre-determined in code, so that print() function does not get any errors in reading variables and types.

#Simply input variable name/variable you are told to enter into console to instantly show dialogue/strValue of said variable.


CONTINUE = "(Enter d1 and then d2 then so on to progress between dialogue)."
GAMEPARTS = """(Enter any of these variable names to get to said variable dialogues, miniscreens, and etc.
All variables present are sorted into their place in the source code.)
/DIALOGUE/
CONTINUE
d1
d2
d3
d4
d5
W1
W2
W3
W4
A1
D1
RW1
(Thia option is WIP; more dialogue variables will be added here soon.)"""

d1 = "You find yourself in a blank green room with no doors. "
d2 = "The only thing present is a switch. turn it on? (enter y1 for yes, and enter n1 for no.)"
n1 = "You decide not to open the switch. (Now enter d2.)"
y1 = "You have now opened the switch."
d3 = "An exit to the green room has opened, and you enter a white room with yellow stripes."
d4 = "There are 2 switches. The first one has a green tile on top of it"
d5 = "The second one has a red tile on top of it. Which switch will you turn on? (enter y2 to turn on the first one, and n2 to turn on the second one.)"
n2 = "You open the second switch. An exit has opened. (You are now entering a different route in gameplay, you must now enter r1d6, r1d7 and so on.)"
r1d6 = "The exit closes and you are now trapped in what you thought was an exit to that white room with yellow stripes."
y2 = "You open the first one. an exit appears. (The next dialogue text is a checkpoint, enter c1 to enter.)"

#After entering a checkpoint, go back to dialouges using the d keyword. But for now, enter ms1, then W1.
c1 = """You now see a corridor with two ways: left and right. (Press W1, W2, and so on for moving forward, you know the drill. But A and D actually rotate you, A rotates you to the left,
and D rotates you to the right. You are depicted as the 8 character.)"""

#Paths you can go to are represented as hashtags (#).
ms1 = "(Please enter W1, or S1, or A1, or D1, and so on, then show mini-screen by entering d7, so on, then repeat."
W1 = "Moved forward."
ms2 = """00000
####0
00800
00#00
00000"""
W2 = "Moved forward."
ms3 = """00000
##8#0
00#00
00#00
00000"""
D1 = "Turned right. (Just go forward.) (This is a different route in gameplay. enter RW1 to move forward, so on, Rms1 to show miniscreen, and so on."
RW1 = "Moved forward."
Rms1 = """00000
###80
00#00
00#00
00000|(Just go back to ms3)"""
A1 = "Turned left. (Just go forward)" 
W2 = "Moved forward."
ms4 = """00000
#8##0
00#00
00#00
00000"""
W4 = """You find a door then you open it. You find yourself in a blue room with 3 exits in the other 3 directions.
However all of the doors are locked. (Enter d6 to continue.)"""


#============================================================================================================================================================================================================================================================#
r1d7 = "You see a note taped to the wall that says 'bruh'."
r1d8 = "yea bro such a bruh moment"
r1d9 = "ENDING 1: STOOPID (Credits roll at the next dialogues)"
r1d10 = "CREATOR: QUITE LITERALLY A 10 YEAR OLD KID"
r1d11 = "PUBLISHER: EVERYTHING WAS CREATED BY THE 10 YEAR OLD KID"

#CONTINUE variable is technically the first dialogue text.
r1d11 = "THANKS FOR PLAYING! ENTER CONTINUE TO RESTART."


print('Welcome to SWITCH. This is a demo game that I have made. Future updates will improve this game.')
print('Please enter print(CONTINUE) in the console to start,')

#print(GAMEPARTS) is an option for the alpha mainly used to skip between parts of gameplay; it's sole use is to locate and help me fix errors in certain parts of gameplay.
print('And please enter print(GAMEPARTS) to progresss between game events, dialogue starts, checkpoints, and endings.')
print('Have fun!')
