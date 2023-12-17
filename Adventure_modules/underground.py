import click
from colorama import init, Fore

init(autoreset=True)
import random

class UndergroundCavernsGame:
    def __init__(self, user):
        self.user = user

    
    def encounter_creatures(self):
        creatures = ["Glowing Worms", "Shadow Bats", "Crystal Spiders"]
        click.echo("\nYou encounter different subterranean creatures.")
    
        for idx, creature in enumerate(creatures, start=1):
            click.echo(f"{idx}. Approach the {creature}")

        choice = click.prompt("\nChoose a creature to approach (1, 2, or 3): ")

        if choice.isdigit() and 1 <= int(choice) <= len(creatures):
            selected_creature = creatures[int(choice) - 1]
            click.echo(f"You approach the {selected_creature}.")

        if selected_creature == "Glowing Worms":
            click.echo(Fore.LIGHTMAGENTA_EX+"\nThe Glowing Worms emit a soft light, revealing a hidden pathway.")
            click.echo(Fore.LIGHTMAGENTA_EX+"You continue your journey with newfound illumination.")
        elif selected_creature == "Shadow Bats":
            click.echo("The Shadow Bats guide you through a secret tunnel.")
            click.echo("You discover a shortcut, bypassing potential dangers.")
        elif selected_creature == "Crystal Spiders":
            click.echo("The Crystal Spiders scatter, revealing a sparkling crystal cache.")
            click.echo("You collect valuable crystals and continue your quest.")
        else:
            click.echo("Invalid choice! The creatures become agitated.")
            click.echo("Game over.")
    def play(self):
        click.echo( Fore.CYAN+"\n             Underground Caverns Adventure ###")
        click.echo(Fore.LIGHTMAGENTA_EX+"A vast network of dark and winding caverns beneath the earth's surface, illuminated only by the glow of bioluminescent fungi.")
        click.echo(Fore.LIGHTMAGENTA_EX+"Adventure: Search for a lost civilization's underground city. Encounter subterranean creatures, solve riddles to open pathways, and discover the secrets of the hidden city.")
        click.echo(Fore.CYAN+"\nYou are now in the underground caverns...\n")

        self.encounter_creatures()
        click.echo("\nYou continue your journey through the underground caverns.")
        click.echo("Solve the riddle to gain access to the passage...")
        answer = click.prompt("What has cities, but no houses; forests, but no trees; and rivers, but no water? ")
        
        if answer.lower() == "map":
            click.echo(Fore.CYAN +"Correct! You have successfully completed the Underground Caverns Adventure!")
        else:
            click.echo("Incorrect! The creature blocks your path.")
            click.echo(Fore.GREEN+"Game over.")
if __name__ == "__main__":
    game = UndergroundCavernsGame("mary")
    game.play()