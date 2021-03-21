import random
import string
#I made this on my own lol

a=["rock",'paper','scissor']
n=str(input("Enter your choice, rock/paper/scissor"))

if n=="rock":
    print(random.choice(a))
elif n=="paper":
    print(random.choice(a))
elif n=="scissor":
    print(random.choice(a))

