#!python3
# Volume Calculator
# Feel free to rename your variables
import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print ("================")
    print ("1. Find volume")
    print ("2. Instructions")
    print ("3. Quit")
    print ("================")

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print ("================")
    print ("The program will\nask you to choose\nbetween 3 shapes\nthen will ask for\nyou to enter info\nneeded to solve and\nthen give you the\nvolume")
    print ("================")
    return None

def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    #prompts
    
    if shape == 1:
        prompts = ["What is side length "]
    elif shape == 2:
        prompts = ["What is radius "]
    elif shape == 3:
        prompts = ["What is its radius ","What is its height "]
    else:
        prompts = []
    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    i1 = input(questions[0])
    i2 = ()
    measurements = [float(i1)]
    if len(questions) > 1:
        i2 = input(questions[1])
        measurements = [float(i1),float(i2)]
    return measurements

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    Exit = False
    while Exit == False:
        title()
        ip = input("Enter number ")
        if int(ip) == 1:
            print ("==============")
            print ("1. Cube")
            print ("2. Sphere")
            print ("3. Cylinder")
            print ("==============")
            shape = input("Enter Shape ")
            shape = int(shape)
            questions = getParams(shape)
            measurements = getInputs(questions)
            if shape == 1:
                answer = math.pow(measurements[0], 3)
                answer = round(answer, 2)
                print ("The answer is " + str(answer))
            if shape == 2:
                answer = 4/3 * math.pi * math.pow(measurements[0],3)
                answer = round(answer, 2)
                print ("The answer is " + str(answer))
            if shape == 3:
                answer = math.pi * math.pow(measurements[0],2) * measurements[1]
                answer = round(answer, 2)
                print ("The answer is " + str(answer))
        elif int(ip) ==2:
            instructions()
        elif int(ip) == 3:
            Exit = True
main()
