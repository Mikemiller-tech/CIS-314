import random
import tkinter as tk
from tkinter import messagebox, simpledialog

def franchise_decision():
    return random.choice(["Play", "Request Trade"])

def get_nfl_teams():
    return {
        "Cardinals", "Falcons", "Ravens", "Bills",
        "Panthers", "Bears", "Bengals", "Browns",
        "Cowboys", "Broncos", "Lions", "Packers",
        "Texans", "Colts", "Jaguars", "Chiefs",
        "Raiders", "Chargers", "Rams", "Dolphins",
        "Vikings", "Patriots", "Saints", "Giants",
        "Jets", "Eagles", "Pittsburgh", "49ers",
        "Seahawks", "Buccaneers", "Titans", "Commanders"
    }

def trade_simulation_gui():
    teams = get_nfl_teams()
    root = tk.Tk(); root.withdraw()
    user_team = simpledialog.askstring("Your Team", "Enter the team you are playing for:")
    if not user_team or user_team.strip() not in teams:
        messagebox.showerror("Invalid Team", "Invalid team name. Please restart.")
        return
    teams.remove(user_team.strip())

    while teams:
        trade_team = random.choice(list(teams))
        ans = messagebox.askquestion(
            "Trade Offer",
            f"Proposed trade destination: {trade_team}\nDo you accept this trade?"
        )
        if ans == "yes":
            messagebox.showinfo("Trade Complete", f"Trade to {trade_team} confirmed!")
            return
        teams.remove(trade_team)

    messagebox.showinfo("No Trades", "No more teams left to trade to. Trade request failed.")

