#lets create a simple die simulator in python

import random

choice = "YES"  #user choice for future rolls
i = 0           #count the no of rolls

print("\t...DIE SIMULATOR...\n")
print("Rolling die for the first time...\n")

while(choice.upper() == "YES"):
    i += 1
    n = random.randint(1,6)     #generate a random number for the die roll
    print("Roll "+str(i)+" output: "+str(n))
    
    choice = input("\nDo you want to continue (YES/NO): ")
    
print("You have rolled the die "+str(i)+" times")
