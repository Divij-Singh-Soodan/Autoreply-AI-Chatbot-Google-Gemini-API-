import pyautogui
import pyperclip
import time
import google.generativeai as genai

# --- CONFIGURATION ---
GEMINI_API_KEY = "" #from Google AI servers
genai.configure(api_key=GEMINI_API_KEY)

# Use the latest stable model
model = genai.GenerativeModel('gemini-2.5-flash')


# Your confirmed coordinates
start_x, start_y = 500, 232  
end_x, end_y = 526, 1047    
input_box_x, input_box_y = 807, 1074

last_replied_content = ""

print("Bot starting... Switch to WhatsApp!")
time.sleep(5)


while True:
    try:
        # 1. Capture Text
        pyautogui.moveTo(start_x, start_y)
        pyautogui.dragTo(end_x, end_y, duration=1.0, button='left')
        pyautogui.hotkey('command', 'c')
        time.sleep(1.0) 

        chat_data = pyperclip.paste().strip()

        if chat_data and chat_data != last_replied_content:
            print("\n--- NEW CHAT DETECTED ---")
            
            # 2. AI Generation
            prompt = f"You are David, a techie from India. Respond in Hinglish to this chat as Harry: {chat_data}"
            response = model.generate_content(prompt)
            bot_reply = response.text
            
            
            #Bot Reply after understanding the context from AI.
            print(f"Attempting to send: {bot_reply[:30]}...")
            
            
            # Copy reply to clipboard
            pyperclip.copy(bot_reply)
            
            # POWER CLICK: Triple click the input box to force macOS to focus there
            pyautogui.click(x=input_box_x, y=input_box_y, clicks=3, interval=0.1, button='left')
            time.sleep(1.0) # Wait for the cursor to definitely appear
            
            # PASTE
            pyautogui.hotkey('command', 'v')
            time.sleep(0.8) # Wait for text to actually appear in the box
            
            # SEND
            pyautogui.press('enter')
            print("Reply Sent!")
            
            last_replied_content = chat_data 
        
        else:
            print("No new messages...", end='\r')

        time.sleep(10) 

    except Exception as e:
        print(f"\nError: {e}")
        time.sleep(5)