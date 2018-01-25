# The script of the game goes in this file.
image school_entrance = "school_entrance.jpg"
image classroom_bg = "class.jpg"
image gymdressingroom = "gymdress1.png"

# CHARS ##
image Psody serious = "Psody_serious.png"
image Scroup_application = "scroup_application.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define psody = Character("Psody", color="#f76141")
define you = Character("You", color="ffffff")
define scroup = Character("Scroup", color="f0314c")

# The game starts here.

label start:
    play music "mainmenu.mp3" fadein 2.0
    scene school_entrance with fade
    you "Two days ago, I've been transferred to a Hearts of Iron IV modder high school."
    you "It turned out that there were a lot of clubs!"
    you "I decided to join Equestria at War club, because I am really into ponies!"
    you "Oh I'm so excited!"
    you "However, I haven't met any of the club members yet. I haven't even attended their class yet."
    you "Well..."
    you "It's still morning."
    you "And the classes haven't started yet."
    you "I need to make a good impression."
    you "Where should I go first?"

    menu: 
          "Gym":
                jump gym
          "Class":
                jump classroom1
          "Dining Room":
                jump dining_room
          "Club Room":
                jump club1

label classroom1:
                show classroom_bg with fade
                you "Oh, I'm first."
                you "I guess, I'm stressing myself too much about this."

                
                return

label club1:
                show classroom_bg with fade
                you "Hello?"
                you "Is anyone there?"
                scroup "Hey..."
                "..."
                show Scroup_application at right with moveinright
                scroup "Oh, you're the new guy..."
                scroup "You forgot to fill in your application..."
                show Scroup_application at center with move

                scroup "Here..."
                you "Okie-dokie"
                hide Scroup_application with dissolve
                you "Well, that's one sad girl"
                menu: 
                     "Gym":
                           jump gym
                     "Class":
                           jump classroom1
                     "Dining Room":
                           jump dining_room
                     "Main Menu":
                               return

label gym:
    stop music fadeout 3.0
    play music "background_gym.mp3" fadein 3.0
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene gymdressingroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    you "Is anyone here?"
    you "Nobody, apparently. Good"
    show Psody serious with dissolve
    psody "Hello there."
    you "Oh god!"

    # These display lines of dialogue.

    psody "Oh. Haven't seen you before. So, you're that rookie everyone talks about? Name's Psody, nice to meet you."

    menu: 
          "H-hey":
                jump psodyishappy
          "You talking to me, bouncer?":
                jump psodyisnothappy
    label psodyishappy:
          psody "You're cute, want to meet me tomorrow?"
          psody "I can get you comfortable in the club."
          you "S-sure!"
          return
    label psodyisnothappy:
          psody "What is this tone of yours?"
          you "REEEEEE"
          psody "You take that back!"
          return
    # This ends the game.

    return
