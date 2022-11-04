
while True :
    Number  = input("Enter Number : ")
    try:
        temp = int(Number)
    except:
        pass
    else:
        break
expression = ""
for i in Number:
    expression += f"+({i}**{len(Number)})"

print(eval(expression))

