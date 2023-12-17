import click
from colorama import init, Fore

init(autoreset=True)
class ForgottenTempleGame:
    def __init__(self, user):
        self.user = user

    def avoid_traps(self):
        click.echo("\nAs you progress deeper into the temple, you encounter a hallway filled with hidden traps.")
        click.echo(Fore.LIGHTYELLOW_EX+"\n1. Navigate carefully, avoiding pressure plates and tripwires.")
        click.echo(Fore.LIGHTYELLOW_EX+"2. Attempt to disarm the traps using your knowledge of ancient mechanisms.")
        choice = click.prompt("Choose your action (1 or 2): ")

        if choice == "1":
            click.echo("\nYou skillfully navigate through the traps, avoiding any danger.")
        elif choice == "2":
            click.echo("\nYou attempt to disarm the traps, but one gets triggered.")
            click.echo("Quick reflexes save you from a dangerous fall.")
        else:
            click.echo("Invalid choice! You trigger a trap, and the chamber shakes.")
            click.echo(Fore.GREEN+"Game over.")

    def inner_sanctum(self):
        click.echo("\nYou reach the inner sanctum, a chamber filled with an aura of ancient power.")
        click.echo(Fore.LIGHTMAGENTA_EX+"1. Approach the relic with caution.")
        click.echo(Fore.LIGHTMAGENTA_EX+"2. Examine the surroundings for hidden clues.")
        choice = click.prompt("Choose your action (1 or 2): ")

        if choice == "1":
            click.echo("\nYou approach the relic with caution, revealing its true power.")
            click.echo(Fore.GREEN+"Congratulations! You have successfully completed the Forgotten Temple Adventure!")
        elif choice == "2":
            click.echo("\nYou examine the surroundings and discover a hidden passage.")
            click.echo("The passage leads to the relic without triggering any traps.")
            click.echo(Fore.GREEN+"\nCongratulations! You have successfully completed the Forgotten Temple Adventure!")
        else:
            click.echo("Invalid choice! The relic's power reacts to your indecision.")
            click.echo(Fore.GREEN+"Game over.")

    def play(self):
        click.echo(Fore.CYAN+"\n             Forgotten Temple Adventure              ")
        click.echo(Fore.LIGHTMAGENTA_EX+"\nA crumbling temple hidden deep in the mountains, filled with forgotten treasures, and guarded by ancient traps.")
        click.echo(Fore.LIGHTMAGENTA_EX+"Adventure: Navigate through the temple's chambers, decipher inscriptions, and avoid traps to reach the inner sanctum where a powerful relic awaits.")
        click.echo(Fore.CYAN+"You are now in the forgotten temple...\n")

        self.avoid_traps()
        self.inner_sanctum()
if __name__ == "__main__":
    game = ForgottenTempleGame("amina")
    game.play()