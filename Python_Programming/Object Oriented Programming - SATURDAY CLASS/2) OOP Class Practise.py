# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:30:05 2023

@author: lEO
"""

class Human:
    # OUR ATTRIBUTES OR CHARACTERISTICS
    def __init__(self, firstname, lastname, age, phone_number, height, weight, skin_color, eye_color, hair_style, body_build, shoe_size, fathers_name, mothers_name, gender):
        self.__firstname = firstname
        self.__lastname = lastname 
        self.__age = age
        self.__phone_number = phone_number
        self.height = height
        self.__weight = weight
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.hair_style = hair_style
        self.body_build =  body_build   # Possible options ("Average Size", "Muscular", "Chubby", "Obese", "Skinny", "Petite")
        self.__shoe_size = shoe_size
        self.__fathers_name = fathers_name
        self.__mothers_name = mothers_name
        self.__friends = []
        self.__gender = gender
    
    
    # OUR METHODS OR ACTIONS
    def make_friends(self, name):
        self.__friends_name = name
        self.__friends.append(self.__friends_name)
    
    def who_are_your_friends(self):
        return self.__friends
        
    # Write the METHOD to remove a friend --- ASSIGNMENT




Ifunanya = Human(
    firstname = "Ifunanya", 
    lastname = "Akupuome", 
    age = 24, 
    phone_number = "09034522070", 
    height = 5.5, 
    weight = 82, 
    skin_color = "Light-skinned", 
    eye_color = "Brown", 
    hair_style = "Cornrows", 
    body_build = "obese :)", 
    shoe_size = 40, 
    fathers_name = "Bartholomew", 
    mothers_name = "Caroline", 
    gender = "Female")

Jennifer = Human(
    firstname = "Jennifer", 
    lastname = "Major", 
    age = 28, 
    phone_number = "09083903633", 
    height = 5.7, 
    weight = 70, 
    skin_color = "Light-skinned", 
    eye_color = "Hazel", 
    hair_style = "Afro", 
    body_build = "Slim", 
    shoe_size = 44, 
    fathers_name = "Captain", 
    mothers_name = "Ruth", 
    gender = "female")
        
Vanessa = Human(
    firstname = "Vanessa", 
    lastname = "Shaka", 
    age = 25, 
    phone_number = "08109828582", 
    height = 5.3, 
    weight = 70, 
    skin_color = "Black", 
    eye_color = "Brown", 
    hair_style = "Cornrows", 
    body_build = "Mesomorph", 
    shoe_size = 37, 
    fathers_name = "Joseph", 
    mothers_name = "Faith", 
    gender = "Female")   
  
    


Ifunanya.make_friends("Jennifer")
Ifunanya.make_friends("Henry")



# Leonards_friends = Leonard.who_are_your_friends()

















 
    
  
    
  
    
  
    
  
    


