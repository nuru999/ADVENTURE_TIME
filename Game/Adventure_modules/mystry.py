import random
import time

class Avatar:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.relics = None

class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Attacker:
    def __init__(self, name, damage_power):
        self.name = name
        self.damage_power = damage_power
 
def choose_avatar(avatars):
    print("Choose your avatar:")
    for i, avatar in enumerate(avatars, start=1):
        print(f"{i}. {avatar.name}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen avatar: "))
            if 1 <= choice <= len(avatars):
                return avatars[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_riddle(riddles, max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        riddle = random.choice(riddles)
        print("Riddle:", riddle.question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == riddle.answer:
            print("Congratulations! You solved the riddle.")
            return True
        else:
            print(f"Sorry, the answer was incorrect. Try again. Attempts left: {max_attempts - attempt}")

    return False

def play_game(avatar):
    print("Fight a bear and earn a relic or run.")
    relic_names = ["Sword of Wisdom", "Shield of Valor", "Amulet of Power", "Ring of Luck", "Staff of Mysteries"]
    
    while True:
        choice = input("Choose an action (1: Run, 2: Fight): ")

        if choice == '1':
            time.sleep(2)
            print("You ran away. Game over.")
            break
        elif choice == '2':
            attacker = Attacker("Bear", 30)
            print(f"You chose to fight a bear with {avatar.health} health.")

            if avatar.health > attacker.damage_power:
                time.sleep(2)
                print("Congratulations! You defeated the bear and earned a random relic.")
                earned_relic_name = random.choice(relic_names)
                avatar.relics = earned_relic_name
                # No need to commit changes since we're not using a database
                
            else:
                time.sleep(2)
                print("You were defeated by the bear. Game over.")

            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Main game logic
avatar_names = ["Knight", "Wizard", "Elf", "Dwarf"]
attacker_names = ["bear", "leopard", "Lion", "Zebra"]
attacker_damages = [30, 25, 40, 15]
riddles_data = [
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
]

avatars = [Avatar(name) for name in avatar_names]
attackers = [Attacker(name, damage) for name, damage in zip(attacker_names, attacker_damages)]
riddles = [Riddle(**data) for data in riddles_data]

chosen_avatar = choose_avatar(avatars)
print(f"You've chosen the avatar: {chosen_avatar.name}")

if ask_riddle(riddles):
    print("Congratulations! You solved the riddle.")
    play_game(chosen_avatar)
else:
    print("Sorry, you've run out of attempts. Game over.")
