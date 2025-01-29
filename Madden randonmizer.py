import random

def get_nfl_teams():
    """Return a set of all 32 NFL teams."""
    return {
        "Arizona Cardinals", "Atlanta Falcons", "Baltimore Ravens", "Buffalo Bills",
        "Carolina Panthers", "Chicago Bears", "Cincinnati Bengals", "Cleveland Browns",
        "Dallas Cowboys", "Denver Broncos", "Detroit Lions", "Green Bay Packers",
        "Houston Texans", "Indianapolis Colts", "Jacksonville Jaguars", "Kansas City Chiefs",
        "Las Vegas Raiders", "Los Angeles Chargers", "Los Angeles Rams", "Miami Dolphins",
        "Minnesota Vikings", "New England Patriots", "New Orleans Saints", "New York Giants",
        "New York Jets", "Philadelphia Eagles", "Pittsburgh Steelers", "San Francisco 49ers",
        "Seattle Seahawks", "Tampa Bay Buccaneers", "Tennessee Titans", "Washington Commanders"
    }

def trade_generator():
    """Handles the trade request scenario for a franchise-tagged player or a player requesting a trade."""
    print("The player has requested a trade!")
    teams = get_nfl_teams()

    # User selects their current team
    user_team = input("Enter the team you are playing for: ").strip()
    if user_team not in teams:
        print("Invalid team name. Please enter a valid NFL team.")
        return

    teams.remove(user_team)  # Remove user's team from trade options

    while True:
        # Generate a random trade destination
        trade_team = random.choice(list(teams))
        print(f"Proposed trade destination: {trade_team}")

        # Ask user if they accept
        accept = input("Do you accept this trade? (yes/no): ").strip().lower()
        if accept == "yes":
            print("Trade confirmed! Program ending.")
            break
        elif accept == "no":
            print("Rerolling new trade destination...\n")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def resign_generator():
    """Handles the decision for a rookie player choosing between an extension, free agency, or requesting a trade."""
    decision = random.choice(["Resign", "Test Free Agency", "Request Trade"])
    
    if decision == "Resign":
        print("The player has accepted a contract extension! Program ending.")
        return
    elif decision == "Test Free Agency":
        print("The player has decided to test free agency!")
    else:
        print("The player has requested a trade!")
        trade_generator()  # Call trade generator instead of free agency
        return

    teams = get_nfl_teams()
    
    # User selects their current team (for removal)
    user_team = input("Enter the team you are playing for: ").strip()
    if user_team not in teams:
        print("Invalid team name. Please enter a valid NFL team.")
        return

    teams.remove(user_team)  # Remove user's team from potential signing destinations

    while True:
        # Generate a random free agency signing
        signing_team = random.choice(list(teams))
        print(f"Free Agency offer from: {signing_team}")

        # Ask user if they accept
        accept = input("Do you accept this offer? (yes/no): ").strip().lower()
        if accept == "yes":
            print("Contract signed! Program ending.")
            break
        elif accept == "no":
            print("Rerolling another offer...\n")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """Main function to let the user choose between the Trade Generator and the Resign Generator."""
    while True:
        choice = input("Do you want the Trade Generator or Resign Generator? (trade/resign): ").strip().lower()
        if choice == "trade":
            trade_generator()
            break
        elif choice == "resign":
            resign_generator()
            break
        else:
            print("Invalid input. Please enter 'trade' or 'resign'.")

if __name__ == "__main__":
    main()
