

class SkyCityRuinsGame:
    def __init__(self, user):
        self.user = user

    def navigate_platforms(self):
        print("You navigate through floating platforms, balancing on the edge of the abyss.")
        print("1. Jump to the next platform.")
        print("2. Use a nearby rope to swing to the next platform.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You make a daring jump and reach the next platform safely.")
        elif choice == "2":
            print("You swing across using the rope, showcasing your agility.")
        else:
            print("Invalid choice! You slip and barely hold on to the platform.")
            print("Game over.")

    def avoid_airship_remnants(self):
        print("As you explore, you encounter remnants of fallen airships.")
        print("1. Navigate carefully around the debris.")
        print("2. Investigate the wreckage for useful items.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You carefully navigate around the airship remnants.")
        elif choice == "2":
            print("You find a hidden compartment with valuable artifacts.")
        else:
            print("Invalid choice! You trigger a hidden trap in the wreckage.")
            print("Game over.")

    def uncover_truth(self):
        print("You reach the heart of the ruins, where a holographic display reveals the city's history.")
        print("1. Examine the holographic display closely.")
        print("2. Activate a console to access archived records.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You discover insights into the city's technological advancements.")
        elif choice == "2":
            print("Accessing the console, you unveil the truth behind the city's fall.")
            print("You have successfully completed the Sky City Ruins Adventure!")
        else:
            print("Invalid choice! The holographic display malfunctions.")
            print("Game over.")

    def play(self):
        print("### Sky City Ruins Adventure ###")
        print("The remnants of a once-floating city are now suspended in the sky, with crumbling skyscrapers and floating debris.")
        print("Adventure: Explore the floating ruins to uncover the history of the city. Navigate floating platforms, solve riddles, and avoid airship remnants. Uncover the truth behind the city's fall.")
        print("You are now in the sky city ruins...\n")

        self.navigate_platforms()
        self.avoid_airship_remnants()
        self.uncover_truth()
if __name__ == "__main__":
    game = SkyCityRuinsGame("kate")
    game.play()