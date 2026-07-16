import os
from dotenv import load_dotenv
from pathlib import Path
from groq import Groq


load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("No api key found")

client = Groq(api_key=my_api_key)

model = "llama-3.3-70b-versatile"

role = "user"

prompt = "Suggest a name of my website that list the jobs from various website using api which help to get the job to the job seekers . suggest one name only"


message_system = {
    "role":"system",
    "content":"You are my brand manager who suggest name for my website of job . name should be in one word"
}
message = {
    "role":role,
    "content":prompt
}

messages =[message_system,message]

response = client.chat.completions.create(model=model,messages=messages,temperature=2)

answere = response.choices[0].message.content
print(answere)