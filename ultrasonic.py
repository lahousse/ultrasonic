################ Henri Lahousse ################
# easy distance calculation with 4 ultrasonic sensors
# 05/31/2022

# libraries
import RPi.GPIO as GPIO                  # Importing RPi.GPIO for the pins
import time                              # for delays

GPIO.setwarnings(False)                  # turns off warnings
GPIO.setmode(GPIO.BCM)                   # usu fysical numbering

trig_links = 1                           # set trigger pin
trig_midden = 2                          # =
trig_rechts = 3                          # =
trig_achterkant = 4                      # =
echo_links = 5                           # set echo pin
echo_midden = 6                          # =
echo_rechts = 7                          # =
echo_achterkant = 8                      # =


GPIO.setup(trig_achterkant, GPIO.OUT)		     # set pin as output
GPIO.setup(trig_links, GPIO.OUT)		         # =
GPIO.setup(trig_midden, GPIO.OUT)                # =
GPIO.setup(trig_rechts, GPIO.OUT)		         # =
GPIO.setup(echo_achterkant, GPIO.IN)	    	 # set pin as input
GPIO.setup(echo_links, GPIO.IN)                  # =
GPIO.setup(echo_midden, GPIO.IN)                 # =
GPIO.setup(echo_rechts, GPIO.IN)                 # =


def ultrasonic(results):
    triggers = [trig_links, trig_midden, trig_rechts, trig_achterkant]         # list triggers
    echos = [echo_links, echo_midden, echo_rechts, echo_achterkant]            # list echos

    results = []                                                               # list for results
    def afstand(trigger, echo):                                                # calculates distance based on time between trigger and echo
       GPIO.output(trigger, True)                                              # turns on trigger
       time.sleep(0.00001)                                                     # delay
       GPIO.output(trigger, False)                                             # turns off trigger

       while GPIO.input(echo) == 0:                                            # while there is no echo signal
           puls_start = time.time()                                            # timer counts

       while GPIO.input(echo) == 1:                                            # same as above
           puls_end = time.time()                                              # timer stops

       puls_duration = puls_end - puls_start                                   # calc pulse duration

       afstand = puls_duration * 17150                                         # calc distance based on pulse duration

       afstand = round(afstand, 3)                                             # only 3 numbers

       results.append(afstand)                                                 # appends list of results with result distance

    afstand(triggers[0], echos[0])                                             # applies function on trigger and echo
    afstand(triggers[1], echos[1])                                             # =
    afstand(triggers[2], echos[2])                                             # =
    afstand(triggers[3], echos[3])                                             # =

    return results

    


