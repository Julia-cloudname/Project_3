def get_user_data():
    """
    Get data input from the user 
    """
    print("Please enter your height in centimeters")
    print("Example: 162\n")
    height = int(input("Enter your data here: "))

    print("\nPlease enter your weight in kilograms")
    print("Example: 60\n")
    weight = int(input("Enter your data here: "))

    print("\nPlease enter your age")
    print("Example: 34\n")
    age = int(input("Enter your data here: "))

    print("Calculating...")
    return weight, height, age


def basal_metabolic_rate(weight, height, age):
    """
    Calculate basal metabolic rate
    """
    bmr = 655.1 + (9.6 * weight) + (1.85 * height) - (age * 4.68)
    print(f"Your basal metabolic rate is {int(bmr)} calories per day.")
    print("""\n    Basal metabolic rate (BMR) - minimum amount of calories that our 
    body needs to carry out basic functions such as 
    breathing, circulation, and cell production while 
    at rest. In other words, it is the  amount of 
    energy required by our body to keep functioning 
    while we are doing nothing.""")


# get data from user
weight, height, age = get_user_data()

# calculate BMR
basal_metabolic_rate(weight, height, age)