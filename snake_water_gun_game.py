import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="s":
            return True
        elif you=="g":
            return False
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
print("comp turn: Snake(s) Water(w) Gun(g)?")
randno=random.randint(1,3)
if randno==1:
    comp="s"
elif randno==2:
    comp="w"
else:
    comp="g"
you=input("your turn: Snake(s) Water(w) Gun(g)? ")
a=gamewin(comp,you)
print(f"you choose {you}")
print(f"comp choose {comp}")
if a==None:
    print("Its a tie!")
elif a:
    print("You win ")
else:
    print("You loose")