def rookie_deal_simulation():
    root = tk.Tk(); root.withdraw()
    position = simpledialog.askstring(
        "Position",
        "What position do you play? (QB, RB, WR, CB, LB, DT, OL)"
    )
    if not position:
        messagebox.showerror("Error", "Position not entered.")
        return

    pos = position.strip().upper()
    stats = {}

    # Gather stats based on position
    if pos == "QB":
        stats["Passing Yards"]   = simpledialog.askinteger("Stat", "Enter passing yards:")
        stats["Touchdowns"]      = simpledialog.askinteger("Stat", "Enter number of touchdowns:")
        stats["Interceptions"]   = simpledialog.askinteger("Stat", "Enter number of interceptions:")

    elif pos == "RB":
        stats["Rushing Yards"]   = simpledialog.askinteger("Stat", "Enter rushing yards:")
        stats["Touchdowns"]      = simpledialog.askinteger("Stat", "Enter number of touchdowns:")
        stats["Fumbles"]         = simpledialog.askinteger("Stat", "Enter number of fumbles:")

    elif pos == "WR":
        stats["Receiving Yards"] = simpledialog.askinteger("Stat", "Enter receiving yards:")
        stats["Touchdowns"]      = simpledialog.askinteger("Stat", "Enter number of touchdowns:")
        stats["Drops"]           = simpledialog.askinteger("Stat", "Enter number of drops:")

    elif pos == "CB":
        stats["Interceptions"]   = simpledialog.askinteger("Stat", "Enter number of interceptions:")
        stats["Pass Breakups"]   = simpledialog.askinteger("Stat", "Enter number of pass breakups:")
        stats["Tackles"]         = simpledialog.askinteger("Stat", "Enter number of tackles:")

    elif pos == "LB":
        stats["Tackles"]     = simpledialog.askinteger("Stat", "Enter number of tackles:")
        stats["Interceptions"] = simpledialog.askinteger("Stat", "Enter number of interceptions:")
        stats["TFL"]         = simpledialog.askinteger("Stat", "Enter tackles for loss:")
        stats["Sacks"]       = simpledialog.askfloat("Stat", "Enter number of sacks:")

    elif pos == "DT":
        stats["Sacks"]       = simpledialog.askfloat("Stat", "Enter number of sacks:")
        stats["TFL"]         = simpledialog.askinteger("Stat", "Enter tackles for loss:")

    elif pos == "OL":  # Offensive Lineman
        stats["Sacks Allowed"] = simpledialog.askfloat("Stat", "Enter sacks allowed (can be 0.5, etc):")
        stats["Pancakes"]      = simpledialog.askinteger("Stat", "Enter pancake blocks:")

    else:
        messagebox.showinfo("Unknown Position", "We'll accept basic performance stats.")
        stats["Games Played"] = simpledialog.askinteger("Stat", "Enter number of games played:")
        stats["Overall Grade"]= simpledialog.askinteger("Stat", "Enter your performance rating (1-100):")

    # Randomly decide: contract or trade
    final_decision = random.choice(["Contract", "Trade"])
    if final_decision == "Trade":
        messagebox.showinfo("Trade Requested", "You’ve requested a trade!")
        return trade_simulation_gui()

    # Evaluate performance
    performance = "Poor"
    if pos == "QB":
        y, t = stats.get("Passing Yards",0), stats.get("Touchdowns",0)
        if y > 4000 and t > 30: performance="Great"
        elif y > 3000 and t > 20: performance="Okay"
    elif pos == "RB":
        y, t = stats.get("Rushing Yards",0), stats.get("Touchdowns",0)
        if y > 1300 and t > 12: performance="Great"
        elif y > 800  and t > 6: performance="Okay"
    elif pos == "WR":
        y, t = stats.get("Receiving Yards",0), stats.get("Touchdowns",0)
        if y > 1200 and t > 10: performance="Great"
        elif y > 700  and t > 5: performance="Okay"
    elif pos == "CB":
        p = stats.get("Interceptions",0)
        if p > 5: performance="Great"
        elif p > 2: performance="Okay"
    elif pos == "LB":
        tkls, sks = stats.get("Tackles",0), stats.get("Sacks",0)
        if tkls > 90 and sks > 6: performance="Great"
        elif tkls > 60 and sks > 3: performance="Okay"
    elif pos == "DT":
        sks, tfl = stats.get("Sacks",0), stats.get("TFL",0)
        if sks > 7 and tfl > 9: performance="Great"
        elif sks > 4 and tfl > 5: performance="Okay"
    elif pos == "OL":
        sa = stats.get("Sacks Allowed", 0.0)
        if sa <= 5:
            performance = "Great"
        elif sa <= 10:
            performance = "Okay"
        else:
            performance = "Poor"

    # Ask for overall rating and age
    ovr = simpledialog.askinteger("Overall Rating", "Enter your player OVR (0–100):")
    age = simpledialog.askinteger("Age", "Enter your age:")

    # Base salary & bonus by performance
    if performance == "Great":
        base_salary, base_bonus = 20_000_000, 8_000_000
    elif performance == "Okay":
        base_salary, base_bonus = 12_000_000, 4_000_000
    else:
        base_salary, base_bonus =  6_000_000, 1_000_000

    # Adjust by OVR
    if ovr >= 90:
        base_salary += 4_000_000; base_bonus += 2_000_000
    elif ovr >= 80:
        base_salary += 2_000_000; base_bonus += 1_000_000
    elif ovr <= 65:
        base_salary -= 1_000_000; base_bonus -=   500_000

    # Adjust by age
    if age <= 25:
        base_salary += 2_000_000; base_bonus += 1_000_000
    elif age >= 30:
        base_salary -= 2_000_000; base_bonus -= 1_000_000

    # Enforce minimums
    base_salary = max(base_salary, 1_000_000)
    base_bonus  = max(base_bonus, 0)

    # Contract length: start from performance, then tweak by OVR & age
    if performance == "Great":
        years = 4
    elif performance == "Okay":
        years = 3
    else:
        years = 2

    if ovr >= 90:    years += 1
    if age <= 25:    years += 1
    if age >= 32:    years -= 1

    contract_years = max(1, min(years, 5))

    # Format outputs
    contract_salary = f"${base_salary // 1_000_000}M/year"
    contract_bonus  = f"${base_bonus  // 1_000_000}M signing bonus"
    contract_length = f"{contract_years} year{'s' if contract_years > 1 else ''}"

    # Show contract
    messagebox.showinfo(
        "Contract Offer",
        f"Stats: {stats}\n"
        f"Performance: {performance}\n"
        f"OVR: {ovr} | Age: {age}\n\n"
        f"Suggested Contract:\n"
        f" • Salary: {contract_salary}\n"
        f" • Bonus:  {contract_bonus}\n"
        f" • Length: {contract_length}"
    )

def start_franchise_path_gui():
    if franchise_decision() == "Play":
        messagebox.showinfo("Decision", "Staying under franchise tag – program ends.")
    else:
        messagebox.showinfo("Decision", "Requesting trade!")
        trade_simulation_gui()

def start_rookie_path_gui():
    rookie_deal_simulation()

def gui_start():
    root = tk.Tk()
    root.title("NFL Player Path Selection")
    root.geometry("400x300")
    root.configure(bg="#1E90FF")

    frame = tk.Frame(root, bg="#1E90FF")
    frame.pack(expand=True)

    tk.Label(frame, text="Choose your path", font=("Arial",18,"bold"),
             bg="#1E90FF", fg="white").pack(pady=20)

    tk.Button(frame, text="Franchise Tag Method",
              command=lambda: [root.destroy(), start_franchise_path_gui()],
              width=30, height=2, bg="#FFD700", fg="black",
              font=("Arial",12,"bold")).pack(pady=10)

    tk.Button(frame, text="Rookie Deal Method",
              command=lambda: [root.destroy(), start_rookie_path_gui()],
              width=30, height=2, bg="#32CD32", fg="white",
              font=("Arial",12,"bold")).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    gui_start()
