import random

class UndergroundCavernsGame:
    def __init__(self, user):
        self.user = user

    
    def encounter_creatures(self):
        creatures = ["Glowing Worms", "Shadow Bats", "Crystal Spiders"]
        print("\nYou encounter different subterranean creatures.")
    
        for idx, creature in enumerate(creatures, start=1):
            print(f"{idx}. Approach the {creature}")

        choice = input("\nChoose a creature to approach (1, 2, or 3): ")

        if choice.isdigit() and 1 <= int(choice) <= len(creatures):
            selected_creature = creatures[int(choice) - 1]
            print(f"You approach the {selected_creature}.")

        if selected_creature == "Glowing Worms":
            print("\nThe Glowing Worms emit a soft light, revealing a hidden pathway.")
            print("You continue your journey with newfound illumination.")
        elif selected_creature == "Shadow Bats":
            print("The Shadow Bats guide you through a secret tunnel.")
            print("You discover a shortcut, bypassing potential dangers.")
        elif selected_creature == "Crystal Spiders":
            print("The Crystal Spiders scatter, revealing a sparkling crystal cache.")
            print("You collect valuable crystals and continue your quest.")
        else:
            print("Invalid choice! The creatures become agitated.")
            print("Game over.")
    def play(self):
        print("\n             Underground Caverns Adventure ###")
        print("A vast network of dark and winding caverns beneath the earth's surface, illuminated only by the glow of bioluminescent fungi.")
        print("Adventure: Search for a lost civilization's underground city. Encounter subterranean creatures, solve riddles to open pathways, and discover the secrets of the hidden city.")
        print("\nYou are now in the underground caverns...\n")

        self.encounter_creatures()
        print("\nYou continue your journey through the underground caverns.")
        print("Solve the riddle to gain access to the passage...")
        answer = input("What has cities, but no houses; forests, but no trees; and rivers, but no water? ")
        
        if answer.lower() == "map":
            print("Correct! You have successfully completed the Underground Caverns Adventure!")
        else:
            print("Incorrect! The creature blocks your path.")
            print("Game over.")
if __name__ == "__main__":
    game = UndergroundCavernsGame("mary")
    game.play()