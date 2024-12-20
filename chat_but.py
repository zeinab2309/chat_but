import pyautogui as pg
#برای مطالعه و اطلاعات بیشتر درباره کتبخانه بالا از سایت زیر استفاده کنید
# https://pyautogui.readthedocs.io/en/latest/
from datetime import datetime
from time import sleep
from random import choice
today = datetime.now().strftime("%Y-%m-%d")
lst=[f"would you like to talk to me?",
     "how are you?",
     f"today is :{today}","good day",
     "Do you have a question to ask me?",
     "I wish you happiness"]
pg.click(530, 999)
pg.write("hello i,m robot \nwhat,s your name? (enter your name in english )\n", interval=0.02)
pg.hotkey('ctrl','enter')
name=input("your name: ")
pg.click(530, 999)
pg.write(f"hi {name}", interval=0.1)
pg.press('enter')
for i in range(5):
    sleep(0.5)
    pg.click(530, 999)
    pg.write(choice(lst), interval=0.1)
    pg.hotkey('ctrl','enter')
