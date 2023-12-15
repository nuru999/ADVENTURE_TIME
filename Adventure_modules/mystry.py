class MysteriousForestGame:
    def __init__(self, user):
        self.user = user

    def explore_forest(self):
        print("As you venture deeper into the mysterious forest, you come across ancient trees and hidden pathways.")
        print("1. Follow a faint trail to the east.")
        print("2. Climb a massive tree to get a better view.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You follow the trail and discover a hidden clearing.")
        elif choice == "2":
            print("Climbing the tree, you spot a glimmer in the distance.")
        else:
            print("Invalid choice! You stumble upon a mystical creature's nest.")
            print("Game over.")

    def find_artifact(self):
        print("In the hidden clearing, you find an ancient pedestal with a concealed compartment.")
        print("1. Open the compartment to reveal the hidden artifact.")
        print("2. Examine the surroundings for any potential dangers.")
        choice = input("Choose your action (1 or 2): ")

        if choice == "1":
            print("You open the compartment and unveil the hidden artifact.")
            print("Congratulations! You have successfully completed the Mysterious Forest Adventure!")
        elif choice == "2":
            print("You cautiously examine the surroundings and find no immediate dangers.")
            print("You open the compartment and unveil the hidden artifact.")
            print("Congratulations! You have successfully completed the Mysterious Forest Adventure!")
        else:
            print("Invalid choice! The mystical energy surrounding the artifact reacts unpredictably.")
            print("Game over.")

    def play(self):
        print("### Mysterious Forest Adventure ###")
        print("A dense, ancient forest cloaked in mist and mystery.")
        print("Adventure: Explore the forest to find a hidden artifact.")
        print("Encounter mystical creatures and solve riddles to unlock the artifact's location.")
        print("You are now in the mysterious forest...\n")

        self.explore_forest()
        self.find_artifact()
if __name__ == "__main__":
    game = MysteriousForestGame(["alex", "john"])
    game.play()

