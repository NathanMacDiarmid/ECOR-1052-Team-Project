import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(1,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)


num = 0

while num <= 247:
    
    GPIO.output(25,GPIO.LOW) # Initializes all of the outputs back to zero before the reading of the next list.
    GPIO.output(8,GPIO.LOW)
    GPIO.output(7,GPIO.LOW)
    GPIO.output(1,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(16,GPIO.LOW)
    GPIO.output(20,GPIO.LOW)
    GPIO.output(21,GPIO.LOW)
    
    lst = []
    i = num
    
    for x in range(8): # Sets up an 8-bit list, changes provided number to binary.
        lst.append(i % 2)
        i = i // 2
    lst.reverse() # Reverses the list so it is in proper binary order.
    print(lst) # Prints the new list every time it is updated.
    
    # Checks to see which LED is lighting up.
    if lst[0] != 0:
        GPIO.output(25,GPIO.HIGH)
        
    if lst[1] != 0:
        GPIO.output(8,GPIO.HIGH)
        
    if lst[2] != 0:
        GPIO.output(7,GPIO.HIGH)
        
    if lst[3] != 0:
        GPIO.output(1,GPIO.HIGH)
        
    if lst[4] != 0:
        GPIO.output(12,GPIO.HIGH)
        
    if lst[5] != 0:
        GPIO.output(16,GPIO.HIGH)
        
    if lst[6] != 0:
        GPIO.output(20,GPIO.HIGH)
        
    if lst[7] != 0:
        GPIO.output(21,GPIO.HIGH)
            
    num += 1 # Adds 1 to the precoditioned variable so that it goes in a range from 0 to 255 - last digit in team leaders student number. In our case, that was 4.
    time.sleep(0.5) # Pauses before reading next list.
    
GPIO.cleanup()