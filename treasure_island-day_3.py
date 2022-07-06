print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\\\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \\ "/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\\
 \_/__________________________________________________________________/
 ''')
print("Welcome to treasure island!\nYour mission is to find the treasure.")
dec_1 = input("You've arrived at a fork in the road. Will you go LEFT or RIGHT? ")

dec_1 = dec_1.lower()

if dec_1 == "right":
    print("You go left and are caught in a net trap hidden under a pile of leaves. You die from dehydration after four days. Game over.")
    exit()

dec_2 = input("After taking the right path, you come across a rushing strem. Will you try to SWIM across or WAIT for the water to calm down? ")
dec_2 = dec_2.lower()
if dec_2 == "swim":
    print("While at first you were able to fight against the water, you soon succumb and drown. Game over.")
    exit()

dec_3 = input("After what felt like forever, the stream calmed down and you were able to cross. You've come across a stange building on the other side with three doors. Which one will you enter, the RED one, the YELLOW one, or the BLUE one?")
dec_3 = dec_3.lower()
if dec_3 == "yellow":
    print("You open the yellow door and find a cave full of riches the likes of which you have never seen! You win!")
    exit()
else:
    print("Behind the door was a gun rigged to fire upon opening. You are shot square in the heart. Game over.")
    exit()