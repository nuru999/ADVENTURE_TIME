import random
import click

class Avatar:
    def __init__(self, name, health_points, damage_points):
        self.name = name
        self.health_points = health_points
        self.damage_points = damage_points

    def is_alive(self):
        return self.health_points > 0

    def increase_health(self, amount):
        self.health_points += amount

    def receive_damage(self, amount):
        self.health_points -= amount

class PowerfulRelic:
    def __init__(self, name, health_points, damage_points):
        self.name = name
        self.health_points = health_points
        self.damage_points = damage_points

    def is_alive(self):
        return self.health_points > 0

    def receive_damage(self, amount):
        self.health_points -= amount

class ForgottenTempleAdventure:
    def __init__(self):
        self.description = "A crumbling temple hidden deep in the mountains, filled with forgotten treasures, and guarded by ancient traps."
        self.inscriptions_pool = [
            "Hello from the other side",
            "Cold enough to chill my bones",
            "Change gon come, oooh yes it will",
            "i will love you unconditionally",
            "That one na lie, I dey for you my friend",
            "But you put on quite a show (Ooh, oh)Really had me going",
            "Then you're left in the dust Unless I stuck by ya",
            "I get like this every time On these days that feel like you and me",
            "im so excited its already weekend!",
            "Colouring this life like it's all in crayons"
            
        ]
        self.inscription_solutions =  {
            "Hello from the other side": "Hello",
            "Cold enough to chill my bones": "Cold",
            "Change gon come, oooh yes it will": "A Change Is Gonna Come",
            "i will love you unconditionally": "Unconditionally",
            "That one na lie, I dey for you my friend": "How are you my friend",
            "But you put on quite a show (Ooh, oh)Really had me going": "Take a Bow",
            "Then you're left in the dust Unless I stuck by ya": "Sunflower",
            "I get like this every time On these days that feel like you and me": "Heartbreak anniversary",
            "That girl is a real crowd pleaser Small world, all her friends know me": "Black beetles",
            "Colouring this life like it's all in crayons": "Colouring This Life",
}

        self.selected_inscription = ""
        self.player = Avatar(name="Babji", health_points=100, damage_points=20)
        self.powerful_relic = PowerfulRelic(name="Titan", health_points=150, damage_points=15)

    def start_adventure(self):
        click.echo("Welcome to the Forgotten Temple Adventure!")
        click.echo("You are an adventurer seeking the hidden treasures of a forgotten temple.")
        click.echo("You have two challenges ahead")
        click.echo("Let the adventure begin!")
        self.selected_inscription = random.choice(self.inscriptions_pool)
        
        self.decipher_inscriptions()

    def get_adventure_description(self):
        return f"Navigate through the temple's chambers, decipher cryptic inscriptions, and avoid traps to reach the inner sanctum where a powerful relic, {self.powerful_relic.name}, awaits.\nInscription: {self.selected_inscription}"

    def decipher_inscriptions(self):
        click.echo("\n--- Decipher the Lyric ---")
        click.echo(f"\tYou hear a lyric:\n\t\"{self.selected_inscription}\"")

        for attempt in range(3):
            player_input = click.prompt(f"Attempt {attempt + 1} What is the title of this song? ")

            if self.check_solution(player_input):
                click.echo("Congratulations! You've deciphered the lyrics.")
                self.player.increase_health(10)
                click.echo(f"You earned 10 health points. Current Health: {self.player.health_points}")
                self.battle()
                break
            else:
                click.echo("Incorrect answer. Try again.")

        else:
            # Notify the user of the correct answer after three failed attempts
            click.echo(f"Out of attempts! The correct answer was: {self.inscription_solutions[self.selected_inscription]}")
            click.echo("The meaning eludes you for now. Keep exploring.")
            

    def check_solution(self, player_input):
        expected_solution = self.inscription_solutions[self.selected_inscription]
        return player_input.lower() == expected_solution.lower()

    def battle(self):
        click.echo("\n--- LET THE BATTLE BEGIN!!!! ---")
        click.echo(f"You encounter the Powerful Relic, {self.powerful_relic.name}!")

        while self.player.is_alive() and self.powerful_relic.is_alive():
            click.echo(f"\n{self.player.name}'s Health: {self.player.health_points}")
            click.echo(f"{self.powerful_relic.name}'s Health: {self.powerful_relic.health_points}")

            action = click.prompt("Choose an action (attack/defend/run)").lower()

            if action == "attack":
                self.attack(self.player, self.powerful_relic)
                self.attack(self.powerful_relic, self.player)
            elif action == "defend":
                self.defend(self.player)
                self.attack(self.powerful_relic, self.player)
            elif action == "run":
                click.echo(f"{self.player.name} managed to escape the battle.")
                break
            else:
                click.echo("Invalid action. Try again.")

        if self.player.is_alive():
            click.echo(f"Congratulations! You defeated {self.powerful_relic.name} and completed the adventure.")
        else:
            click.echo(f"{self.player.name} has been defeated. Game over.")

    def attack(self, attacker, target):
        damage_dealt = random.randint(attacker.damage_points // 2, attacker.damage_points)
        target.receive_damage(damage_dealt)
        click.echo(f"{attacker.name} dealt {damage_dealt} damage to {target.name}!")

    def defend(self, player):
        player.increase_health(5)
        click.echo(f"{player.name} chose to defend. Health increased by 5. Current Health: {player.health_points}")

@click.command()
def play_forgotten_temple():
    forgotten_temple = ForgottenTempleAdventure()
    forgotten_temple.start_adventure()

if __name__ == "__main__":
    play_forgotten_temple()
