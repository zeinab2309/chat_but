import pyautogui as pg
#برای مطالعه و اطلاعات بیشتر درباره کتبخانه بالا از سایت زیر استفاده کنید
# https://pyautogui.readthedocs.io/en/latest/
from time import sleep
from random import choice
lst=["would you like to talk to me?","how are you?","good day","I wish you happiness"]
pg.click(530, 999)
pg.write("slam i,m robot \n", interval=0.1)
for i in range(5):
    sleep(0.1)
    pg.click(530, 999)
    pg.write(choice(lst), interval=0.1)
    pg.press('enter')
pg.hotkey('ctrl','enter')
