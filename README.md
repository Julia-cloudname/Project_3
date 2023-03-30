# **Calorie Calculator**
## **Overview**

Calorie Calculator is a console application for calculating daily calorie requirements based on height, weight, gender, and physical activity. In this application, the user inputs the required data, and based on that, the program calculates the basal metabolic rate (BMR). This is the minimum number of calories required by our body to perform basic functions such as breathing, blood circulation, and cell production while at rest. In other words, it is the amount of energy our body needs to continue functioning while doing nothing.

Additionally, the user can receive recommendations on how many calories they should consume per day to achieve their goal, whether it is to lose, gain, or maintain weight.

To calculate the basal metabolic rate, the Harris-Benedict formula is used, based on total body mass, height, age, and gender. The application uses recommendations from The Centers for Disease Control and Prevention for weight loss and weight gain to calculate daily calorie requirements.

The application is created in Python and uses functions, loops, and conditional statements to calculate the result.

![Am I Responsive Screenshot](images/bmr_calculator.png)

## Table of contents:
1. [**Overview**](#overview)
1. [**Planning stage**](#planning-stage)
    * [***Target Audiences***](#target-audiences)
    * [***User Stories***](#user-stories)
    * [***App Aims***](#app-aims)
    * [***App diagrams***](#app-diagrams)
1. [**Current Features**](#current-features)
    * [***Start Screen***](#start-screen)
    * [***Control the program***](#control-the-program)
1. [**Future-Enhancements**](#future-enhancements)
1. [**Testing Phase**](#testing-phase)
1. [**Deployment**](#deployment)
1. [**Tech**](#tech)
1. [**Credits**](#credits)
    * [**Content**](#content)
    * [**Media**](#media)
    * [**Honourable mentions**](#honorable-mentions)
​
## **Planning Stage**

#### **Target Audiences:**
* People who want to lose weight and are interested in monitoring their calorie intake to create a calorie deficit and achieve weight loss.
* People who want to maintain their weight and use a calorie calculator to determine their daily calorie needs to maintain their current weight.
* Physically active people and Athletes, who need to determine their daily calorie needs to support their training and physical activity.
* People with health conditions, such as diabetes, who want to monitor their calorie intake and manage their condition.
* Fitness and health and professionals, such as dietitians and personal trainers, who create custom nutrition plans for their clients.

<br>

#### **User Stories:**
* As a user, I want to understand how to start the program.
* As a user, I want to quickly learn and understand how to control the application
* As a user, I want a clean and simple user interface.
* As a user, I want the app to run smoothly and bug-free and how to fix them if they are happening (if I enter not valid data )
* As a user, I want to get calculated results after entering the data
* As a user, I want to be able to choose whether or not to run app again when it ends.

<br>

#### **App Aims:**
* To offer the user a smooth and bug free version of a classic game with a slightly different twist.
* To provide a clean and simple interface for the user with no need to reference external sources.
* To provide clear instructions and a win condition.
* To provide an enjoyable user experience of playing battleships.
* To provide an interesting and entertaining Star Wars-based version of the game.

<br>

#### **App diagrams**

I used [app.diagrams.net](app.diagrams.net) to planning stages of this project

This is the flow chart of the app:
![app.diagrams](diagram)
<br>

## **Current Features**

#### **Start Screen** 

![Screenshot of start screen](png)

* The start screen features the name of the program - BMR Calculator. Then app prompts to press enter and chose to end the program or start.

#### **Control the program**

* To control the program user can use the menu at the start and at the end of the program.  User enter data with keyboard follof the instruction on the screen. 

## **Future-Enhancements**
​
There are several features with scope for future improvement. I would have liked to add the following in future:
​
* Recomendation how to speed up the metabolic rate, for example, by increasing or changing physical activity, improving diet and sleep, calorie content and food composition.
* Add calculate the rate of proteins, fats, carbohydrates

## **Testing Phase**
​
**Functionality**

* I made sure the app performed as expected from start to finish.
* I tried to use the app on a local terminal and on Heroku several times. The app worked as anticipated with no errors.
* When entering incorrect data, I saw error messages on the screen and suggestions on how to fix them in order to continue the application
