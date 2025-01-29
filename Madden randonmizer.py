import random

def franchise_decision():
    """Randomly decide if a player stays under the franchise tag or requests a trade."""
    return random.choice(["Play", "Request Trade"])

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

def trade_simulation():
    """Handle the trade request scenario."""
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

def main():
    """Main function to run the simulation."""
    decision = franchise_decision()
    if decision == "Play":
        print("The player will stay under the franchise tag. Program ending.")
    else:
        print("The player has requested a trade!")
        trade_simulation()

if __name__ == "__main__":
    main()
