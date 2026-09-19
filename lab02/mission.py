"""
Name: Kyle Sewell
Course: CIS109
Assignment: Lab 02 - Secret Mission
"""

# Capturing input from the user (Part 1)
agent_name = input("Enter your agent name: ")
agent_age = int(input("Enter your age: "))
years_training = float(input("How many years have you been training? "))
favorite_color = input("Enter your favorite color: ")
gadget_count = int(input("How many gadgets are you carrying? "))
total_minutes = int(input("How many minutes do you have? "))

# Calculations (Part 2)
training_percentage = (years_training / agent_age) * 100
gadgets_per_year = gadget_count / years_training
time_remaining = total_minutes - 7
time_seconds = total_minutes * 60

# String formatting using f-strings and .upper() (Part 3)
mission_code = f"{agent_name.upper()}-{favorite_color.upper()}-{agent_age}"

# Boolean expressions (Part 4)
is_adult = agent_age >= 18
has_many_gadgets = gadget_count >= 5
has_experience = years_training > 0

# Output Briefing (Part 5)
print("====================================")
print("        SECRET MISSION BRIEFING")
print("====================================")
print()
print(f"Agent: {agent_name}")
print(f"Mission Code: {mission_code}")
print()
print(f"Age: {agent_age}")
print(f"Training: {years_training:g} years")
print(f"Training Percentage: {training_percentage:.2f}%")
print()
print(f"Gadgets: {gadget_count}")
print(f"Gadget Density: {gadgets_per_year:.2f} per training year")
print()
print(f"Mission Time: {total_minutes} minutes")
print(f"Mission Time Remaining: {time_remaining} minutes")
print(f"Mission Time in Seconds: {time_seconds}")
print()
print(f"Adult Agent: {is_adult}")
print(f"Many Gadgets: {has_many_gadgets}")
print(f"Training Experience: {has_experience}")
print()
print("====================================")
print("        GOOD LUCK, AGENT!")
print("====================================")