# Smoking Money Saved Calculator

# Variables to store user input
cigarettes_per_day = 0
cost_per_pack = 0
cigarettes_per_pack = 0
days_not_smoked = 0

# Function to calculate money saved
def calculate_savings():
    cigarettes_not_smoked = cigarettes_per_day * days_not_smoked
    packs_not_bought = cigarettes_not_smoked / cigarettes_per_pack
    money_saved = packs_not_bought * cost_per_pack
    return money_saved

# Main program
print("Welcome to the Smoking Money Saved Calculator!")

# Get user input
cigarettes_per_day = int(input("How many cigarettes did you smoke per day? "))
cost_per_pack = float(input("What's the cost of a pack of cigarettes? "))
cigarettes_per_pack = int(input("How many cigarettes are in a pack? "))
days_not_smoked = int(input("How many days have you not smoked? "))

# Calculate and display savings
savings = calculate_savings()
print(f"You've saved ${savings:.2f} by not smoking for {days_not_smoked} days!")
