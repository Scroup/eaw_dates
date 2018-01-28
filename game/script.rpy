# The script of the game goes in this file.
image school_entrance = "school_entrance.jpg"
image classroom_bg = "class.jpg"
image gymdressingroom = "gymdress1.png"
image canteen = "school_canteen.jpg"
# CHARS ##
image Psody serious = "Psody_serious.png"
image Scroup_application = "scroup_application.png"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define psody = Character("Psody", color="#f76141",what_outlines=[ (2, "#e76e6e") ])
define you = Character("[player_name]", color="ffffff",what_outlines=[ (2, "#9296a3") ])
define scroup = Character("Scroup", color="f0314c",what_outlines=[ (2, "#e76e98") ])

# The game starts here.
label start:
    stop music
    $ renpy.movie_cutscene("images/splash.webm")
    stop music
    play music "thrilling_set.wav" fadein 1.0
    scene bedroom_night with fade
    narrator "You lived a very boring and poor life."
    narrator "Ponies and anime were the only things that mattered to you. And also that game, called Hearts of Iron 4."
    narrator "Looking at your life now, is there substance to it? Thinking about all this now... Nuisance, Isn't it?"
    narrator "But..."
    narrator "Here your dreams will come {color=#B13415}true{/color}."
    "......."
    narrator "No, don't thank me for that."
    narrator "Anyway, what's your name?"
# Input for name
    $ player_name = renpy.input("What's my name?")
    if player_name  == " ":
        $ player_name="Nerd"
    if player_name  == "":
        $ player_name="Memelord"
    $ player_name = player_name.strip()
# TEST
    if player_name  == "Memelord":
        narrator "[player_name]? Seriously? Could you be more original?"
    elif player_name  == "Cyrus":
        narrator "[player_name]. Oh, [player_name], I was waiting for you, my croatian boy."
    elif player_name  == "Scroup":
        narrator "Scroupy, ayy lmao, do you want there to be two of you?"
    elif player_name  == "Flake":
        narrator "Flock, right?"
    elif player_name  == "Yard":
        narrator "Flock, right?"
    else:
        narrator "[player_name]? What kind of name is that?"
    you "......!"
    narrator "Who am I? That doesn't matter."
    narrator "Time's up! Let me just start this meme."
    hide text with dissolve
    with Pause(1)
    stop music

    scene bedroom_day with fade
    play music "At_Long_Last.mp3"
    you "What kind of nightmare was that?"
    you "Well."
    you "It doesn't matter, I should go."

    stop music
    play music "snowfall_in_eqs.mp3" fadein 2.0
    scene school_entrance with fade
    you "Two days ago I transferred to a new high school."
    you "It turned out that there were a lot of clubs, that studied HoI4 modding!"
    you "I decided to join Equestria at War club, because I am really into ponies!"
    you "Oh I'm so excited!"
    you "However, I haven't met any of the club members yet. I haven't even attended their class yet."
    you "Well..."
    you "It's still morning."
    you "And the classes haven't started yet."
    you "I need to make a good impression."
    you "Where should I go first today?"

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
          jump clubalt1
    label psodyisnothappy:
          psody "What is this tone of yours?"
          you "REEEEEE"
          psody "You take that back!"
          scene black with dissolve
          hide Psody serious
          narrator "He hits you in the head. You passed out on the cold, wet floor."
          hide text with dissolve
          with Pause(1)
          scene gymdressingroom with dissolve
          you "Ough that hurts"
          you "Why did I even tried to mess with this swoll, nice guy?"
          you "Welp, that's not the first time for me to make poor decision."
          you "Oh, he's gone now. I'll better keep going too."

          return
    # This ends the game.
label clubalt1:
    show classroom_bg with fade
    narrator "blank"
    show Psody serious at center
    psody "There we go. Scroup! We have a fresh meat!"
    you "..."
    psody "What? I'm just pulling your leg, sweetie."
    scroup "Wha? Yes, I'm comming..."
    show Psody serious at left with move
    show Scroup_application at right with moveinright
    scroup "Oh"
    scroup "Psody, what is this?"
    psody "A new guy."
    you "Is something wrong?"
    scroup "REEE GET OUT NORMIE"
    narrator "Oh boy that's it"
    return
label dining_room:
                show canteen with fade
                you "It's not time to eat really."
                you "But I could wait here until the classes start."
                return
return
