def get_user_data():
    """
    Get data input from the user 
    """
    print("Please enter your height in centimeters")
    print("Example: 162")

    height = input("Enter your data here: ")

    print("Please enter your weight in kilograms")
    print("Example: 60")

    weight = input("Enter your data here: ")
    print(f'Your height is {height} cm and weight is {weight} kg')


get_user_data()
