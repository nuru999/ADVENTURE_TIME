import click
from colorama import init, Fore

init(autoreset=True)
class SkyCityRuinsGame:
    def __init__(self, user):
        self.user = user

    def navigate_platforms(self):
        click.echo("\nYou navigate through floating platforms, balancing on the edge of the abyss.")
        click.echo(Fore.LIGHTYELLOW_EX+"1. Jump to the next platform.")
        click.echo(Fore.LIGHTYELLOW_EX+"2. Use a nearby rope to swing to the next platform.")
        choice = click.prompt("\nChoose your action (1 or 2): ")

        if choice == "1":
            click.echo("\nYou make a daring jump and reach the next platform safely.")
        elif choice == "2":
            click.echo("\nYou swing across using the rope, showcasing your agility.")
        else:
            click.echo("Invalid choice! You slip and barely hold on to the platform.")
            click.echo(Fore.GREEN+"Game over.")

    def avoid_airship_remnants(self):
        click.echo("\nAs you explore, you encounter remnants of fallen airships.")
        click.echo(Fore.LIGHTYELLOW_EX+"1. Navigate carefully around the debris.")
        click.echo(Fore.LIGHTYELLOW_EX+"2. Investigate the wreckage for useful items.")
        choice = click.prompt("Choose your action (1 or 2): ")

        if choice == "1":
            click.echo("\nYou carefully navigate around the airship remnants.")
        elif choice == "2":
            click.echo("\nYou find a hidden compartment with valuable artifacts.")
        else:
            click.echo("Invalid choice! You trigger a hidden trap in the wreckage.")
            click.echo(Fore.GREEN+"Game over.")

    def uncover_truth(self):
        click.echo("\nYou reach the heart of the ruins, where a holographic display reveals the city's history.")
        click.echo(Fore.LIGHTYELLOW_EX+"1. Examine the holographic display closely.")
        click.echo("2. Activate a console to access archived records.")
        choice = click.prompt("Choose your action (1 or 2): ")

        if choice == "1":
            click.echo("\nYou discover insights into the city's technological advancements.")
        elif choice == "2":
            click.echo("\nAccessing the console, you unveil the truth behind the city's fall.")
            click.echo("You have successfully completed the Sky City Ruins Adventure!")
        else:
            click.echo("Invalid choice! The holographic display malfunctions.")
            click.echo(Fore.GREEN+"Game over.")

    def play(self):
        click.echo(Fore.CYAN+"\n             Sky City Ruins Adventure          ")
        click.echo(Fore.LIGHTMAGENTA_EX+"The remnants of a once-floating city are now suspended in the sky, with crumbling skyscrapers and floating debris.")
        click.echo(Fore.LIGHTMAGENTA_EX+"\nAdventure: Explore the floating ruins to uncover the history of the city. Navigate floating platforms, solve riddles, and avoid airship remnants. Uncover the truth behind the city's fall.")
        click.echo(Fore.CYAN+"You are now in the sky city ruins...\n")

        self.navigate_platforms()
        self.avoid_airship_remnants()
        self.uncover_truth()
if __name__ == "__main__":
    game = SkyCityRuinsGame("kate")
    game.play()

