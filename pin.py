import RPi.GPIO as GPIO


class Pin():
    def __init__(self):
        ######################
        # CONSTANTS FOR GPIO #
        ######################
        self.pins = [5, 6, 13, 16, 19, 20, 21, 26]
        
        #################
        # GPIO SETTINGS #
        #################

        GPIO.setmode(GPIO.BCM)
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            
                    
    def offAll(self) -> None:
        """Off all reley.
        """
        for pin in self.pins:
            GPIO.output(pin, GPIO.HIGH)
            
    
    def onAll(self) -> None:
        """On all reley.
        """
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)
            
    
    def offPin(self, pin: int) -> None:
        """Off the reley.

        Args:
            pin (int): Possible values: [5, 6, 13, 16, 19, 20, 21, 26].
        """
        GPIO.output(pin, GPIO.HIGH)
        
    
    def onPin(self, pin: int) -> None:
        """On the reley.

        Args:
            pin (int): Possible values: [5, 6, 13, 16, 19, 20, 21, 26].
        """
        GPIO.output(pin, GPIO.LOW)