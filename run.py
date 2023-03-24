def get_user_data():
    """
    Get data input from the user 
    """
    print("Please enter your height in centimeters")
    print("Example: 172\n")
    height = int(input("Enter your data here:\n"))

    print("\nPlease enter your weight in kilograms")
    print("Example: 70\n")
    weight = int(input("Enter your data here:\n"))

    print("\nPlease enter your age")
    print("Example: 38\n")
    age = int(input("Enter your data here:\n"))

    print("\nPlease enter 'female' if you are woman and 'male' if you are man")
    print("Example: female\n")
    gender = input("Enter your data here:\n")

    print("Calculating...")
    return weight, height, age, gender


def basal_metabolic_rate_woman(weight, height, age, gender):
    """
    Calculate basal metabolic rate for women
    """
    bmr = 655.1 + (9.6 * weight) + (1.85 * height) - (age * 4.68) 
    # source - Wikipedia
    print(f"Weight: {weight}, height: {height}, age: {age}, gender: {gender}")
    print(f"Your basal metabolic rate is {int(bmr)} calories per day.")
    print("""\n    Basal metabolic rate (BMR) - minimum amount of calories 
    that our body needs to carry out basic functions such
    as breathing, circulation, and cell production while 
    at rest. In other words, it is the  amount of 
    energy required by our body to keep functioning 
    while we are doing nothing.""")


def basal_metabolic_rate_man(weight, height, age, gender):
    """
    Calculate basal metabolic rate for men
    """
    bmr = 66.5 + (13.7 * weight) + (5 * height) - (age * 6.75)
    # source - Wikipedia
    print(f"Weight:{weight}, height:{height}, age:{age}, gender:{gender}")
    print(f"Your basal metabolic rate is {int(bmr)} calories per day.")
    print("""\n    Basal metabolic rate (BMR) - minimum amount of calories 
    that our body needs to carry out basic functions such
    as breathing, circulation, and cell production while 
    at rest. In other words, it is the  amount of 
    energy required by our body to keep functioning 
    while we are doing nothing.\n""")


def determine_gender():
    """
    Calculate BMR depend on gender
    """
    weight, height, age, gender = get_user_data()
    if (gender == "male"):
        basal_metabolic_rate_man(weight, height, age, gender)
    else:
        basal_metabolic_rate_woman(weight, height, age, gender)


determine_gender()


def activity_multiplier():
    """ 
    Define type of activity based on user answer
    """
    print("\nPlease enter data about your activity")
    print("""\n    Little or no exercise: press 1\n
    1–3 days per week of exercise or activity: press 2\n
    3–5 days per week of moderate activity or sports: press 3\n
    6–7 days per week of hard exercise: press 4\n
    athletes who train twice per day or more: press 5""")
    print("Example: 2\n")
    activity = int(input("Enter your data here:\n"))

    return activity 


activity_multiplier()


def get_user_goal():
    """
    Get data input from the user about goal
    """
    print("\nPlease enter data about your goal")
    print("""\n    To lose weight : enter 'lose'\n
    To keep weight: enter 'maintain'\n
    To gain weight : enter 'gain' """)
    print("Example: lose\n")
    goal = input("Enter your data here:\n")
    print(goal)


get_user_goal()

def calorie_calculator():
    """ 
    Calculate calorie needs based on BMR
    """