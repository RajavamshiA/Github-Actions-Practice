import random
import sys

print("🎮 Welcome to the Guessing Game!")

if len(sys.argv) < 2:
    print("❌ Please provide your guess (1-10). Example: python game.py 5")
    sys.exit(1)

player_guess = int(sys.argv[1])
number = random.randint(1, 10)

print(f"Your guess: {player_guess}")
print(f"Correct number: {number}")

if player_guess == number:
    print("✅ You win!")
else:
    print("❌ Try again!")