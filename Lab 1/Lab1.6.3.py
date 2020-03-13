import RPi.GPIO as GPIO #Library for the GPIO Pins
import time #Library for time-related tasks

GPIO.setmode(GPIO.BCM) #Sets the way we reference the GPIO Pins
GPIO.setup(25,GPIO.OUT) #Sets GPIO Pin 25 to an output pin
GPIO.setup(8,GPIO.OUT) #Sets GPIO Pin 8 to an output pin
GPIO.setup(7,GPIO.OUT) #Sets GPIO Pin 7 to an output pin
GPIO.setup(1,GPIO.OUT) #Sets GPIO Pin 1 to an output pin
GPIO.setup(12,GPIO.OUT) #Sets GPIO Pin 12 to an output pin
GPIO.setup(16,GPIO.OUT) #Sets GPIO Pin 16 to an output pin
GPIO.setup(20,GPIO.OUT) #Sets GPIO Pin 20 to an output pin
GPIO.setup(21,GPIO.OUT) #Sets GPIO Pin 21  to an output pin

for x in range(1): #iterates through the loop once

    print ("LED 25 on") #Prints when the LED turns on in the console below
    GPIO.output(25,GPIO.HIGH) #Sets the voltage of Pin 25 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 8 on") #Prints when the LED turns on in the console below
    GPIO.output(8,GPIO.HIGH) #Sets the voltage of Pin 8 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 7 on") #Prints when the LED turns on in the console below
    GPIO.output(7,GPIO.HIGH) #Sets the voltage of Pin 7 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 1 on") #Prints when the LED turns on in the console below
    GPIO.output(1,GPIO.HIGH) #Sets the voltage of Pin 1 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 12 on") #Prints when the LED turns on in the console below
    GPIO.output(12,GPIO.HIGH) #Sets the voltage of Pin 12 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 16 on") #Prints when the LED turns on in the console below
    GPIO.output(16,GPIO.HIGH) #Sets the voltage of Pin 16 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 20 on") #Prints when the LED turns on in the console below
    GPIO.output(20,GPIO.HIGH) #Sets the voltage of Pin 20 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 21 on") #Prints when the LED turns on in the console below
    GPIO.output(21,GPIO.HIGH) #Sets the voltage of Pin 25 'HIGH' (3.3V)
    time.sleep(2) #Pauses the program for 2 seconds
    
    print ("LED 25 off") #Prints when the LED turns off in the console below
    GPIO.output(25,GPIO.LOW) #Sets the voltage of Pin 25 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 7 off") #Prints when the LED turns off in the console below
    GPIO.output(7,GPIO.LOW) #Sets the voltage of Pin 7 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 12 off") #Prints when the LED turns off in the console below
    GPIO.output(12,GPIO.LOW) #Sets the voltage of Pin 12 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 20 off") #Prints when the LED turns off in the console below
    GPIO.output(20,GPIO.LOW) #Sets the voltage of Pin 20 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 8 off") #Prints when the LED turns off in the console below
    GPIO.output(8,GPIO.LOW) #Sets the voltage of Pin 8 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 1 off") #Prints when the LED turns off in the console below
    GPIO.output(1,GPIO.LOW) #Sets the voltage of Pin 1 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 16 off") #Prints when the LED turns off in the console below
    GPIO.output(16,GPIO.LOW) #Sets the voltage of Pin 16 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    
    print ("LED 21 off") #Prints when the LED turns off in the console below
    GPIO.output(21,GPIO.LOW) #Sets the voltage of Pin 21 'LOW' (0V)
    time.sleep(2) #Pauses the program for 2 second
    

GPIO.cleanup()#Resets the GPIO Pins that we used
