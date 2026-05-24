import json
from coffee_data import COFFEE_DATA, RECOMMENDATION_MAP
from datetime import datetime
history = []
total_caffeine = 0

#Displays the main menu and handles user navigation.
def main_menu():
    while True:
        print("Welcome to BrewMood ₍˄·͈༝·͈˄*₎◞ ̑̑")
        print("What do you want today?")
        print("1. Start a test")
        print("2. Log a Drink")
        print("3. View history")
        print("4. Check caffeine level")
        print("5. Reset Today's Records")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            brewmood_test_flow()  
        elif choice == "2":
            manual_log()
        elif choice == "3":
            view_history()
        elif choice == "4":
            caffeine_warning()
        elif choice == "5":
            reset_today()
        elif choice == "6":
            print("Goodbye! Enjoy your day:)")
            break
        else:
            print("Invalid option. Please choose 1-6.")
            continue

#Runs the complete recommendation test flow(mood and personality)
def brewmood_test_flow():
    while True:
        current_mood = choose_mood()
        coffee_personality = personality_test()

        try:
            # generate the recommendation
            coffee, caffeine, kaomoji, description = recommend_coffee(
                current_mood,
                coffee_personality
        )
        # use exception handling to hand missing recommendation errors
        except ValueError as error:
            print(error)
            continue

        next_action = after_test()
        if next_action == "log":
           log_coffee(coffee, caffeine, current_mood)
           break
           
        elif next_action == "retake":
            continue

        elif next_action == "menu":
            break

# select the current mood
def choose_mood():

    while True:

        print("\nChoose your current mood:")
        print("1. Tired (－_－) zzZ")
        print("2. Stressed (＠_＠;)")
        print("3. Calm ( ˶ˆᗜˆ˵ )")
        print("4. Energetic ✧(•̀ᴗ•́)و")

        mood_choice = input("Choose an option: ")

        if mood_choice == "1":
            print("Your current mood is: tired (－_－) zzZ")
            return "tired"

        elif mood_choice == "2":
            print("Your current mood is: stressed (＠_＠;)")
            return "stressed"

        elif mood_choice == "3":
            print("Your current mood is: calm ( ˶ˆᗜˆ˵ )")
            return "calm"

        elif mood_choice == "4":
            print("Your current mood is: energetic ✧(•̀ᴗ•́)و")
            return "energetic"
       
       # to prevent user from inputing invalid option
        else:
            print("Invalid option. Please choose 1-4.")
            continue

# yes or no question to determine the user's coffee personality
def personality_test():

    score = 0
    print("\n=== Coffee Personality Test ===")
    print("\nPlease answer yes or no based on your situation ⸜₍๑•⌔•๑₎")

    answer1 = input("\n1. Do you like sweet drinks? ").lower()
    if answer1 == "yes":
        score += 2
    elif answer1 == "no":
        score += 0
    else:
            print("Invalid answer(`3´)! This question will be skipped.")
    
    answer2 = input("2. Do you prefer strong coffee? ").lower()
    if answer2 == "yes":
        score+=3
    elif answer2 == "no":
        score+=0
    else:
        print("Invalid answer(`3´)! This question will be skipped.")
    
    answer3 = input("3. Do you usually stay up late? ").lower()
    if answer3 == "yes":
        score+=2
    elif answer3 == "no":
        score+=0
    else:
        print("Invalid answer(`3´)! This question will be skipped.")
    
    answer4 = input("4. Do you like a calm and cozy cafe atmosphere? ").lower()
    if answer4 == "yes":
        score -= 1
    elif answer4 == "no":
        score+=1
    else:
        print("Invalid answer(`3´)! This question will be skipped.")

    if score<=1:
        personality = "soft"
    elif score<=4:
        personality = "balanced"
    else:
        personality = "intense"
    
    print(f"\nYour coffee personality is: {personality}")

    return personality

# recommendation system based on mood and personality
def recommend_coffee(current_mood, coffee_personality):
    key = (current_mood, coffee_personality)

# raise an error if the recommendation does not exist
    if key not in RECOMMENDATION_MAP:
        raise ValueError("No coffee recommendation foundヽ(・×・´)ゞ")

# get the name from the recomendation_map
    coffee = RECOMMENDATION_MAP[key]

# access the details about the selected coffee from the coffee_data
    coffee_info = COFFEE_DATA[coffee]

# extract details from coffee_data
    caffeine = coffee_info["caffeine"]
    kaomoji = coffee_info["kaomoji"]
    description = coffee_info["description"]

    print("\n=== Your BrewMood Recommendation ===")
    print(f"Recommended coffee: {coffee}")
    print(f"Caffeine: {caffeine} mg")
    print(f"Description: {description} {kaomoji}")
#return all the recommendation result
    return coffee, caffeine, kaomoji, description

# after the recommendation the user can choose what to do next
def after_test():
    while True:
        print("\nWhat would you like to do next?")
        print("1. Log this coffee")
        print("2. Retake the test")
        print("3. Return to main menu")

        choice = input("Choose an option: ")
        if choice == "1":
            return "log"
        
        elif choice == "2":
            return "retake"

        elif choice == "3":
            return "menu"
        
        else:
            print("Invalid option. Please choose 1-3.")
            continue

# Log a drink into history and update the caffeine tracking.
def log_coffee(coffee, caffeine, mood = "manual"):
    global total_caffeine
    global history

