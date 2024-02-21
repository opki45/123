import random
import time
words = ["apple","banana","cherry","donkey","giraffe","elephant","fish","jug","Hyper","Insidious"]


def start_game():
    print("This is a speed typing game!")
    input("Press Enter to start....")
    score = 0
    game_duration = 30
    start_time = time.time()
    while start_time < game_duration:
        word = random.choice(words)
        print(f"Type this word as fast as you can: {word}")
        user_input = input()
        if user_input.lower == word:
            score += 1
            print(f"Correct! Your current score is: {score}")
        else:
            print(f"Game over! Your final score is: {score}")


if __name__ == "__main__":
    start_game()

