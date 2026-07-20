from groq import Groq
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def get_weather(city):
    return "Sunny, 25°C"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city name"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


def run_agent(question):
    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        tools=tools
    )
    message = response.choices[0].message
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        city = eval(tool_call.function.arguments)["city"]
        weather = get_weather(city)
        print(f"Tool called: get_weather({city}) → {weather}")
        return f"Weather in {city}: {weather}"
    else:
        return message.content

print(run_agent("What is the weather in Berlin?"))
result = run_agent("What is the weather in Berlin?")
print("Result:", result)