# get the current date and time
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M")
    # store the coffee record in the history
    history.append({
        "time": time_now,
        "coffee": coffee,
        "caffeine": caffeine,
        "mood": mood
    })

    # update the total caffeine intake
    total_caffeine += caffeine
    # save updated history into JSON file
    save_history()

    print("\nCoffee logged successfully .ﾟ(›⩊‹)ﾟ+.ﾟ")
    print(f"Logged coffee: {coffee}")
    print(f"Mood: {mood}")
    print(f"Time: {time_now}")
    caffeine_warning()

# If the user don't want to do the test they can choose to log the drink manually.
def manual_log():
    coffee_names = list(COFFEE_DATA.keys()) # create a list from coffee_data
    while True:
        print("\n=== Coffee Menu ===")

# display all available coffee options with caffeine info

       # automatically number each coffee option starting from 1
        for index, coffee in enumerate(coffee_names, start=1):
            caffeine = COFFEE_DATA[coffee]["caffeine"]
            print(f"{index}. {coffee} ({caffeine}mg)")

#return to the main menu option
        return_option = len(coffee_names) + 1
        print(f"{return_option}. Return to Main Menu")

        choice = input("What did you drink today? ")

        try:
            choice_number = int(choice)
            
# check if the input number is valid
            if 1 <= choice_number <= len(coffee_names):
                selected_coffee = coffee_names[choice_number - 1] # coffee_name is a list!
                caffeine = COFFEE_DATA[selected_coffee]["caffeine"]

                log_coffee(selected_coffee, caffeine)
                break

            elif choice_number == return_option:
                break

            else:
                print(f"Invalid option. Please choose 1-{return_option}.")

        except:
            print("Invalid input. Please enter a number.")

# displays caffeine intake status and warning messages. will be used when 1)check the caffeine level 2. after log the drink
def caffeine_warning():
    global total_caffeine
    print(f"\nCurrent caffeine total: {total_caffeine}mg")

    if total_caffeine == 0:
        print("Status: No caffeine logged today (´Ａ｀。)\n")

    elif total_caffeine < 200:
        print("Status: Safe(• ̀ω•́ )")
        print("You are still in a low caffeine zone.\n")

    elif total_caffeine <= 400:
        print("Status: Moderate caffeine intake (＠_＠;)")
        print("Caution! Do not exceed 400mg -`д´-\n")
    else:
        print("Status: High caffeine intake!!")
        print("Maybe drink some water and avoid more coffee today (｡•ㅅ•｡)\n")

# saves coffee history data into a JSON file. 
# This part Chat Gpt is used for searching how to save file by using JSON.
def save_history():
    with open("history.json", "w") as file:
        json.dump(history, file, indent = 4)

# load the coffee history from JSON file
def load_history():

    global history
    global total_caffeine

    try:
        # open and read the saved JSON history file
        with open("history.json", "r") as file:
            history = json.load(file)

        total_caffeine = 0 # recalculates today's caffeine total.
        today = datetime.now().strftime("%Y-%m-%d")

        for item in history: # only count drinks logged today
            if item["time"].startswith(today):
                total_caffeine += item["caffeine"]
    
    # if the history file does not exist, start with empty data
    except FileNotFoundError:
        history = []
        total_caffeine = 0

    # if the file is corrupted or empty, reset the file
    except json.JSONDecodeError:
        history = []
        total_caffeine = 0
        save_history()

# displays history viewing option
def view_history():

    while True:
        print("\n=== View History ===")
        print("1. Today's history")
        print("2. All history")
        print("3. Return to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            show_history("today")
            break

        elif choice == "2":
            show_history("all")
            break

        elif choice == "3":
            break

        else:
            print("Invalid option. Please choose 1-3.")
            continue


# displays either today's or all saved history.
def show_history(mode):

    print("\n=== Coffee History ===")

    if len(history) == 0:
        print("No coffee logged yet. (´Ａ｀。)")
        return
    # get today's date for filtering records
    today = datetime.now().strftime("%Y-%m-%d")
    filtered_history = []

    for item in history:
        if mode == "today":
            # only include drinks logged today
            if item["time"].startswith(today):
                filtered_history.append(item)
        elif mode == "all":
            # include all saved records
            filtered_history.append(item)

    if len(filtered_history) == 0:
        print("No coffee records found for this view. (´Ａ｀。)")
        return

    total = 0
    # display filterd history records
    for index, item in enumerate(filtered_history, start=1):
        print(
            f"{index}. [{item['time']}] "
            f"{item['coffee']} ({item['caffeine']}mg) "
            f"| Mood: {item['mood']}"
        )
        total += item["caffeine"]

    print(f"\nTotal drinks shown: {len(filtered_history)}")
    print(f"Total caffeine shown: {total}mg\n")

# clear today's record and reset all tracking.
def reset_today():
    global history
    global total_caffeine
    confirm = input("(×ω×)Are you sure you want to clear today's records (yes/no): ").lower()
    if confirm != "yes":
        print("Reset Cancelled.")
        return
   # get today's date
    today = datetime.now().strftime("%Y-%m-%d")
    new_history = []

    # keep only the records that were not logged today
    for item in history:
        if not item["time"].startswith(today):
            new_history.append(item)

   # replace the old history with the filtered history
    history = new_history
    total_caffeine = 0
    save_history()
    print("\nToday's caffeine records have been cleared( ～'ω')～")
        
# starts the program
if __name__ == "__main__":
    load_history()
    main_menu()
