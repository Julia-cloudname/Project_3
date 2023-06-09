def menu():
    """
    The function presents a menu to the user with two options:
    to start the program or to end it. If the input is valid, the function
    returns the user's choice ("Q" or "S") as a string.
    """
    while True:
        print("1. Enter S to start program/ run again\n"
              "2. Enter Q to end program\n")
        user_choice = input("").lower()
        if user_choice not in ["q", "s"]:
            print(f"\nYou entered {user_choice}. Please enter Q or S")
        else:
            return user_choice


def get_user_height():
    """
    Gets the user's height input in centimetres. If the
    input is not valid, prints a message telling to enter a valid
    height. Returns the input as an integer in a variable.
    """
    while True:
        print("Please enter your height in centimeters")
        print("Example: 172\n")
        try:
            user_height = int(input("Enter your data here:\n"))
            if user_height >= 300 or user_height <= 50:
                print("\nPlease enter a valid height")
            else:
                return user_height
        except ValueError:
            print("\nNot a number. Please, enter your height as a number\n")


def get_user_weight():
    """
    Gets the user's weight input in kg. If the input is not valid,
    prints a message telling to enter a valid weight. Returns the
    input as an integer in a variable.
    """
    while True:
        print("\nPlease enter your weight in kilograms")
        print("Example: 70\n")
        try:
            user_weight = int(input("Enter your data here:\n"))
            if user_weight >= 500 or user_weight <= 3:
                print("\nPlease enter a valid weight")
            else:
                return user_weight
        except ValueError:
            print("\nNot a number. Please, enter your weight as a number\n")


def get_user_age():
    """
    Gets the user's age input in full years. If the input is not valid,
    prints a message telling to enter a valid age. Returns the input as
    an integer in a variable.
    """
    while True:
        print("\nPlease enter your age")
        print("Example: 38\n")
        try:
            user_age = int(input("Enter your data here:\n"))

            if user_age >= 120 or user_age <= 2:
                print("\nPlease enter a valid age")
            else:
                return user_age
        except ValueError:
            print("\nNot a number. Please, enter your age as a number\n")


def get_user_gender():
    """
    Gets the user's gender as string input from the keyboard. If the
    input is not valid, it prints a message telling to enter a valid gender.
    Returns the input as a string in a variable.
    """
    while True:
        print("\nPlease enter 'female' if you are woman"
              "and 'male' if you are man")
        print("Example: female\n")
        try:
            user_gender = input("Enter your data here:\n").lower()

            if user_gender not in ['female', 'male']:
                print(
                    f"\nYou entered {user_gender}."
                    f" Please, enter 'male' or 'female'\n")
            else:
                return user_gender
        except ValueError:
            print("Gender is not valid")


def get_user_activity():
    """
    Gets the user's activity as integer. If the input is not valid,
    it prints a message telling to enter a valid number. Returns the
    input as an integer in a variable.
    """
    while True:
        print("\nPlease enter data about your activity")
        print("""\n    Little or no exercise: press 1\n
        1 - 3 days per week of exercise or activity: press 2\n
        3 - 5 days per week of moderate activity or sports: press 3\n
        6 - 7 days per week of hard exercise: press 4\n
        athletes who train twice per day or more: press 5""")
        print("Example: 2\n")
        try:
            user_activity = input("Enter your data here:\n")
            if user_activity not in ['1', '2', '3', '4', '5']:
                print("""\nPlease enter a valid number of activity from"
                      "1 till 5""")
            else:
                return int(user_activity)
        except ValueError:
            print("""\nNot a number. Please, enter your user
            activity as a number\n""")


def get_user_goal():
    """
    Gets the user's goal as string input from the keyboard. If the
    input is not valid, it prints a message telling to enter a valid goal.
    Returns the input as a string in a variable.
    """
    while True:
        print("\nPlease enter data about your goal")
        print("""\n    To lose weight : enter 'lose'\n
        To keep weight: enter 'maintain'\n
        To gain weight : enter 'gain' """)
        print("Example: lose\n")
        try:
            user_goal = input("Enter your data here:\n").lower()
            if user_goal not in ['lose', 'maintain', 'gain']:
                print(f"\nYou entered {user_goal}."
                      f" Please enter a valid goal")
            else:
                return user_goal
        except ValueError:
            print("""\n Please, chose your goal from menu\n""")


