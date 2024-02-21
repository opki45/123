import time
import random


class Place:
    def __init__(self, name_of_place, size_of_place, locked=False):
        self.name = name_of_place
        self.size = size_of_place
        self.locked = locked
        self.next_places = []
        self.new_items = []

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def is_locked(self):
        return self.locked

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.new_items.append(item_instance)

    def show_next_places(self):
        print("According, to the map, the next available places you can go to from here are: ")
        for place in self.next_places:
            print(place.get_name())
        choice_one = input("Enter the one you would want to go to: ")


class Player:
    def __init__(self, given_name, points_collected):
        self.name = given_name
        self.points = points_collected
        self.current_place = None
        self.inventory = []

    def move_to_next_place(self, next_place):
        self.current_place = next_place
        print(f"You are currently in {self.current_place.name}")

    def receive_points(self, additional_points):
        self.points += additional_points
        print(f"You have received {additional_points} points. Total points are now: {self.points}")

    def battle(self):
        print(f"{self.name} is now fighting villains with a sword")
        # sword taking place for an item

    def answer_riddle_question(self):
        # player is answering riddle
        pass

    def win(self):
        print(
            "Congratulations, since you have found the treasure you have won the game"
        )

    def lose(self):
        print("Unfortunately, you have lost the game")

    def __str__(self):
        return (f"Player: {self.name}, Points: {self.points}, "
                f"Current Place: {self.current_place.name if self.current_place else 'None'}")


class Item:
    def __init__(self, item_name):
        self.name_of_item = item_name

    def buy_item(self):
        print(f"{self.name_of_item} is being bought with points received ")

    def use_item(self):
        print(f"Do you want to use {self.name_of_item}?")


