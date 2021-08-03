
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while (1 < 2):
    print "\n"
    print "Rock, Paper, Scissors!"
    userChoice = raw_input("R,P,or S: ")
    if not re.match("[SsRrPp]", userChoice):
        print "Please choose a letter:"
        print "[R]ock, [S]cissors or [P]aper."
        continue
    // Echo the user's choice
    print "You chose: " + userChoice
    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print "I choose: " + opponenetChoice
    if opponenetChoice == str.upper(userChoice):
        print "Tie! "
    #if opponenetChoice == str("R") and str.upper(userChoice) == "P"
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':      
        print "Scissors beats rock, I win, you're trash! "
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':      
        print "Scissors beats paper! I win, you're trash! "
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':      
        print "Paper beats rock. I win, you're trash! "
        continue
    else:       
        print "You have bested me. One day I shall come back for revenge..."
