# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("MoM", color ="#EE4B2B")

define s = Character("Sharma's SON", color = "#964B00")
define pov = Character("[player_name]")

init python:
    import random
    bgm_tracks = [
        "audio1.mp3",
        "audio2.mp3",
        
    ]



# The game starts here.

label start:

    
    $ selected_bgm = random.choice(bgm_tracks)
    play music selected_bgm fadein 1.0 loop volume 0.5


    image scene1 = "images/scene 1.png"
    image scene2 = "images/scene 2.png"
    image scene3 = "images/scene 3.png"
    image scene4 = "images/scene 4.png"
    image scene5 = "images/scene 5.png"
    image scene6 = "images/scene 6.png"
    image scene7 = "images/scene 7.png"
    image scene8 = "images/scene 8.png"
    image scene9 = "images/scene 9.png"
    image scene10 = "images/scene 10.png"
    image scene11 = "images/scene 11.png"
    image scene12 = "images/scene 12.png"
    image scene13 = "images/scene 13.png"
    image good = "images/goodending.png"

    show scene12
    $player_name = renpy.input("WHAT'S YOUR NAME KIDOO?", length=15)
    $player_name = player_name.strip()

    if not player_name:
        $ player_name = "IDIOT"

   

    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene MY BEDROOM

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show scene1

    # These display lines of dialogue.

    
    
    

    m "WAKE UPPPP!!! ,..... ahh! THIS KID."
    show scene2
    m "(turns off the fan for no particular reason)"
    show scene3

    pov '"z..zzz"'
    show scene4
    pov '"z..zzz"'
    pov '"z..zzz.." (feels the burn of 48 degrees allover)'
    show scene5
    pov 'hey! who turned off the GODDAMN FANNNN!'
    "(bro thinks he scary)"
    show scene6
    m "YOUR MOTHER!! (grabs me by the hair and throws me out of bed.)"
    m "You realize what time it is!??"
    m "Mr Sharma's son woke up at 5 am."
    m "he is the one who goes to buy milk in their house."
    m "then there's you!!"
    m "A fool!"

    menu:
        "WHAT SHOULD I DO???"
        "(STAY SCILENT)":
            jump goodending
        "(Lie)":
            jump fight

label fight:
    
    pov "...."
    pov "MoM he smokes in the park at 5 am with the Milk man."
    pov "(lying hard to sabe my azzz)"
    m "hey! how dare you talk to your mom like that!!"
    show scene7
    m "(she reaches for the broom.)"
    show scene8
    pov "(I reach for the captian america shield.)"
    pov "(My life depends on it \"literally\")"
    show scene9
    pov "(Thinking I am worthy!)"
    show scene10
    play sound 'audio/avenger3.mp3' volume 2
    pov "Avengers!"
    show scene11
    pov "Assemble"
    show scene12

    "(Meanwhile in the park)"
    "..."
    show scene13
    s "AHH! yes stronger"
    s "where "
    s "do you"
    s "get this shizzz"
    s "crazy!!"

    return

    label goodending:
    show good

    "--you live on--"

    


    



    # This ends the game.

    return
