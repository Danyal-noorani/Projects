import random
selection = ""
while selection!= "e":
    question = input("Enter Question: ")
    lst = ["It is certain",
               "Reply hazy, try again",
               "Don’t count on it",
               "It is decidedly so",
               "Ask again later",
               "My reply is no",
               "Without a doubt",
               "Better not tell you now",
               "My sources say no",
               "Yes definitely",
               "Cannot predict now",
               "Outlook not so good"
               "You may rely on it",
               "Concentrate and ask again",
               "Very doubtful",
               "As I see it, yes",
               "Most likely",
               "Outlook good",
               "Yes",
               'Signs point to yes']

    print("Thinking...")

    print(random.choice(lst))

    selection = input("[E]xit \n[A]gain\n:  ")
    selection = selection.lower()
