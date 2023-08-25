import RPi.GPIO as GPIO
import RPi_I2C_driver

import time

class Tumbler:
    def __init__(self):
        self.down_pin_left = 18
        self.down_pin_right = 4
        self.trig_pin = 19
        self.echo_pin = 26

        self.lcd = RPi_I2C_driver.lcd(0X27)
        self.lcd.clear()

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.down_pin_left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.down_pin_right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        
        # Menu status
        self.status_main = 1
        self.status_accept = -1
        self.status_next = -1

    def printLCD(self, cursor: int = 0, text: str = ""):
        lcd_cell = 16
        text_len = len(text)
        gap_1 = gap_2 = ""
        
        if text_len % 2 == 1 and lcd_cell > text_len:
            gap_1 = lcd_cell - text_len
            gap_2 = " " * (int(gap_1/2) + 1)
            gap_1 = " " * int(gap_1/2)
        elif lcd_cell >= text_len:
            gap_1 = lcd_cell - text_len
            gap_1 = " " * int(gap_1/2)
            
        text = gap_1 + text + gap_2
        
        self.lcd.setCursor(0, cursor)
        self.lcd.print(text)

    def printDistance(self) -> float:
        GPIO.output(self.trig_pin, GPIO.LOW)
        time.sleep(0.00001)
        GPIO.output(self.trig_pin, GPIO.HIGH)

        start = time.time()
        stop = time.time()
        
        while GPIO.input(self.echo_pin) == 0:
            start = time.time()

        while GPIO.input(self.echo_pin) == 1:
            stop = time.time()

        rtTotime = stop - start
        distance = rtTotime * (34000 / 2)
        
        return distance
    
    def waterCheck(self, distance) -> float:
        PI = 3.14
        RADIUS = 4.72
        HEIGHT = 15.5
        water = (HEIGHT-distance)*(RADIUS**2)*PI
        return water
        
    def menuSelect(self):
        if self.status_accept == 0:
            print(0)
        elif self.status_accept == 1:
            print(1)
            
    def mainControl(self):
        """버튼에 따른 LCD 패널 통제 메소드입니다

        Returns:
            tuple: (top_text, buttom_text)
        """
        distanc = tumbler.printDistance()
        basic_up = ("Water : %.2f ml" %distanc)
        basic_down = "Click to Next"
        
        status_2_up = "select coffee"
        
        status_3_up = "Caffeine Check"
        
        status_4_up = "reset weater?"
        status_4_down_1 = " o yes  |   no"
        status_4_down_2 = "   yes  | o no"
        
        if self.status_main == 1 and self.status_next < 1 and self.status_accept < 1:
            return (basic_up, basic_down)
        
        elif self.status_next <= 1 and self.status_accept <= 1 and self.status_main == 1:
            self.status_main = 2
            self.status_next = self.status_accept = 0
        
            return (status_2_up, self.coffee_text()[0])
        
        elif self.status_next >= 0 and self.status_main == 2 and self.status_accept == 0:
            text_coffee = self.coffee_text(self.status_next)[0]
            text_coffee = "o  " + text_coffee + "  o"
        
            return (status_2_up, text_coffee)
        
        elif self.status_accept < 1 and self.status_next < 1 and self.status_main <= 3:
            self.status_accept = 0
            self.status_next = 0
            self.status_main = 3
            text_coffee = self.coffee_text(self.status_next)
            Caffeine = distanc * text_coffee[1]
            text_coffee = text_coffee[0] + str(Caffeine) + "mg"
        
            return (status_3_up, basic_down)
        
        elif self.status_accept >= 1 and self.status_main == 3:
            self.status_main = 4
            self.status_next = self.status_accept = 0
            return (status_4_up, status_4_down_1)
        
        elif self.status_next % 2 == 0 and self.status_main == 3 and self.status_accept == 0:
            return (status_4_up, status_4_down_2)
        
        elif self.status_next % 2 != 0 and self.status_main == 3 and self.status_accept == 0:
            return (status_4_up, status_4_down_1)
        
        elif self.status_next % 2 == 0 and self.status_main == 3 and self.status_accept >= 1:
            self.status_main = 1
            self.status_next = 0
            self.status_accept = 0
            
            return (basic_up, basic_down)
        
        elif self.status_next % 2 != 0 and self.status_main == 4 and self.status_accept >= 1:
            self.status_main = 2
            self.status_next = 0
            self.status_accept = 0
            
            return (status_3_up, basic_down)
        else:
            
            return ("error : accept - "+str(self.status_accept), "main - "+str(self.status_main))         
    
    def coffee_text(self, menu: int = 0):
        """숫자에 따른 커피명과 카페인 함량을 반환합니다

        Args:
            menu (int): 메뉴 숫자값. defult=0

        Returns:
            tuple(str, int): ("커피명", g당 카페인 함량)
        """
        if menu == 0:
            return "Americano", 0.42
        elif menu == 1:
            return "Espresso", 1.69
        elif menu == 2:
            return "Macchiato", 0.21, 
        elif menu == 3:
            return "Cappucino", 0.21
        elif menu == 4:
            return "CafeLatte", 0.21
        elif menu == 5:
            return "CafeMocha", 0.26
        else:
            self.status_next = 0
            return "Americano", 0.42
        
        
if __name__ == "__main__":
    tumbler = Tumbler()

    next_dump = 0
    accept_dump = 0
    
    input_next = GPIO.input(tumbler.down_pin_left)
    input_accept = GPIO.input(tumbler.down_pin_right)
    
    try:
        # get button status
        while True:
            input_next = GPIO.input(tumbler.down_pin_left)
            input_accept = GPIO.input(tumbler.down_pin_right)
            
            if input_next != next_dump:
                print("click next button!", input_next, " | next: ", tumbler.status_next, " | main: ",tumbler.status_main, " | accept: ",tumbler.status_accept)
                tumbler.status_next += 1
            
            text_left = tumbler.mainControl()

            tumbler.printLCD(cursor=0, text=text_left[0])
            tumbler.printLCD(cursor=1, text=text_left[1])
            
            
            if input_accept != accept_dump:
                print("click accept button!", input_accept, " | next: ", tumbler.status_next, " | main: ",tumbler.status_main, " | accept: ",tumbler.status_accept)
                tumbler.status_accept += 1

            # save button status
            next_dump = input_next
            accept_dump = input_accept
            
            text_left = tumbler.mainControl()
            
            tumbler.printLCD(cursor=0, text=text_left[0])
            tumbler.printLCD(cursor=1, text=text_left[1])
                        
    except KeyboardInterrupt:
        GPIO.cleanup()