class Game:
    def __init__(self):
        self.current_place = None
        self.player = Player("PlayerName", 0)

    def setup(self):
        # using beach house on a deserted island
        plane = Place("plane", 50)
        island = Place("Deserted Island", 400)
        ocean = Place("Ocean", 670)
        beach_home = Place("Crusty Beach House", 275)
        living_room = Place("Living Room", 55)
        bedroom = Place("Bedroom", 25)
        kitchen = Place("Kitchen", 22)
        backyard = Place("Backyard", 45)
        shed = Place("Shed", 53)
        bathroom = Place("Bathroom", 22, True)  # bathroom here is open

        # appending/adding to new places
        plane.add_next_place(island)
        plane.add_next_place(ocean)
        ocean.add_next_place(island)
        island.add_next_place(beach_home)
        beach_home.add_next_place(living_room)
        living_room.add_next_place(kitchen)
        kitchen.add_next_place(backyard)
        backyard.add_next_place(kitchen)
        kitchen.add_next_place(bathroom)
        bathroom.add_next_place(bedroom)
        bedroom.add_next_place(bathroom)
        backyard.add_next_place(shed)
        shed.add_next_place(backyard)

        # creating instances of items
        food = Item("Food")
        water_bottle = Item("Water")
        pen = Item("Pen")
        map = Item("Map")
        lighter = Item("Lighter")
        scissors = Item("Scissors")
        knife = Item("Knife")
        lawn_mower = Item("Lawn mower")
        # will add more as i create story

        plane.add_item(lighter)
        kitchen.add_item(knife)
        kitchen.add_item(scissors)
        bedroom.add_item(pen)
        shed.add_item(lawn_mower)
        kitchen.add_item(food)
        kitchen.add_item(water_bottle)
        living_room.add_item(map)
        # will add more as further develop game

        self.current_place = plane

    def start(self):
        print("Welcome to my game!")
        print("Calamity and Misfortune has befallen you, "
              "as you were on a flight to the UK to surprise your computer science teacher for his birthday party,"
              " your plane crashed into the ocean. Luckily for you, "
              "on a plane of 6000 passengers, you have been chosen to still be alive!!!  ")
        print("After suffering, crying, wailing for help,"
              " you find a way to a smart house which helps you "
              "access your inventory and attempt to help you out of the island and almost make it in time for your computer"
              " science teacher's birthday, "
              "however you must set out on a mission to find the treasure that the Stark Industries PR team has hidden.")
        print("You have half an hour to complete the game, You may begin...")

        game_running = True
        start_time = time.time()

        while game_running:
            elapsed_time = time.time() - start_time

            if elapsed_time >= 1800:
                print("Time is up! Game over.")
                game_running = False
                break

            self.display_current_state()

            # collect player input
            choice = input("Enter your choice: ")

            # process player input
            self.process_player_choice(choice)

            # check game ending conditions
            if self.check_game_end_conditions():
                game_running = False
        print("Game over.")

    def display_current_state(self):
        print(f"\nCurrent Place: {self.current_place.name}")
        print("Available actions:")
        print("1. Move to a different place")
        print("2. Examine your inventory")
        print("3. Quit the game")

    def process_player_choice(self, choice):
        if choice == "1":
            self.move_to_next_place()
        elif choice == "2":
            self.display_inventory()
        elif choice == "3":
            print("Quitting the game...")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def move_to_next_place(self):
        next_place = random.choice(self.current_place.next_places)
        # self.player.move_to_next_place(next_place)
        self.current_place = next_place
        print(f"You have moved to {self.current_place.name}")
        print("As you are there you are approached by an old man who asks you a riddle! "
              "You need to answer correctly to proceed")

    def receive_clue(self, clue):
        print(f"You received a clue: {clue}")

    def answer_riddle(self):
        riddle_question = "What has a heart that doesnt beat?"
        options = ["A rock", "A tomato", "An artichoke", "An egg"]
        correct_answer = "An artichoke"

        while True:
            print(f"Riddle: {riddle_question}")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            player_answer = input("Enter the number of your answer: ")

            if player_answer.isdigit() and 1 <= int(player_answer) <= len(options):
                if options[int(player_answer) - 1] == correct_answer:
                    print("Correct! You gain 10 points and receive a clue.")
                    self.player.receive_points(10)
                    self.player.receive_clue("The clue says: Follow the path of the moonlight.")
                    next_place = random.choice(self.current_place.next_places)
                    self.current_place = next_place
                    print(f"You have moved to {self.current_place.name}")
                    break
                else:
                    print("Incorrect! Try again.")
            else:
                print("Invalid answer. Please try again.")

    def encounter_villain(self):
        print("A villain has appeared!")
        # background logic of villian
        # use of inventory items to battle
        print("You can check your inventory and select items to use in the battle.")
        self.display_inventory()
        selected_items = self.select_items_for_battle()
        # battle with villian
        battle_result = self.battle_with_villain(selected_items)

        if battle_result:
            print("Villain defeated! You gain 50 points.")
            self.player.receive_points(50)

            # After defeating the villain, check the villain's inventory
            print("You can now check the villain's inventory.")
            villain_items = self.check_villain_inventory()

            # Allow the player to select items from the villain's inventory
            self.select_items_from_villain(villain_items)
        else:
            print("You were unable to defeat the villain. Better luck next time!")

    def select_items_for_battle(self):
        print("You can check your inventory and select items to use in the battle.")
        self.display_inventory()
        selected_items = []
        while True:
            item_choice = input("Enter the name of the item you want to use (or 'done' to finish): ").lower()

            if item_choice == 'done':
                break
            elif item_choice in self.player.inventory:
                if item_choice not in selected_items:
                    selected_items.append(item_choice)
                    print(f"{item_choice} added to your battle items.")
                else:
                    print(f"You've already selected {item_choice}. Choose a different item.")
            else:
                print("Invalid item. Please select from your inventory.")

        return selected_items

    def battle_with_villain(self, selected_items):
        print("Battling the villain...")
        success_chance = 0.7  # 70% chance of success for each item

        for item in selected_items:
            if random.random() < success_chance:
                print(f"You successfully used {item} in the battle!")
            else:
                print(f"{item} failed to have an impact on the villain.")

        # Determine overall battle result based on the success of individual items
        battle_result = random.random() < success_chance
        return battle_result

    def check_villain_inventory(self):
        print("Now that you have defeated the villian. You check his inventory. he has an Evil potion,"
              " a Dark Amulet and a Cursed dagger. Pick wisely as what you choose will help you in the next mission.")
        villain_items = ["Evil Potion", "Dark Amulet", "Cursed Dagger"]
        print("The villain dropped the following items:")
        for item in villain_items:
            print(item)
        return villain_items

    def select_items_from_villain(self, villain_items):
        print("The villain dropped the following items:")
        for item in villain_items:
            print(item)

        selected_items = []
        while True:
            item_choice = input("Enter the name of the item you want to take (or 'done' to finish): ")
            if item_choice.lower() == 'done':
                break
            elif item_choice in villain_items:
                selected_items.append(item_choice)
                print(f"{item_choice} added to your inventory.")
            else:
                print("Invalid item. Please select from the villain's inventory.")
        # add selected items to players inventory
        self.player.add_items_to_inventory(selected_items)

    def transport_to_gladiator_timeline(self):
        print(
            "Oh no! You accidentally pressed something on the villain and find yourself transported"
            " to a different timeline.")
        print("You are now in ancient Rome, in the middle of a gladiator arena.")
        print("Gladiators are fighting for their lives, and you must find a way to win!")

        # three items for the player to choose from
        gladiator_items = ["Lighter", "Air Freshener", "Water"]
        print("You find three items in your inventory:")
        for item in gladiator_items:
            print(item)

        # player selects an item for battling in the arena
        selected_item = input("Choose an item to use as a weapon: ").capitalize()

        if selected_item in gladiator_items:
            print(f"You use the {selected_item} as a weapon that shoots straight fire!")
            print("You defeat five gladiators with your fiery weapon.")

            # Player's victory
            print("For your victory, the king wants to honor you and offers you any treasure you desire.")

            # Ask the player for their choice
            print(
                "The king asks, 'Do you want to stay in this timeline with a lavish villa, riches, wealth,"
                " success, food, safety, and honor, or do you want to go back in time and surprise "
                "your computer science teacher for his birthday?'")

            player_choice = input("Enter 'stay' or 'go back': ").lower()

            if player_choice == 'stay':
                print(
                    "You choose to stay in ancient Rome. The king honors your decision, "
                    "but unfortunately, you are disqualified from the game "
                    "because you didn't find the treasure.")
            elif player_choice == 'go back':
                print("You choose to go back in time and surprise your computer science teacher.")
                print("The king decides to ask you a riddle")

                riddle_question = "What has keys but can't open locks?"
                correct_answer = "A piano"
                player_answer = input(f"The king asks, '{riddle_question}' Enter your answer: ")

                if player_answer.lower() == correct_answer.lower():
                    print("Correct! The king rewards you with a genie kettle.")
                    print(
                        "The genie can't transport you back directly, but it can give you directions with two wishes.")
                    print("By following the genie's guidance, you build a time machine and successfully surprise your"
                          " computer science teacher.")
                    print("The treasure is your teacher's happiness!")
                    self.player.win()
                else:
                    print("Incorrect answer. You do not receive the genie kettle.")
            else:
                print("Invalid choice. The king is confused, and you make no decision.")
        else:
            print("Invalid item. You must choose one of the provided items.")

    def add_items_to_inventory(self, items):
        self.inventory.extend(items)
        print(f"Added {', '.join(items)} to your inventory.")

    def display_inventory(self):
        print(f"{self.player.name}'s Inventory:")
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            for item in self.inventory:
                print(item)

    def check_game_end_conditions(self):
        if self.check_win_condition() or self.check_lose_condition():
            return True

        return False

    def check_win_condition(self):
        if self.player.points >= 100:
            self.player.win()
            return True
        return False

    def check_lose_condition(self):

        if self.player.points < 0:
            self.player.lose()
            return True
        return False

    def play(self):
        self.setup()
        self.start()

        while True:
            self.display_current_state()

            next_place = random.choice(self.current_place.next_places)
            self.player.move_to_next_place(next_place)

            self.encounter_villain()

            if self.check_win_condition() or self.check_lose_condition():
                break

            self.answer_riddle()

            continue_game = input("Do you want to continue to the next place? (yes/no): ").lower()

            if continue_game != 'yes':
                print("Ending the game.")
                break

            self.transport_to_gladiator_timeline()

            if self.check_win_condition() or self.check_lose_condition():
                break

            continue_game = input("Do you want to continue to the next place? (yes/no): ").lower()

            if continue_game != 'yes':
                print("Ending the game.")
                break

        print("Game Over.")


