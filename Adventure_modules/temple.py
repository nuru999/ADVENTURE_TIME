
class ForgottenTempleGame:
    def __init__(self, user):
        self.user = user

    def avoid_traps(self):
        print("As you progress deeper into the temple, you encounter a hallway filled with hidden traps.")
        print("1. Navigate carefully, avoiding pressure plates and tripwires.")
        print("2. Attempt to disarm the traps using your knowledge of ancient mechanisms.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You skillfully navigate through the traps, avoiding any danger.")
        elif choice == "2":
            print("You attempt to disarm the traps, but one gets triggered.")
            print("Quick reflexes save you from a dangerous fall.")
        else:
            print("Invalid choice! You trigger a trap, and the chamber shakes.")
            print("Game over.")

    def inner_sanctum(self):
        print("You reach the inner sanctum, a chamber filled with an aura of ancient power.")
        print("1. Approach the relic with caution.")
        print("2. Examine the surroundings for hidden clues.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You approach the relic with caution, revealing its true power.")
            print("Congratulations! You have successfully completed the Forgotten Temple Adventure!")
        elif choice == "2":
            print("You examine the surroundings and discover a hidden passage.")
            print("The passage leads to the relic without triggering any traps.")
            print("Congratulations! You have successfully completed the Forgotten Temple Adventure!")
        else:
            print("Invalid choice! The relic's power reacts to your indecision.")
            print("Game over.")

    def play(self):
        print("### Forgotten Temple Adventure ###")
        print("A crumbling temple hidden deep in the mountains, filled with forgotten treasures, and guarded by ancient traps.")
        print("Adventure: Navigate through the temple's chambers, decipher inscriptions, and avoid traps to reach the inner sanctum where a powerful relic awaits.")
        print("You are now in the forgotten temple...\n")

        self.avoid_traps()
        self.inner_sanctum()
if __name__ == "__main__":
    game = ForgottenTempleGame("amina")
    game.play()