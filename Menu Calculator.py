selection=""

menu = """

*****Menu*****

Chicken Strips - $3.50
French Fries - $2.50
Hamburger - $4.00
Hotdog - $3.50
Large Drink - $1.75
Medium Drink - $1.50
Milk Shake - $2.25
Salad - $3.75
Small Drink - $1.25"""



while selection != "E":
    print(menu)
    order = input("Enter Your order: ")
    menu = {"1":3.5,
            "2":2.5,
            "3":4.0,
            "4":3.5,
            "5":1.75,
            "6":1.5,
            "7":2.25,
            "8":3.75,
            "9":1.25}

    length = len(order)
    sum = 0
    for i in order:
        sum+=menu[i]
    print(sum)

    selection = input("[E]xit\n[N]ew Order\n: ")
    selection.upper()