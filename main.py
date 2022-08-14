import sys
from traceback import print_tb
from unittest import result #Allows to kill program if wrong inpput
from colorama import * #Allows custom text color in terminal
import time
import random
import string
import datetime
from pyfiglet import figlet_format


print("""\


  /$$$$$$  /$$$$$$$$       /$$                 /$$                       /$$               /$$                    
 /$$__  $$|_____ $$/      |__/                | $$                      | $$              |__/                    
|__/  \ $$     /$$/        /$$ /$$$$$$$   /$$$$$$$ /$$   /$$  /$$$$$$$ /$$$$$$    /$$$$$$  /$$  /$$$$$$   /$$$$$$$
  /$$$$$$/    /$$/        | $$| $$__  $$ /$$__  $$| $$  | $$ /$$_____/|_  $$_/   /$$__  $$| $$ /$$__  $$ /$$_____/
 /$$____/    /$$/         | $$| $$  \ $$| $$  | $$| $$  | $$|  $$$$$$   | $$    | $$  \__/| $$| $$$$$$$$|  $$$$$$ 
| $$        /$$/          | $$| $$  | $$| $$  | $$| $$  | $$ \____  $$  | $$ /$$| $$      | $$| $$_____/ \____  $$
| $$$$$$$$ /$$/           | $$| $$  | $$|  $$$$$$$|  $$$$$$/ /$$$$$$$/  |  $$$$/| $$      | $$|  $$$$$$$ /$$$$$$$/
|________/|__/            |__/|__/  |__/ \_______/ \______/ |_______/    \___/  |__/      |__/ \_______/|_______/                                                                                                                                                                                                                                                                                                                                                   
               """)



#"L" is code
y = input(
    Fore.RED +"To access this program, you may have a code provided in the message we gave you, as well as the appointment code we may need later. "
     " Please put in the code " + Fore.RESET)
if (y == "ENTER") or "enter" or "Enter":
    print(Fore.BLUE + "Loading.....")
else:
     sys.exit()
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
countdown(1)

def get_random_string(length):
    letters = string.ascii_uppercase
    rno = ''.join(random.choice(letters) for i in range(length))
    print("Your unique reference code", "is:", rno)
get_random_string(6)
countdown(1)

name = input("Insert patient name " )
if (name == "Ray") or "ray": 
    print("  ")
else:
    print("You have put in the wrong name")
    sys.exit()
age = input("Please put in patient age here:" )
patient_status= input("Put in status: New or Old? ")
condition = "new" in patient_status.lower()
if condition: 
    print("You are a NEW patient!")
else: 
    print("You are an OLD patient" + Fore.RESET) 
#The code is "XYZ"
Date = input("Put in your unique access code " )
if Date == "XYZ":
    print("Your appointment date is on 27/11/24",)
else:
    print("Your code is incorrect, Maybe you put in another code by accident?",)
    sys.exit()

    
#Date sustem which calcuates appointment dates
Day = datetime.date(2022, 11, 27) - datetime.date.today() 
Day = str(Day)
print("Your appointment will be in " + Day.strip("0: ,"))
#2nd code is "ABC"
x = input("Do you have a second code that was provided? ")
if "yes" in x.lower():
 print("You may proceed")
 details1 = (age, patient_status , "Your appointment will be on:" + Day)
else: 
    print("Goodbye") 
    sys.exit()
print("You may request a new code that may speed up your date, in such case please insert the new code here")
print("ㅤㅤㅤㅤㅤㅤ")
print("Please wait for a moment before putting in a new code")
print("ㅤㅤㅤㅤㅤㅤ")
countdown(1)
Fore.RESET
Date2 = input(Fore.CYAN + "Put in the new code: ")
if Date2 == "ABC":
    print("Your appointment is on 17/8/22")
else:
        print("The code you put in was icorrect.")
        sys.exit()
Day2 = datetime.date(2022, 8, 17) - datetime.date.today() 
Day2 = str(Day2)
print("Your appointment will be in " + Day2.strip("0: ,"))
details = (name, age, patient_status,"Appointment in:" + Day2.strip("0: ,"))
# Note: if **input** won't ever work as thats a function, i named the variable "a" , hence "if a=..."
a = input("do you want ur Details? (Input Yes or No) ")
if a == "Yes": 
    print(details)
else : 
    countdown(3)
    print("""\

.d8888. d88888b .d8888. .d8888. d888888b  .d88b.  d8b   db      d888888b d88888b d8888b. .88b  d88. d888888b d8b   db  .d8b.  d888888b d88888b d8888b. 
88'  YP 88'     88'  YP 88'  YP   `88'   .8P  Y8. 888o  88      `~~88~~' 88'     88  `8D 88'YbdP`88   `88'   888o  88 d8' `8b `~~88~~' 88'     88  `8D 
`8bo.   88ooooo `8bo.   `8bo.      88    88    88 88V8o 88         88    88ooooo 88oobY' 88  88  88    88    88V8o 88 88ooo88    88    88ooooo 88   88 
  `Y8b. 88~~~~~   `Y8b.   `Y8b.    88    88    88 88 V8o88         88    88~~~~~ 88`8b   88  88  88    88    88 V8o88 88~~~88    88    88~~~~~ 88   88 
db   8D 88.     db   8D db   8D   .88.   `8b  d8' 88  V888         88    88.     88 `88. 88  88  88   .88.   88  V888 88   88    88    88.     88  .8D 
`8888Y' Y88888P `8888Y' `8888Y' Y888888P  `Y88P'  VP   V8P         YP    Y88888P 88   YD YP  YP  YP Y888888P VP   V8P YP   YP    YP    Y88888P Y8888D' 
""")