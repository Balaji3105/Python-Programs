import random

#function to check the number
def NumberGuess(g,n,r1,r2):
    r=0
    d=int((r1+r2)/2)
    if g == n:
        r=0
    elif g<n :
        r=1
    elif g>n:
        r=2
    return r

#Getting the inputs for range
r1=int(input('Enter the starting number: '))
r2=int(input('Enter the ending number:'))

#Creating a random integer between r1 & r2 and storing it in a variable
n=random.randint(r1,r2)

#Guess number
g=int(input("Guess the number between: "))
s,c=0,1

for i in range(r2):
    s=NumberGuess(g,n,r1,r2)
    c+=1
    if s==0:
        break
    elif s==1:
        r1=r2/2
        g = int(input("You guessed too low. Please guess again..."))

    elif s == 2:
        r2=r2/2
        g = int(input("You guessed too high.Please guess again..."))

print("You did it in ",c,"tries. Congrats!")


