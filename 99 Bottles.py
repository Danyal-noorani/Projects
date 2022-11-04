#99 bottles of beer on the wall, 99 bottles of beer.
#Take one down and pass it around, 98 bottles of beer on the wall.

for i in range(99,-1,-1):
    plu = "bottles"
    if i == 1:
        print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
        print(f"Take one down and pass it around, no more bottles of beer on the wall.\n")
    elif i==2:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i - 1} bottle of beer on the wall.\n")
    elif i==0:
        print(f"No more bottles of beer on the wall, no more bottles of beer")
        print(f"Go to the store and buy some more, 99 bottles of beer on the wall.")
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.\n")


