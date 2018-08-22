# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Parker")
define a = Character("Alex")
define l = Character("Lazule")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show parker happy

    # These display lines of dialogue.

    p "What are ya fuckin' gay?"

    a "Dude we're all gay."

    l "Yea. Pretty much"

    p "That's kinda gay."

    p "so uh, what do you faggots wanna do today?"

    a "I don't know? Do what we normally do and just exist?"

    l "Eh, anyway, theres the demo! See y'all fuckers later."

    # This ends the game.

    return
