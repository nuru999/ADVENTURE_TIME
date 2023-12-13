from sqlalchemy import Column, Integer, String, create_engine,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
import time

Base = declarative_base()

class Avatar(Base):
    __tablename__ = 'avatars'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    health = Column(Integer, default=100) 
    relics=Column(Integer)
class Riddle(Base):
    __tablename__ = 'riddles'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
class Attacker(Base):
    __tablename__ = 'attackers'
    id = Column(Integer, primary_key=True)
    damage_power = Column(Integer, default=20)
    name = Column(String,unique=True)  # Correct indentation

# ... (rest of your code)


engine = create_engine("sqlite:///game_db.db", echo=True)
# Drop the attackers table (if it exists)
#Avatar.__table__.drop(engine, checkfirst=True)
#Attacker.__table__.drop(engine, checkfirst=True)

# Recreate all tables
Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()

# Sample avatars and riddles
avatar_names =[]# ["Knight", "Wizard", "Elf", "Dwarf"]
attacker_names=[]#["bear","leopard","Lion","Zebra"]
attacker_damages=[]#[30,25,40,15]
riddles_data = [
   # {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "answer": "echo"},
    #{"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
]

# Populate database with avatars and riddles
for name in avatar_names:
    avatar = Avatar(name=name)
    session.add(avatar)
for attacker_name, attacker_damage in zip(attacker_names, attacker_damages):
    attacker = Attacker(name=attacker_name, damage_power=attacker_damage)
    session.add(attacker)
for riddle_data in riddles_data:
    riddle = Riddle(**riddle_data)
    session.add(riddle)
   
session.commit()

def choose_avatar():
    avatars = session.query(Avatar).all()
    print("Choose your avatar:")
    for i, avatar in enumerate(avatars, start=1):
        print(f"{i}. {avatar.name}")

    while True:
        try:
            choice = int(input("Enter the number of your chosen avatar: "))
            if 1 <= choice <= len(avatars):
                return avatars[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def ask_riddle(max_attempts=3):
    for attempt in range(1, max_attempts + 1):
        riddle = session.query(Riddle).order_by(func.random()).first()
        print("Riddle:", riddle.question)
        user_answer = input("Your answer: ").strip().lower()

        if user_answer == riddle.answer:
            print("Congratulations! You solved the riddle.")
            return True
        else:
            print(f"Sorry, the answer was incorrect. Try again. Attempts left: {max_attempts - attempt}")

    
    return False

def play_game(avatar):
    print("Fight a bear and earn a relic or run.")
     # List of possible relic names
    relic_names = ["Sword of Wisdom", "Shield of Valor", "Amulet of Power", "Ring of Luck", "Staff of Mysteries"]
    while True:
        choice = input("Choose an action (1: Run, 2: Fight): ")
        
        if choice == '1':
            time.sleep(20)
            print("You ran away. Game over.")
            break
        elif choice == '2':
            attacker = session.query(Attacker).first()
            print(f"You chose to fight a bear with {avatar.health} health.")
            
            if avatar.health > attacker.damage_power:
                time.sleep(20)
                print("Congratulations! You defeated the bear and earned a random relic.")
                # Add logic to earn a random relic name
                earned_relic_name = random.choice(relic_names)
                avatar.relics = earned_relic_name
                session.commit()
                 # Add a 20-second delay
                
            else:
                time.sleep(20)
                print("You were defeated by the bear. Game over.")
                # Add logic to delete the user from the database
                session.delete(avatar)
                session.commit()
                # Add a 20-second delay
                
            
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Main game logic
chosen_avatar = choose_avatar()
print(f"You've chosen the avatar: {chosen_avatar.name}")

if ask_riddle():
    print("Congratulations! You solved the riddle.")
    play_game(chosen_avatar)
else:
     print("Sorry, you've run out of attempts. Game over.")