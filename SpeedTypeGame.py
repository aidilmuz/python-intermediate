import random
import time


def SpeedTypeGame():
    words = ["python", "java", "javascript", "html", "css", "ruby", "swift", "kotlin", "typescript", "csharp"]
    word = random.choice(words)

    print("Welcome to the Typing Speed Test!")
    print(f"Type the following word as fast as you can: {word}")
    input("Press Enter when you are ready...")

    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    if user_input == word:
        time_taken = round(end_time - start_time, 2)
        print(f"Great job! You typed the word correctly in {time_taken} seconds.")
    else:
        print(f"Oops! That's not correct. The correct word was '{word}'.")

if __name__ == "__main__":
    SpeedTypeGame()