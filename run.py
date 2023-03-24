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

    print("\nPlease enter 'f' if you are woman and 'm' if you are man")
    print("Example: f\n")
    gender = input("Enter your data here:\n")

    print("Calculating...")
    return weight, height, age, gender


def basal_metabolic_rate_woman(weight, height, age, gender):
    """
    Calculate basal metabolic rate for women
    """
    bmr = 655.1 + (9.6 * weight) + (1.85 * height) - (age * 4.68) 
    # source - Wikipedia
    print(f"Weight:{weight}, height:{height}, age:{age}, gender:{gender}")
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
    while we are doing nothing.""")


def determine_gender():
    """
    Calculate BMR depend on gender
    """
    weight, height, age, gender = get_user_data()
    if (gender == "m"):
        basal_metabolic_rate_man(weight, height, age, gender)
    else:
        basal_metabolic_rate_woman(weight, height, age, gender)


determine_gender()