#Desert Dash
#Intro
name = input('What is your name? ')
print('Welcome to Desert Dash,', name)
print("")
print('You have stolen a camel to make your way across the great Irimina desert.')
print("")
print('The natives want their camel back and are chasing you down!')
print("")
print('Survive your desert dash and outrun the natives!!!!')
print("")
print('Rules:')
print("")
print('If you die of hunger, you lose, if you die of thirst, you lose, if the natives catch up to you, you lose, if your camel dies of fatigue, you lose.')
print("")

#Vitality/Distance Variables
import random
done = False
miles_traveled = 0
thirst = 0
water = 0
camel_thirst = 0
lactic_acid = 0
natives_traveled = 0
canteen = 5
player_thirst= 0
natives_moving = random.randrange(5,20)
medium_speed = random.randrange(5,15)
full_speed = random.randrange(15,20)

#Player options
while not done:
    print("A. Drink from water sack.")
    print("B. Go at a medium pace.")
    print("C. Speed your camel up to full speed.")
    print("D. Stop to rest your camel overnight.")
    print("E. Make an inventory of your supplies and check the natives progress.")
    print("Q. Give up and allow the natives to take back their camel and kill you.")
    print("")
    decision = input("Pick an action: ")
    print("")
    if decision == "q" or decision == "Q":
        print("GAME OVER MAN, GAME OVER!!!")
        done = True
    #Check yo' self and yo' camel and the natives progress
    elif decision == "e" or decision == "E":
        print("Miles traveled:", miles_traveled)
        print("Sips left in Canteen:", canteen) 
        print("The natives have traveled:", natives_traveled) 
        print("Camel's endurance level:", lactic_acid) 
        print("Camel's thirst level:", camel_thirst)
        full_speed += random.randrange(15,20)
        miles_travaled += random.randrange(15,20)
        natives_traveled += random.randrange(5,20)
        thirst = camel_thirst +1
        water = player_thirst + 1
        print("")
    #Resting overnight
    elif decision == "d" or decision == "D":
        lactic_acid = 0
        print("You have eaten and are no longer hungry")
        print("Your camel is refreshed and ready, but the natives have traveled," ,natives_traveled, "miles")
        print("")
    #full_speed
    elif decision == "c" or decision == "C":
        print("You and your camel are at", full_speed, "miles")
        full_speed += random.randrange(15,20)
        miles_traveled += random.randrange(15,20)
        natives_traveled += random.randrange(5,20)
        camel_thirst + 1
        player_thirst + 1      
        lactic_acid += random.randrange(1,5)
        print("Camel Stamina Level:", lactic_acid)
        print("The natives are at,", natives_traveled, "miles")
        print("")
    #moderate_speed
    elif decision == "b" or decision == "B":
        print ("You and your camel are at", medium_speed, "miles")
        medium_speed += random.randrange(5,15)
        miles_traveled += random.randrange(5,15)
        natives_traveled += random.randrange(5,20) 
        camel_thirst + 1
        player_thirst + 1 
        lactic_acid += random.randrange(1,5)
        print("Camel Stamina Level:", lactic_acid)
        print("The natives are at," ,natives_traveled, "miles")
        print("")
    #drinks_from_canteen
    elif decision == "a" or decision == "A":
        print("you drank from your water sack")
        canteen = canteen - 1
        water = 0
    #You are thirsty
    if water >= 3:
        print("you are getting parched")
    #you died of thirst
    if water >=5:
        print("You died from dehydration, GAME OVER")
        done = True
    #Your camel is getting fatigued
    if lactic_acid >= 8:
        print("Your camel is getting tired, it needs a break")
    #Camel Dies
    if lactic_acid >= 12:
        print("Your camel has died, GAME OVER")
        done = True
    #if the natives catch up with you
    if natives_traveled == miles_traveled:
        print("The natives got you! GAME OVER")
        done = True
    #the natives are on the move
    elif natives_traveled >= -10:
        print("The natives are getting closer")
      
    if miles_traveled == 300:
        print("You won and got through the Irimina Desert, you get to keep the camel. YOU WON")
        done = true

    if canteen <= 0:
        print("You ran out of sips")

    elif thirst >= 1:
        miles_traveled = 1 
      
      
        
            
        
        
    
        
        
    
    
