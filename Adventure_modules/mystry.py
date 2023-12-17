import click
from colorama import init, Fore

init(autoreset=True)
class MysteriousForestGame:
    def __init__(self, user):
        self.user = user

    def explore_forest(self):
        click.echo("As you venture deeper into the mysterious forest, you come across ancient trees and hidden pathways.")
        click.echo(Fore.LIGHTYELLOW_EX+"\n1. Follow a faint trail to the east.")
        click.echo(Fore.LIGHTYELLOW_EX+"2. Climb a massive tree to get a better view.")
        choice = click.prompt(Fore.LIGHTMAGENTA_EX+"\nChoose your action (1 or 2): ")

        if choice == "1":
            click.echo(Fore.CYAN+"\nYou follow the trail and discover a hidden clearing.")
        elif choice == "2":
            click.echo(Fore.CYAN+"\nClimbing the tree, you spot a glimmer in the distance.")
        else:
            print(Fore.LIGHTRED_EX+"Invalid choice! You stumble upon a mystical creature's nest.")
            print(Fore.GREEN+"Game over.")

    def find_artifact(self):
        click.echo("\nIn the hidden clearing, you find an ancient pedestal with a concealed compartment.")
        click.echo(Fore.LIGHTYELLOW_EX+"\n1. Open the compartment to reveal the hidden artifact.")
        click.echo(Fore.LIGHTYELLOW_EX+"2. Examine the surroundings for any potential dangers.")
        choice = click.prompt("\nChoose your action (1 or 2): ")

        if choice == "1":
            click.echo("You open the compartment and unveil the hidden artifact.")
            click.echo(Fore.GREEN+"Congratulations! You have successfully completed the Mysterious Forest Adventure!")
        elif choice == "2":
            click.echo("\nYou cautiously examine the surroundings and find no immediate dangers.")
            click.echo("\nYou open the compartment and unveil the hidden artifact.")
            click.echo(Fore.GREEN+"Congratulations! You have successfully completed the Mysterious Forest Adventure!")
        else:
            click.echo(Fore.LIGHTRED_EX+"Invalid choice! The mystical energy surrounding the artifact reacts unpredictably.")
            click.echo(Fore.GREEN+"Game over.")

    def play(self):
        click.echo(Fore.CYAN+"\n            Mysterious Forest Adventure               ")
        click.echo(Fore.LIGHTMAGENTA_EX+ "\nA dense, ancient forest cloaked in mist and mystery.")
        click.echo(Fore.LIGHTMAGENTA_EX+"Adventure: Explore the forest to find a hidden artifact.")
        click.echo(Fore.LIGHTMAGENTA_EX+"Encounter mystical creatures and solve riddles to unlock the artifact's location.")
        click.echo(Fore.CYAN+"\nYou are now in the mysterious forest...\n")

        self.explore_forest()
        self.find_artifact()
if __name__ == "__main__":
    game = MysteriousForestGame(["alex", "john"])
    game.play()