game_instance = Game()
game_instance.play()
import time
import random


class Place:
    def __init__(self, name_of_place, size_of_place, locked=False):
        self.name = name_of_place
        self.size = size_of_place
        self.locked = locked
        self.next_places = []
        self.new_items = []

    def get_name(self):
        return self.name

    def get_size(self):
        return self.size

    def is_locked(self):
        return self.locked

    def add_next_place(self, place_instance):
        self.next_places.append(place_instance)

    def add_item(self, item_instance):
        self.new_items.append(item_instance)

    def show_next_places(self):
        print("According, to the map, the next available places you can go to from here are: ")
        for place in self.next_places:
            print(place.get_name())
        choice_one = input("Enter the one you would want to go to: ")


class Player:
    def __init__(self, given_name, points_collected):
        self.name = given_name
        self.points = points_collected
        self.current_place = None
        self.inventory = []

    def move_to_next_place(self, next_place):
        self.current_place = next_place
        print(f"You are currently in {self.current_place.name}")

    def receive_points(self, additional_points):
        self.points += additional_points
        print(f"You have received {additional_points} points. Total points are now: {self.points}")

    def battle(self):
        print(f"{self.name} is now fighting villains with a sword")
        # sword taking place for an item

    def answer_riddle_question(self):
        # player is answering riddle
        pass

    def win(self):
        print(
            "Congratulations, since you have found the treasure you have won the game"
        )

    def lose(self):
        print("Unfortunately, you have lost the game")

    def __str__(self):
        return (f"Player: {self.name}, Points: {self.points}, "
                f"Current Place: {self.current_place.name if self.current_place else 'None'}")


