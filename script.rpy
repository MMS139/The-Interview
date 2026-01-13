# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define interviewer = Character("Interviewer")
init python:
    showered = 0
    teethbrushed = 0
    combed = 0
    changed = 0

image bg bedroom:
    zoom 2.0
    "bg bedroom.jpg"

transform fit_height:
    ysize config.screen_height

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bedroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # Alarm clock sound

    # These display lines of dialogue.

    # Yawning sound
    "(yawns) I'm late!"
    "I have to get ready for my interview quickly! But I don't have enough time to get everything ready..."
    # Show list of things to do to get ready
    "It's 9:00 right now. I'll have to leave the house by 9:10 to get to my interview on time."
    "I'll have to sacrifice some things, but what?"
    jump shower


label shower:
    scene bg shower
    "Oh man. I'm gonna have to take a shower. If only I woke up earlier."
    menu:
        "Take a shower.":
            "Welp. Shower it is."
            $ showered = 1
            # Blur screen and fade to black
            jump teethbrush
        "Don't take a shower.":
            "I'll be fine without a shower."
            jump teethbrush

label teethbrush:
    scene bg sink with fade
    if showered == 0:
        "Still have 9 minutes left."
        "Time to brush my teeth."
    elif showered == 1:
        "Alright, time to brush my teeth."
        "3 minutes left, not enough time!"
    menu:
        "Brush your teeth.":
            "There's no way I'm gonna go to my date with a bad breath."
            "Especially when I'm fresh out of breath mints."
            $ teethbrushed = 1
            jump hair
        "Don't brush your teeth.":
            "I don't have time to brush my teeth."
            jump hair

label hair:
    scene bg wardrobe with fade
    if showered == 0:
        "My hair is still messy from when I woke up."
        if teethbrushed == 0:
            "9 minutes. Shouldn't have wasted time just going in the bathroom."
        elif teethbrushed == 1:
            "7 minutes. Combing my hair shouldn't take too long."
    elif showered == 1:
        "I still need to comb my hair after my shower."
        if teethbrushed == 0:
            "3 minutes. Combing my hair shouldn't take too long."
        elif teethbrushed == 1:
            "1 minute. I am NOT leaving in time."
    menu:
        "Comb your hair.":
            "I don't wanna look like I just woke up."
            "(mutters) Even though I did."
            $ combed = 1
            jump clothes
        "Don't comb your hair.":
            "Hopefully she doesn't care about my hair."
            jump clothes

label clothes:
    scene bg wardrobe
    "If only I ironed my clothes yesterday!"
    menu:
        "Iron and put on clothes.":
            "Time to iron my clothes..."
            scene bg wardrobe with fade
            $ changed = 1
            pause 1.0
            "All changed!"
            jump date
        "Don't iron and put on clothes.":
            "No time to iron my clothes."
            "I'll just have to put them on the way the are."
            scene bg wardrobe with fade
            $ changed = 0.5
            pause 1.0
            "All changed!"
            jump date
        "Don't change clothes at all.":
            "I do not have time to change my clothes."
            "Seems like I'll have to go in my PJs."
            jump date

label date:
    scene bg restaurant with fade
    '''
    if showered == 0:
        if teethbrushed == 0:
            if combed == 0:
                if changed == 0:
                    pass
                    jump bad
                elif changed == 1:
                    pass
            elif combed == 1:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
        elif teethbrushed == 1:
            if combed == 0:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
            elif combed == 1:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
    elif showered == 1:
        if teethbrushed == 0:
            if combed == 0:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
            elif combed == 1:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
        elif teethbrushed == 1:
            if combed == 0:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
            elif combed == 1:
                if changed == 0:
                    pass
                elif changed == 1:
                    pass
    '''

label bad:
    scene bg bedroom with fade
    "She broke up with me..."

label good:
    scene bg bedroom with fade
    "That date went really well!"

label mid:
    scene bg bedroom with fade
    "The date went alright."

    return
