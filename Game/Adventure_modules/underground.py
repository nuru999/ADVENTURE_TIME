import random

class Player:
    def __init__(self, name, health=100, damage=50):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        target.receive_damage(self.damage)
        print(f"The {self.name} damaged the {target.name}!")

    def award_health_points(self, points):
        self.health += points

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

class UndergroundCavernsAdventure:
    description = "A vast network of dark and winding caverns beneath the earth's surface, illuminated only by the glow of bioluminescent fungi."

    def __init__(self, player):
        self.player = player
        self.rat = Player("Skinwalker", 40, 15)

    def play_game(self):
        print("Welcome to the Underground Caverns Adventure!")
        print("You have two challenges to face.")

        # First Challenge: Guessing Game
        print("\nFirst Challenge: Guess the Random Number!")
        if self.generate_random_number():
            pass

        # Ask the player whether to proceed with the second challenge
        user_input = input("Do you want to proceed to the second challenge? Type 'battle' to engage in a battle or 'exit' to leave: ").lower()

        if user_input == 'exit':
            print("You decide to leave the caverns. Thanks for playing!")
        elif user_input == 'battle':
            # Second Challenge: Battle
            print("\nSecond Challenge: Battle with a Mythical Creature!")
            self.battle()
        else:
            print("Invalid command. Exiting the caverns. Thanks for playing!")

    def generate_random_number(self):
        random_number = random.randint(1, 10)

        for guess_attempt in range(6):
            user_guess = int(input(f"Attempt {guess_attempt + 1}: Guess the random number (between 1 and 10): "))

            if user_guess == random_number:
                print("Congratulations! You guessed the correct number. ")
                self.player.award_health_points(20)  # Award health points for successful guess
                print("You have gained 20 points!")
                print(f"Your health is now a robust {self.player.health} points. Well done, {self.player.name}!")

                return True  # Signal that the correct number was guessed

            elif guess_attempt < 5:
                print(f"Sorry, that's not correct. Try again!")

        print(f"Sorry, the correct number was {random_number}. Better luck next time! you will not know the secret of this underground caverns!")
        return False

    def battle(self):
        print(f"You encounter a mythical creature in the caverns: {self.rat.name}!")

        while self.rat.health > 0 and self.player.health > 0:
            # Player's turn
            print("\nPlayer's Turn:")
            action = input("Choose your action: 'attack', 'defend', or 'escape': ").lower()

            if action == 'attack':
                self.player_attack()
            elif action == 'defend':
                self.player_defend()
            elif action == 'escape':
                self.player_escape()
            else:
                print("Invalid action. Try again.")

            if self.rat.health <= 0:
                print(f"You defeated {self.rat.name}! Congratulations!")
                self.player.award_health_points(30)  # Award additional health points for defeating the creature
                print(f"Your health points: {self.player.health}")
                break

            # Rat's turn
            print("\nRat's Turn:")
            rat_action = random.choice(['attack', 'defend', 'escape'])

            if rat_action == 'attack':
                self.rat_attack()
            elif rat_action == 'defend':
                self.rat_defend()
            elif rat_action == 'escape':
                self.rat_escape()

            if self.player.health <= 0:
                print("You were defeated by the mythical creature. Better luck next time!")
                break

    def player_attack(self):
        attack_damage = random.randint(10, 20)
        self.rat.take_damage(attack_damage)
        print(f"You dealt {attack_damage} damage to {self.rat.name}.")

    def player_defend(self):
        defense_bonus = random.randint(5, 10)
        self.player.award_health_points(defense_bonus)
        print(f"You defended against the mythical creature and gained {defense_bonus} health points.")

    def player_escape(self):
        escape_success = random.choice([True, False])
        if escape_success:
            print("You successfully escaped from the mythical creature!")
            self.player.award_health_points(10)
        else:
            print("Escape attempt failed. The mythical creature attacks you.")

    def rat_attack(self):
        attack_damage = random.randint(8, 15)
        self.player.take_damage(attack_damage)
        print(f"{self.rat.name} dealt {attack_damage} damage to you.")

    def rat_defend(self):
        defense_bonus = random.randint(3, 8)
        self.rat.award_health_points(defense_bonus)
        print(f"{self.rat.name} defended against your attack and gained {defense_bonus} health points.")

    def rat_escape(self):
        print(f"{self.rat.name} attempts to escape.")

if __name__ == "__main__":
    # Create a player instance
    player = Player(name="Avatar Roshi")

    # Create an instance of the UndergroundCavernsAdventure
    adventure = UndergroundCavernsAdventure(player)

    # Start the adventure
    adventure.play_game()
