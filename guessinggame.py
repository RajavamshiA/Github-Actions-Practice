import random

print("🎮 Welcome to the Guessing Game!")
number = random.randint(1, 10)

guess = random.randint(1, 10)  # Simulate a player guess
print(f"Player guessed: {guess}")
print(f"Correct number: {number}")

if guess == number:
    print("✅ You win!")
else:
    print("❌ Try again!")