from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD

password = []

lcd = LCD.lcd()
lcd.lcd_clear()

def key_pressed(key):
    global password
    password.append(key)

    print(password)

def out_thread():
    global password
    outputstr = ""
    numoftries = 0
    
    while(True):
        while(numoftries != -1):
            
            if len(password) > 0:       #clear second row
                print("cleared")
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Lock", 1)
            

            while(len(password) > 0 and numoftries != -1):

                while(len(outputstr) < len(password)):          #REQ02
                    outputstr += "*"
                    lcd.lcd_display_string("Safe Lock", 1) 
                    lcd.lcd_display_string(outputstr, 2)    
                    
                if len(password) == 4 and numoftries < 3:
                    if password == [1,2,3,4]: #assume that password is 1,2,3,4    #REQ03
                        print("correct")
                        numoftries = -1

                    else:                                       #REQ04
                        print("wrong")
                        outputstr = ""
                        password = []
                        
                        numoftries += 1
                        lcd.lcd_clear()
                        lcd.lcd_display_string("Wrong PIN", 1)

            if numoftries == 3:                   #REQ05
                print("disabled")
                lcd.lcd_clear()
                while(True):
                    lcd.lcd_display_string("Safe Disabled", 1)    

            elif numoftries == -1:                #REQ03
                lcd.lcd_clear()
                lcd.lcd_display_string("Safe Unlocked", 1)
                lcd.lcd_display_string("", 2)

        while(numoftries == -1):
            if '*' in password:         #lock safe
                outputstr = ""
                numoftries = 0
                password = []
                
                print("lock")

                lcd.lcd_display_string("Safe Lock", 1)
                lcd.lcd_display_string("Enter PIN:", 2)




def main():
    lcd = LCD.lcd()
    lcd.lcd_clear()

    lcd.lcd_display_string("Safe Lock", 1)
    lcd.lcd_display_string("Enter PIN:", 2)