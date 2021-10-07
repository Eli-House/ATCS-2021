p = ["Sudar", "Eli", "Eddie", "Charlie"]

def c(a):
    if len(a) > 3:
        print("The rooms is full")
    else:
        print("Open space")

c(p)

p.pop(0)
p.pop(2)

c(p)