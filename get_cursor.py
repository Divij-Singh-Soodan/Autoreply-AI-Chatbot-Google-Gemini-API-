import pyautogui
import time

print("Move mouse over the WhatsApp text... (Press Ctrl+C to stop)")

try:
    while True:
        # Get and print current mouse coordinates
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)
        
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print('\nDone.')