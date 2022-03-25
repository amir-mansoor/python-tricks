import pyautogui as spam
import time
import random

limit = input("Enter the limit of the messages: ")

time.sleep(5)

for i in range(int(limit)):
    msgs = ["Fucker", "Chutiye", "Kameene", "BSDK", "Choronga nahe tere ko","Wo hal karonga tera", "Saale", "School k ba goro","Bakhti","Jhooti"]
    msg = random.choice(msgs)
    spam.typewrite(msg)
    spam.press("Enter")
