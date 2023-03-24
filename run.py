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

    print("\nPlease enter data about your activity")
    print("""\n    Little or no exercise: press 1\n
    1–3 days per week of exercise or activity: press 2\n
    3–5 days per week of moderate activity or sports: press 3\n
    6–7 days per week of hard exercise: press 4\n
    athletes who train twice per day or more: press 5""")
    print("Example: 2\n")
    activity = input("Enter your data here:\n")

    print("\nPlease enter data about your goal")
    print("""\n    To lose weight : enter 'lose'\n
    To keep weight: enter 'maintain'\n
    To gain weight : enter 'gain' """)
    print("Example: lose\n")
    goal = input("Enter your data here:\n")

    return weight, height, age, gender, activity, goal


def basal_metabolic_rate_woman(weight, height, age):
    """
    Calculate basal metabolic rate for women
    """
    bmr = 655.1 + (9.6 * weight) + (1.85 * height) - (age * 4.68) 
    # source - Wikipedia
    print(f"Weight: {weight}, height: {height}, age: {age}, gender: woman")
    print(f"Your basal metabolic rate is {int(bmr)} calories per day.")
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

    return calorie_needs 
        

if __name__ == "__main__":
    weight, height, age, gender, activity, goal = get_user_data()
    bmr = calculate_bmr(weight, height, age, gender)
    daily_calorie = calorie_calculator(activity, bmr)
    print(daily_calorie)