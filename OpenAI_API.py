from openai import OpenAI
import os

client = OpenAI(
    api_key = ''
)

command = '''
[22/11/25, 6:23:20 PM] Rajat CSE Central University: ested haai pata nahi
[22/11/25, 6:23:29 PM] Rajat CSE Central University: Shubh
[22/11/25, 6:23:40 PM] Rajat CSE Central University: Saumya ye log ho sakte haai interested
[22/11/25, 6:23:57 PM] Divij Singh Soodan @David: shubh
[22/11/25, 6:24:25 PM] Rajat CSE Central University: Haai
[22/11/25, 6:24:39 PM] Divij Singh Soodan @David: voh chala gya bro
[22/11/25, 6:25:07 PM] Rajat CSE Central University: Ohh haa toh ghar mei haai.... sorry yaar help na kar saka tujhe
[25/11/25, 10:01:29 PM] Rajat CSE Central University: Give me your roll no
[25/11/25, 10:01:34 PM] Rajat CSE Central University: Official wala
[25/11/25, 10:04:42 PM] Rajat CSE Central University: Give me name also
[29/12/25, 7:37:29 PM] Divij Singh Soodan @David: Maine bhi dekhli
[29/12/25, 8:02:16 PM] Rajat CSE Central University: Sahi kia
[29/12/25, 8:07:55 PM] Rajat CSE Central University: Dhurandar dekha ??
'''

completion = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'system', 'content':'you are a person named David who speaks hindi as well as english and is a techie. he is from India and is a coder also. Analyze chat history and respond like harry.'},
        {'role': 'user', 'content':'what is coding'}
    ]
)

print(completion.choices[0].message)