def bmr_woman(weight_value, height_value, age_value):
    """
    Calculates basal metabolic rate for women. Function takes weight,
    height and age as parametres. Returns calculation as integer in
    variable
    """
    bmr_value = 655.1 + \
        (9.6 * weight_value) + \
        (1.85 * height_value) - \
        (age_value * 4.68)
    # source - Wikipedia
    print(f"\nWeight: {weight_value}, height: {height_value}, "
          f" age: {age_value}, gender: woman")
    print(f"\nYour basal metabolic rate is"
          f" {int(bmr_value)} calories per day.\n")
    print("Basal metabolic rate (BMR) - minimum amount of calories"
          "that our body needs to carry out basic functions such"
          "as breathing, circulation, and cell production while "
          "at rest. In other words, it is the  amount of"
          "energy required by our body to keep functioning"
          "while we are doing nothing.")
    return bmr_value


def bmr_man(weight_value, height_value, age_value):
    """
    Calculates basal metabolic rate for men. Function takes weight,
    height and age as parametres. Returns calculation as integer in
    variable
    """
    bmr_value = 66.5 + (13.7 * weight_value) + (5 * height_value) - \
        (age_value * 6.75)
    # source - Wikipedia
    print(f"Weight: {weight_value}, height: {height_value}"
          f" age: {age_value}, gender: man")
    print(f"Your basal metabolic rate is {int(bmr_value)} calories per day.\n")
    print("Basal metabolic rate (BMR) - minimum amount of calories"
          "that our body needs to carry out basic functions such"
          "as breathing, circulation, and cell production while "
          "at rest. In other words, it is the  amount of"
          "energy required by our body to keep functioning"
          "while we are doing nothing.")
    return bmr_value


def calculate_bmr(weight_value, height_value, age_value, gender_value):
    """
    Calculates BMR depend on gender. Function takes weight,
    height, age and gender as parametres. Returns calculation as integer in
    variable
    """
    if (gender_value == "male"):
        return bmr_man(weight_value, height_value, age_value)
    else:
        return bmr_woman(weight_value, height_value, age_value)


def calorie_calculator(activity_value, bmr_value):
    """
    Calculats calorie needs based on BMR. Function takes activity and
    BMR as parametres. Returns calculation as integer in variable
    """
    if activity_value == 1:
        calorie_needs = bmr_value * 1.2
    elif activity_value == 2:
        calorie_needs = bmr_value * 1.37
    elif activity_value == 3:
        calorie_needs = bmr_value * 1.55
    elif activity_value == 4:
        calorie_needs = bmr_value * 1.72
    else:
        calorie_needs = bmr_value * 1.9

    return int(calorie_needs)


def goal_calorie(goal_value, daily_calorie_value):
    """
    Calculats calorie needs depend on user goal. Function takes goal and
    daily calorie as parametres. Returns calculation as integer in variable
    """

    if goal_value == "lose":
        return int(daily_calorie_value - 500)
    elif goal_value == "gain":
        return int(daily_calorie_value + 500)
    else:
        return int(daily_calorie_value)


def print_welcome():
    """Prints welcome message"""
    print("""   
         *     (                                                         
   (   (  `    )\ )     (          (             (           )           
 ( )\  )\))(  (()/(     )\      )  )\        (   )\    )  ( /(      (    
 )((_)((_)()\  /(_))  (((_)  ( /( ((_) (    ))\ ((_)( /(  )\()) (   )(   
((_)_ (_()((_)(_))    )\___  )(_)) _   )\  /((_) _  )(_))(_))/  )\ (()\  
 | _ )|  \/  || _ \  ((/ __|((_)_ | | ((_)(_))( | |((_)_ | |_  ((_) ((_) 
 | _ \| |\/| ||   /   | (__ / _` || |/ _| | || || |/ _` ||  _|/ _ \| '_| 
 |___/|_|  |_||_|_\    \___|\__,_||_|\__|  \_,_||_|\__,_| \__|\___/|_|   
""")
    print("Welcome to the calorie calculator! Let's calculate calorie needs!")


def main():
    """Starts program"""
    print_welcome()

    while True:
        print("Press Enter to continue...")
        input()
        user_choice = menu()

        if user_choice == "q":
            print("The program is finished. Press Run program to start it")
            exit()
        else:
            height = get_user_height()
            weight = get_user_weight()
            age = get_user_age()
            gender = get_user_gender()
            activity = get_user_activity()
            goal = get_user_goal()

            bmr = calculate_bmr(weight, height, age, gender)
            daily_calorie = calorie_calculator(activity, bmr)

            goal_calorie_value = goal_calorie(goal, daily_calorie)

            print(f"\nYour daily calorie needs are: "
                  f" {daily_calorie} calories per day")
            print(f"\nTo {goal} weight eat: {goal_calorie_value}"
                  f" calories per day")


if __name__ == "__main__":
    main()

