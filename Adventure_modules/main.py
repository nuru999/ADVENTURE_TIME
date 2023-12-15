import sqlite3
from getpass import getpass

# Game modules
from mystry import MysteriousForestGame
from temple import ForgottenTempleGame
from underground import UndergroundCavernsGame
from sky_city import SkyCityRuinsGame

# Database setup
conn = sqlite3.connect('user_game_database.db')
cursor = conn.cursor()

# Create the user, game, and user_game_progress tables if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS User (
        UserID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserName TEXT NOT NULL UNIQUE,
        Password TEXT NOT NULL,
        CurrentGameID INTEGER,
        FOREIGN KEY (CurrentGameID) REFERENCES Game(GameID)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Game (
        GameID INTEGER PRIMARY KEY AUTOINCREMENT,
        GameName TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS UserGameProgress (
        ProgressID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER,
        GameID INTEGER,
        CurrentStage TEXT NOT NULL,
        FOREIGN KEY (UserID) REFERENCES User(UserID),
        FOREIGN KEY (GameID) REFERENCES Game(GameID)
    )
''')
conn.commit()

# cursor.execute('INSERT INTO Game (GameName) VALUES ("Mysterious Forest Adventure")')
# cursor.execute('INSERT INTO Game (GameName) VALUES ("Forgotten Temple Adventure")')
# cursor.execute('INSERT INTO Game (GameName) VALUES ("Underground Caverns Adventure")')
# cursor.execute('INSERT INTO Game (GameName) VALUES ("Sky City Ruins Adventure")')
# conn.commit()

# Initialize the user variable
user = None

# Function to register a new user
def register_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Check if the username already exists
    cursor.execute('SELECT * FROM User WHERE UserName = ?', (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose another.")
        return

    # Insert the new user into the database
    cursor.execute('INSERT INTO User (UserName, Password) VALUES (?, ?)', (username, password))
    conn.commit()
    print("Registration successful!")

# Function to authenticate a user
def authenticate_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    # Check if the username and password match
    cursor.execute('SELECT * FROM User WHERE UserName = ? AND Password = ?', (username, password))
    user = cursor.fetchone()

    if user:
        print("Authentication successful!")
        return user
    else:
        print("Invalid credentials. Please try again.")
        return None

# Function to choose a game
def choose_game():
    print("Choose an adventure game:")
    print("1. Mysterious Forest Adventure")
    print("2. Forgotten Temple Adventure")
    print("3. Underground Caverns Adventure")
    print("4. Sky City Ruins Adventure")
    
    while True:
        try:
            choice = int(input("Enter the number of your chosen adventure game: "))
            cursor.execute('UPDATE User SET CurrentGameID = ? WHERE UserID = ?', (choice, user[0]))
            conn.commit()
            if 1 <= choice <= 4:
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program
while True:
    print("\nWelcome to the Adventure Game Center!")

    # User authentication or registration
    while True:
        action = input("Do you want to [1] login or [2] register? Enter 'q' to quit: ")

        if action == '1':
            user = authenticate_user()
            if user:
                break
        elif action == '2':
            register_user()
        elif action.lower() == 'q':
            conn.close()
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter '1', '2', or 'q'.")

    # User has successfully logged in
    while True:
        # User chooses an adventure game
        game_choice = choose_game()

        # Update the user's current game in the database
        cursor.execute('UPDATE User SET CurrentGameID = ? WHERE UserID = ?', 
                       (game_choice, user[0]))
        conn.commit()

        # Play the chosen adventure game
        if game_choice == 1:
            game = MysteriousForestGame(user)
        elif game_choice == 2:
            game = ForgottenTempleGame(user)
        elif game_choice == 3:
            game = UndergroundCavernsGame(user)
        elif game_choice == 4:
            game = SkyCityRuinsGame(user)
        
        # Play the chosen game
        game.play()
        
        cursor.execute('INSERT INTO UserGameProgress (UserID, GameID, CurrentStage) VALUES (?, ?, ?)',
                       (user[0], game_choice, "Initial Stage"))
        conn.commit()

        # Ask if the user wants to play another adventure game
        play_again = input("Do you want to play another adventure game? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing!")
            conn.close()
            exit()
