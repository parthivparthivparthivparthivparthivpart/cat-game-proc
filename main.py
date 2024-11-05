cat_attributes = {
    "Intelligence": 10,
    "Energy": 50,
    "Weight": 10,
    "Sanity": 75
}
universe_attributes = {
    "Mass": 1000000000000
}
import re
cat_name = input("What is the name of your cat? ")
if re.search(r'[^a-zA-Z0-9]', cat_name):
    print('we have deduced that your cat is an eldritch being as it has an otherwordly name, so care for it at your own risk')
cat_color = input("What is the color of your cat? ")
while True:
    print(f"\nCat Name: {cat_name}, Color: {cat_color}, Attributes: {cat_attributes}")
    print("\nWhat would you like to do with your cat?")
    print("a. Play with your cat")
    print("b. Train it")
    print("c. Feed it")
    print("d. Put it to sleep")
    print("e. Print latest stats")

    choice = input("Choose an option (a, b, c, d, e): ").lower()

    if choice == 'a':
        # Play with the cat
            print("You play with your cat!")
            cat_attributes["Energy"] -= 4
            cat_attributes["Intelligence"] += 1


    elif choice == 'b':
        # Train the cat
        print("You train your cat!")
        cat_attributes["Intelligence"] += 3
        cat_attributes["Energy"] -= 10

    elif choice == 'c':
        # Feed the cat
        print("You feed your cat!")
        cat_attributes["Energy"] += 20
        cat_attributes["Weight"] += 1

    elif choice == 'd':
        # Put the cat to sleep
        print("You put your cat to sleep.")
        cat_attributes["Energy"] += 5
        cat_attributes['Intelligence'] -= 1

    elif choice == 'e':
        # Print the latest stats
        print(f"Latest Stats: {cat_attributes}")

    else:
        print("Invalid option, please try again.")

    if cat_attributes["Intelligence"] <0:
        print(f"{cat_name} became so stupid it escaped your house and 7 cars ran over it")
        break

    if cat_attributes["Energy"] <0:
        print(f"{cat_name} Has lost all of their energy.")
        if cat_attributes["Energy"] <0:

           if choice == 'a':
               cat_attributes["Intelligence"] += 1
               cat_attributes["Sanity"] -= 5
               print(f"{cat_name} tried to play with you, but is starting to lose its sanity")
           if choice == 'b':
               cat_attributes["Weight"] -= 1
               cat_attributes["Intelligence"] += 1
               cat_attributes["Sanity"] -= 10
               cat_attributes['Energy'] -= 10
               print(f"{cat_name} tried training and did enough, but is losing sanity")
    if cat_attributes['Sanity'] <50:
        if re.search(r'[^a-zA-Z0-9]', cat_name):
            print(f"Ending 3: your eldritch being, {cat_name}, has lost too much sanity and destroyed the universe")
            break
        cat_attributes["Weight"] -= 5
        cat_attributes["Intelligence"] += 10
        cat_attributes["Sanity"] -= 10
        cat_attributes['Energy'] -= 10
        print('Your cat is starting to despise you')
    if cat_attributes["Weight"] <5:
        print(f'Ending 2: {cat_name} ate itself from starvation and died')
        break
    if re.search(r'[^a-zA-Z0-9]', cat_name):
        if cat_attributes["Energy"] >100:
          print('you have given your eldritch God too much power and it is starting to slowly decamate the universe')
          universe_attributes["Mass"] -= 100000000000
    if universe_attributes["Mass"] <0:
        print(f'Ending 1: {cat_name} destroyed everything but you, and now you both live in the void')
        break