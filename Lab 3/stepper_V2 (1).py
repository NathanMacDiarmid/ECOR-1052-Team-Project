# For students
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

control_pins = [21, 20, 12, 16]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)
    
# Following matrix should contain the coil energizing sequence for coils A, B, A',  and B' 
halfstep_seq = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]
]


for i in range(50): # Hint: For Task 2, change the argument of 'range' to see what effect is has on motor rotation.
    for halfstep in range(8):
        for pin in range(4):
            GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(0.001)
        
GPIO.cleanup()