import os
import time
os.system("sudo pigpiod")
time.sleep(1)
import pigpio

# output pins on raspi mapped to ESCs
esc_1 = 23
esc_2 = 25
esc_3 = 12
esc_4 = 16

pi = pigpio.pi();
pi.set_servo_pulsewidth(esc_1, 0)
pi.set_servo_pulsewidth(esc_2, 0)
pi.set_servo_pulsewidth(esc_3, 0)
pi.set_servo_pulsewidth(esc_4, 0)

max_throttle = 2000
min_throttle = 700


while (True):

    command = input("calibrate OR manual OR control OR arm OR stop OR exit: ")

    if command == "manual":
        manual_drive()
    elif command == "calibrate":
        calibrate()
    elif command == "arm":
        arm()
    elif command == "control":
        control()
    elif command == "stop":
        stop()
    elif command == "exit":
        exit()
    else:
        print("Invalid input\n")



#def manual_drive(): #You will use this function to program your ESC if required
#    print "You have selected manual option so give a value between 0 and you max value"
#    while True:
#        inp = raw_input()
#        if inp == "stop":
#            stop()
#            break
#        elif inp == "control":
#            control()
#            break
#        elif inp == "arm":
#            arm()
#            break
#        else:
#            pi.set_servo_pulsewidth(ESC,inp)

def calibrate():   #This is the auto calibration procedure of a normal ESC

    pi.set_servo_pulsewidth(esc_1, 0)
    pi.set_servo_pulsewidth(esc_2, 0)
    pi.set_servo_pulsewidth(esc_3, 0)
    pi.set_servo_pulsewidth(esc_4, 0)
    
    inp = input("Disconnect the battery and press Enter")
    if inp == '':
        
        pi.set_servo_pulsewidth(esc_1, max_throttle)
        pi.set_servo_pulsewidth(esc_2, max_throttle)
        pi.set_servo_pulsewidth(esc_3, max_throttle)
        pi.set_servo_pulsewidth(esc_4, max_throttle)
        
        inp = input("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
        if inp == '':
            
            pi.set_servo_pulsewidth(esc_1, min_throttle)
            pi.set_servo_pulsewidth(esc_2, min_throttle)
            pi.set_servo_pulsewidth(esc_3, min_throttle)
            pi.set_servo_pulsewidth(esc_4, min_throttle)
            
            print "Wierd eh! Special tone"
            time.sleep(7)
            print "Wait for it ...."
            time.sleep (5)
            print "Im working on it, DONT WORRY JUST WAIT....."
            
            pi.set_servo_pulsewidth(esc_1, 0)
            pi.set_servo_pulsewidth(esc_2, 0)
            pi.set_servo_pulsewidth(esc_3, 0)
            pi.set_servo_pulsewidth(esc_4, 0)
            
            time.sleep(2)
            print "Arming ESC now..."
            
            pi.set_servo_pulsewidth(esc_1, min_throttle)
            pi.set_servo_pulsewidth(esc_2, min_throttle)
            pi.set_servo_pulsewidth(esc_3, min_throttle)
            pi.set_servo_pulsewidth(esc_4, min_throttle)

            time.sleep(1)
            print "See.... uhhhhh"
            control() # You can change this to any other function you want

#def control():
#    print "I'm Starting the motor, I hope its calibrated and armed, if not restart by giving 'x'"
#    time.sleep(1)
#    speed = 1500    # change your speed if you want to.... it should be between 700 - 2000
#    print "Controls - a to decrease speed & d to increase speed OR q to decrease a lot of speed & e to increase a lot of speed"
#    while True:
#        pi.set_servo_pulsewidth(ESC, speed)
#        inp = raw_input()
#
#        if inp == "q":
#            speed -= 100    # decrementing the speed like hell
#            print "speed = %d" % speed
#        elif inp == "e":
#            speed += 100    # incrementing the speed like hell
#            print "speed = %d" % speed
#        elif inp == "d":
#            speed += 10     # incrementing the speed
#            print "speed = %d" % speed
#        elif inp == "a":
#            speed -= 10     # decrementing the speed
#            print "speed = %d" % speed
#        elif inp == "stop":
#            stop()          #going for the stop function
#            break
#        elif inp == "manual":
#            manual_drive()
#            break
#        elif inp == "arm":
#            arm()
#            break
#        else:
#            print "WHAT DID I SAID!! Press a,q,d or e"

#def arm(): #This is the arming procedure of an ESC
#    print "Connect the battery and press Enter"
#    inp = raw_input()
#    if inp == '':
#        pi.set_servo_pulsewidth(ESC, 0)
#        time.sleep(1)
#        pi.set_servo_pulsewidth(ESC, max_value)
#        time.sleep(1)
#        pi.set_servo_pulsewidth(ESC, min_value)
#        time.sleep(1)
#        control()

#def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
#    pi.set_servo_pulsewidth(ESC, 0)
#    pi.stop()

