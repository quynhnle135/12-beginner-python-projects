def madlib():
    print("Let make some madlib programming related!")
    adj_one = input("What is the first adjective that comes to your mind? ")
    adj_two = input("How about the second adjective that you can think of right now? ")
    verb_one = input("Give me one verb please: ")
    verb_two = input("Mas verbo, por favor: ")
    famous_person = input("Who is your celebrity crush? Don't be shy, just tell me: ")

    programming_madlib = f"Computer programming is so {adj_one}! It makes me super {adj_two} all the time because \nI love to {verb_one}. " \
                         f"Stay hydrated and {verb_two} like you are {famous_person}!!!"

    print(programming_madlib)

    choice = input("Do you want to continue? Yes/No: ")
    if choice == "Yes":
        print("Let make some madlib about something more ordinary!")
        food = input("What do you want to eat now? ")
        name = input("Give me a name that pop up in your head right now! ")
        noun = input("One noun please: ")
        adjective = input("It's time to describe something. Can you give an adjective? ")
        verb_three = input("Action time! Give me one verb: ")
        verb_four = input("Another verb: ")
        verb_five = input("ANOTHER ANOTHER VERB: ")
        verb_six = input("LAST VERB, I PROMISE: ")
        madlib_one = f"It was {food} day at school, and {name} was super {adjective} for lunch. But when she went " \
                     f"outside to eat, a {noun} stole her {food}! {name} chased the {noun} all over school. " \
                     f"She {verb_four}, {verb_five}, and {verb_six} through the playground. Then she tripped on her " \
                     f"{noun} and the {noun} escaped! Luckily, {name}’s friends were willing to share their {food} with her."
        print(madlib_one)
    else:
        print("Good bye!")