class Item:
    def __init__(self, item_name):
        self.name_of_item = item_name

    def buy_item(self):
        print(f"{self.name_of_item} is being bought with points received ")

    def use_item(self):
        print(f"Do you want to use {self.name_of_item}?")


class Game:
    def __init__(self):
        self.current_place = None
        self.player = Player("PlayerName", 0)

    def setup(self):
        # using beach house on a deserted island
        plane = Place("plane", 50)
        island = Place("Deserted Island", 400)
        ocean = Place("Ocean", 670)
        beach_home = Place("Crusty Beach House", 275)
        living_room = Place("Living Room", 55)
        bedroom = Place("Bedroom", 25)
        kitchen = Place("Kitchen", 22)
        backyard = Place("Backyard", 45)
        shed = Place("Shed", 53)
        bathroom = Place("Bathroom", 22, True)  # bathroom here is open

        # appending/adding to new places
        plane.add_next_place(island)
        plane.add_next_place(ocean)
        ocean.add_next_place(island)
        island.add_next_place(beach_home)
        beach_home.add_next_place(living_room)
        living_room.add_next_place(kitchen)
        kitchen.add_next_place(backyard)
        backyard.add_next_place(kitchen)
        kitchen.add_next_place(bathroom)
        bathroom.add_next_place(bedroom)
        bedroom.add_next_place(bathroom)
        backyard.add_next_place(shed)
        shed.add_next_place(backyard)

        # creating instances of items
        food = Item("Food")
        water_bottle = Item("Water")
        pen = Item("Pen")
        map = Item("Map")
        lighter = Item("Lighter")
        scissors = Item("Scissors")
        knife = Item("Knife")
        lawn_mower = Item("Lawn mower")
        # will add more as i create story

        plane.add_item(lighter)
        kitchen.add_item(knife)
        kitchen.add_item(scissors)
        bedroom.add_item(pen)
        shed.add_item(lawn_mower)
        kitchen.add_item(food)
        kitchen.add_item(water_bottle)
        living_room.add_item(map)
        # will add more as further develop game

        self.current_place = plane

    def start(self):
        print("Welcome to my game!")
        print("Calamity and Misfortune has befallen you, "
              "as you were on a flight to the UK to surprise your computer science teacher for his birthday party,"
              " your plane crashed into the ocean. Luckily for you, "
              "on a plane of 6000 passengers, you have been chosen to still be alive!!!  ")
        print("After suffering, crying, wailing for help,"
              " you find a way to a smart house which helps you "
              "access your inventory and attempt to help you out of the island and almost make it in time for your computer"
              " science teacher's birthday, "
              "however you must set out on a mission to find the treasure that the Stark Industries PR team has hidden.")
        print("You have half an hour to complete the game, You may begin...")

        game_running = True
        start_time = time.time()

        while game_running:
            elapsed_time = time.time() - start_time

            if elapsed_time >= 1800:
                print("Time is up! Game over.")
                game_running = False
                break

            self.display_current_state()

            # collect player input
            choice = input("Enter your choice: ")

            # process player input
            self.process_player_choice(choice)

            # check game ending conditions
            if self.check_game_end_conditions():
                game_running = False
        print("Game over.")

    def display_current_state(self):
        print(f"\nCurrent Place: {self.current_place.name}")
        print("Available actions:")
        print("1. Move to a different place")
        print("2. Examine your inventory")
        print("3. Quit the game")

    def process_player_choice(self, choice):
        if choice == "1":
            self.move_to_next_place()
        elif choice == "2":
            self.display_inventory()
        elif choice == "3":
            print("Quitting the game...")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def move_to_next_place(self):
        next_place = random.choice(self.current_place.next_places)
        # self.player.move_to_next_place(next_place)
        self.current_place = next_place
        print(f"You have moved to {self.current_place.name}")
        print("As you are there you are approached by an old man who asks you a riddle! "
              "You need to answer correctly to proceed")

    def receive_clue(self, clue):
        print(f"You received a clue: {clue}")

    def answer_riddle(self):
        riddle_question = "What has a heart that doesnt beat?"
        options = ["A rock", "A tomato", "An artichoke", "An egg"]
        correct_answer = "An artichoke"

        while True:
            print(f"Riddle: {riddle_question}")
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            player_answer = input("Enter the number of your answer: ")

            if player_answer.isdigit() and 1 <= int(player_answer) <= len(options):
                if options[int(player_answer) - 1] == correct_answer:
                    print("Correct! You gain 10 points and receive a clue.")
                    self.player.receive_points(10)
                    self.player.receive_clue("The clue says: Follow the path of the moonlight.")
                    next_place = random.choice(self.current_place.next_places)
                    self.current_place = next_place
                    print(f"You have moved to {self.current_place.name}")
                    break
                else:
                    print("Incorrect! Try again.")
            else:
                print("Invalid answer. Please try again.")

    def encounter_villain(self):
        print("A villain has appeared!")
        # background logic of villian
        # use of inventory items to battle
        print("You can check your inventory and select items to use in the battle.")
        self.display_inventory()
        selected_items = self.select_items_for_battle()
        # battle with villian
        battle_result = self.battle_with_villain(selected_items)

        if battle_result:
            print("Villain defeated! You gain 50 points.")
            self.player.receive_points(50)

            # After defeating the villain, check the villain's inventory
            print("You can now check the villain's inventory.")
            villain_items = self.check_villain_inventory()

            # Allow the player to select items from the villain's inventory
            self.select_items_from_villain(villain_items)
        else:
            print("You were unable to defeat the villain. Better luck next time!")

    def select_items_for_battle(self):
        print("You can check your inventory and select items to use in the battle.")
        self.display_inventory()
        selected_items = []
        while True:
            item_choice = input("Enter the name of the item you want to use (or 'done' to finish): ").lower()

            if item_choice == 'done':
                break
            elif item_choice in self.player.inventory:
                if item_choice not in selected_items:
                    selected_items.append(item_choice)
                    print(f"{item_choice} added to your battle items.")
                else:
                    print(f"You've already selected {item_choice}. Choose a different item.")
            else:
                print("Invalid item. Please select from your inventory.")

        return selected_items

    def battle_with_villain(self, selected_items):
        print("Battling the villain...")
        success_chance = 0.7  # 70% chance of success for each item

        for item in selected_items:
            if random.random() < success_chance:
                print(f"You successfully used {item} in the battle!")
            else:
                print(f"{item} failed to have an impact on the villain.")

        # Determine overall battle result based on the success of individual items
        battle_result = random.random() < success_chance
        return battle_result

    def check_villain_inventory(self):
        print("Now that you have defeated the villian. You check his inventory. he has an Evil potion,"
              " a Dark Amulet and a Cursed dagger. Pick wisely as what you choose will help you in the next mission.")
        villain_items = ["Evil Potion", "Dark Amulet", "Cursed Dagger"]
        print("The villain dropped the following items:")
        for item in villain_items:
            print(item)
        return villain_items

    def select_items_from_villain(self, villain_items):
        print("The villain dropped the following items:")
        for item in villain_items:
            print(item)

        selected_items = []
        while True:
            item_choice = input("Enter the name of the item you want to take (or 'done' to finish): ")
            if item_choice.lower() == 'done':
                break
            elif item_choice in villain_items:
                selected_items.append(item_choice)
                print(f"{item_choice} added to your inventory.")
            else:
                print("Invalid item. Please select from the villain's inventory.")
        # add selected items to players inventory
        self.player.add_items_to_inventory(selected_items)

    def transport_to_gladiator_timeline(self):
        print(
            "Oh no! You accidentally pressed something on the villain and find yourself transported"
            " to a different timeline.")
        print("You are now in ancient Rome, in the middle of a gladiator arena.")
        print("Gladiators are fighting for their lives, and you must find a way to win!")

        # three items for the player to choose from
        gladiator_items = ["Lighter", "Air Freshener", "Water"]
        print("You find three items in your inventory:")
        for item in gladiator_items:
            print(item)

        # player selects an item for battling in the arena
        selected_item = input("Choose an item to use as a weapon: ").capitalize()

        if selected_item in gladiator_items:
            print(f"You use the {selected_item} as a weapon that shoots straight fire!")
            print("You defeat five gladiators with your fiery weapon.")

            # Player's victory
            print("For your victory, the king wants to honor you and offers you any treasure you desire.")

            # Ask the player for their choice
            print(
                "The king asks, 'Do you want to stay in this timeline with a lavish villa, riches, wealth,"
                " success, food, safety, and honor, or do you want to go back in time and surprise "
                "your computer science teacher for his birthday?'")

            player_choice = input("Enter 'stay' or 'go back': ").lower()

            if player_choice == 'stay':
                print(
                    "You choose to stay in ancient Rome. The king honors your decision, "
                    "but unfortunately, you are disqualified from the game "
                    "because you didn't find the treasure.")
            elif player_choice == 'go back':
                print("You choose to go back in time and surprise your computer science teacher.")
                print("The king decides to ask you a riddle")

                riddle_question = "What has keys but can't open locks?"
                correct_answer = "A piano"
                player_answer = input(f"The king asks, '{riddle_question}' Enter your answer: ")

                if player_answer.lower() == correct_answer.lower():
                    print("Correct! The king rewards you with a genie kettle.")
                    print(
                        "The genie can't transport you back directly, but it can give you directions with two wishes.")
                    print("By following the genie's guidance, you build a time machine and successfully surprise your"
                          " computer science teacher.")
                    print("The treasure is your teacher's happiness!")
                    self.player.win()
                else:
                    print("Incorrect answer. You do not receive the genie kettle.")
            else:
                print("Invalid choice. The king is confused, and you make no decision.")
        else:
            print("Invalid item. You must choose one of the provided items.")

    def add_items_to_inventory(self, items):
        self.inventory.extend(items)
        print(f"Added {', '.join(items)} to your inventory.")

    def display_inventory(self):
        print(f"{self.player.name}'s Inventory:")
        if not self.player.inventory:
            print("Your inventory is empty.")
        else:
            for item in self.inventory:
                print(item)

    def check_game_end_conditions(self):
        if self.check_win_condition() or self.check_lose_condition():
            return True

        return False

    def check_win_condition(self):
        if self.player.points >= 100:
            self.player.win()
            return True
        return False

    def check_lose_condition(self):

        if self.player.points < 0:
            self.player.lose()
            return True
        return False

    def play(self):
        self.setup()
        self.start()

        while True:
            self.display_current_state()

            next_place = random.choice(self.current_place.next_places)
            self.player.move_to_next_place(next_place)

            self.encounter_villain()

            if self.check_win_condition() or self.check_lose_condition():
                break

            self.answer_riddle()

            continue_game = input("Do you want to continue to the next place? (yes/no): ").lower()

            if continue_game != 'yes':
                print("Ending the game.")
                break

            self.transport_to_gladiator_timeline()

            if self.check_win_condition() or self.check_lose_condition():
                break

            continue_game = input("Do you want to continue to the next place? (yes/no): ").lower()

            if continue_game != 'yes':
                print("Ending the game.")
                break

        print("Game Over.")


game_instance = Game()
game_instance.play()
