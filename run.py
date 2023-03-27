def get_user_height():
    """
    Get data input from the user - height
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
    Get data input from the user - weight
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
    Get data input from the user - age
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
    Get data input from the user - gender
    """
    while True:
        print("\nPlease enter 'female' if you are woman and 'male' if you are man")
        print("Example: female\n")
        try:
            user_gender = input("Enter your data here:\n")

            if user_gender != 'female' or user_gender != 'male':
                print(f"\nYou entered {user_gender}. Please, enter 'male' or 'female'\n")
            else:
                return user_gender
        except ValueError:
            print("Gender is not valid")


def get_user_activity():
    """
    Get data input from the user - activity
    """
    print("\nPlease enter data about your activity")
    print("""\n    Little or no exercise: press 1\n
    1–3 days per week of exercise or activity: press 2\n
    3–5 days per week of moderate activity or sports: press 3\n
    6–7 days per week of hard exercise: press 4\n
    athletes who train twice per day or more: press 5""")
    print("Example: 2\n")
    user_activity = input("Enter your data here:\n")

    return user_activity


def get_user_goal():
    """
    Get data input from the user - height
    """
    print("\nPlease enter data about your goal")
    print("""\n    To lose weight : enter 'lose'\n
    To keep weight: enter 'maintain'\n
    To gain weight : enter 'gain' """)
    print("Example: lose\n")
    user_goal = input("Enter your data here:\n")

    return user_goal


def basal_metabolic_rate_woman(weight, height, age):
    """
    Calculate basal metabolic rate for women
    """
    bmr = 655.1 + (9.6 * weight) + (1.85 * height) - (age * 4.68) 
    # source - Wikipedia
    print(f"\nWeight: {weight}, height: {height}, age: {age}, gender: woman")
    print(f"\nYour basal metabolic rate is {int(bmr)} calories per day.")
    print("""\n    Basal metabolic rate (BMR) - minimum amount of calories 
    that our body needs to carry out basic functions such
    as breathing, circulation, and cell production while 
    at rest. In other words, it is the  amount of 
    energy required by our body to keep functioning 
    while we are doing nothing.""")
    return bmr


def basal_metabolic_rate_man(weight, height, age):
    """
    Calculate basal metabolic rate for men
    """
    bmr = 66.5 + (13.7 * weight) + (5 * height) - (age * 6.75)
    # source - Wikipedia
    print(f"Weight:{weight}, height:{height}, age:{age}, gender: man")
    print(f"Your basal metabolic rate is {int(bmr)} calories per day.")
    print("""\n    Basal metabolic rate (BMR) - minimum amount of calories 
    that our body needs to carry out basic functions such
    as breathing, circulation, and cell production while 
    at rest. In other words, it is the  amount of 
    energy required by our body to keep functioning 
    while we are doing nothing.\n""")
    return bmr


def calculate_bmr(weight, height, age, gender):
    """
    Calculate BMR depend on gender
    """
    if (gender == "male"):
        return basal_metabolic_rate_man(weight, height, age)
    else:
        return basal_metabolic_rate_woman(weight, height, age)


def calorie_calculator(activity, bmr):
    """ 
    Calculate calorie needs based on BMR
    """
    if activity == "1":
        calorie_needs = bmr * 1.2
    elif activity == "2":
        calorie_needs = bmr * 1.37
    elif activity == "3":
        calorie_needs = bmr * 1.55
    elif activity == "4":
        calorie_needs = bmr * 1.72
    else:
        calorie_needs = bmr * 1.9        

    return int(calorie_needs) 


def goal_calorie():
    """ 
    Calculate calorie needs depend on user goal
    """
    get_height = get_user_height()
    get_weight = get_user_weight()

    get_age = get_user_age()
    get_gender = get_user_gender()
    get_activity = get_user_activity()
    get_goal = get_user_goal()
    
    get_bmr = calculate_bmr(get_weight, get_height, get_age, get_gender)
    daily_calorie = calorie_calculator(get_activity, get_bmr)
    
    if get_goal == "lose":
        new_calorie = daily_calorie - 500
    elif get_goal == "gain":
        new_calorie = daily_calorie + 500
    else:
        new_calorie = daily_calorie

    print(f"\nYour daily calorie needs are:\n    {daily_calorie} calories per day")
    print(f"\nTo {get_goal} weight eat:")
    
    return int(new_calorie)


if __name__ == "__main__":
    
    get_goal_calorie = goal_calorie()
    print(f"    {get_goal_calorie} calories per day")