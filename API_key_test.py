from openai import OpenAI, RateLimitError

# REPLACE WITH YOUR NEW KEY
client = OpenAI(api_key="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") 

try:
    print("Testing key...")
    client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello"}]
    )
    print("✅ SUCCESS: The key works! You have credits.")
    
except RateLimitError:
    print("❌ FAILED: The key is valid, but you have $0 credits.")
except Exception as e:
    print(f"❌ ERROR: {e}")
    
#we are directly connecting to OpenAI servers to check for the API key 
#used for various software projects

