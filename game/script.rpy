# The script of the game goes in this file.

image gymdressingroom = "gymdress1.png"
image Psody serious = "Psody_serious.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define psody = Character("Psody")
define you = Character("You")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene gymdressingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Psody serious

    # These display lines of dialogue.

    psody "Oh. Haven't seen you before. So, you're that rookie everyone talks about? Name's Psody, nice to meet you."

    menu: 
          "H-hey":
                jump psodyishappy
          "You talking to me, bouncer?":
                jump psodyisnothappy
    label psodyishappy:
          psody "You're cute, want to meet me tomorrow?"
          you "S-sure!"
          return
    label psodyisnothappy:
          psody "What is this tone of yours?"
          you "REEEEEE"
          psody "You take that back!"
          return



    # This ends the game.

    return
