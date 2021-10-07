a = ["Crossy Roads", "Apex", "Clash of Clans", "Call of Duty"]
for b in a:
    print("My fav games" , b)

z = False

while (z == False):
    userGame = input("What game your like?")
    a.append(userGame)
    play = input("Type y to add another game. Type n to stop adding games")
    if play == 'n':
        z = True

for c in a:
    print("Our fav games" , c)
