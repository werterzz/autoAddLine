import openpyxl
import pyautogui
import time
from pathlib import Path

xlsx_file = Path('./', 'phoneNumber.xlsx')
wb_obj = openpyxl.load_workbook(xlsx_file) 

# Read the active sheet:
sheet = wb_obj.active

arr = []

for row in sheet.values:
   for value in row:
    #  print(value)
     arr.append(value)

print(arr)

for i in range(len(arr)):
    pyautogui.click('./images/searchForFriendBtn.png')
    time.sleep(2)
    pyautogui.click('./images/phoneNumberBtn.png')
    pyautogui.write(arr[i])
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    try:
        pyautogui.click('./images/addBtn.png')
    except:
        pyautogui.click('./images/okBtn.png')
        time.sleep(3)
        # below function find two close button you can get on array or use can capture
        # new image with more detail and more position on x,y (old close button 
        # has just close button but new close button has text and close button)
        x, y = pyautogui.locateOnScreen('./images/closeBtn.png', confidence=0.9)
    time.sleep(10)

# pyautogui.click('./images/closeBtn.png')