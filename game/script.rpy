# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("MoM", color ="#EE4B2B")
define M = Character("ME")
define s = Character("Sharma's SON", color = "#964B00")

# The game starts here.

label start:
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

    M '"z..zzz"'
    show scene4
    M '"z..zzz"'
    M '"z..zzz.." (feels the burn of 48 degrees allover)'
    show scene5
    M 'hey! who turned off the GODDAMN FANNNN!'
    M "(bro thinks he scary)"
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
    
    M "...."
    M "MoM he smokes in the park at 5 am with the Milk man."
    M "(lying hard to sabe my azzz)"
    m "hey! how dare you talk to your mom like that!!"
    show scene7
    m "(she reaches for the broom.)"
    show scene8
    M "(I reach for the captian america shield.)"
    M "(My life depends on it \"literally\")"
    show scene9
    M "(Thinking I am worthy!)"
    show scene10
    M "Avengers!"
    show scene11
    M "Assemble"
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
