from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq
import os
import json
import pandas as pd
from typing import List
import traceback


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
app = FastAPI()

class Resumeinput(BaseModel):
    resume_input: str


class AnalyseOutput(BaseModel):
    skills: list[str]
    years_of_experience: int
    top3_strengths: list[str]

@app.post("/analyse")
def analyse(data: Resumeinput):
    try:
        prompt = f"""Extract information from this resume and respond in JSON only with exactly these fields:
        {{
            "skills": ["skill1", "skill2"],
            "years_of_experience": 5,
            "top_3_strengths": ["strength1", "strength2", "strength3"]
        }}

        Resume: {data.resume_input}"""

        response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[
        {"role": "system", "content": "You are a resume analyser. Respond in JSON only."},
        {"role": "user", "content": prompt}
        ]
        )


        content = response.choices[0].message.content
        content = content.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        result = json.loads(content)
        # CSV logging goes here
        log_row ={
        "resume": data.resume_input,
        "skills": result["skills"],
        "years_of_experience": result["years_of_experience"],
        "top_3_strengths": result["top_3_strengths"]
        }
        
        if os.path.exists("day14/logs.csv"):
            try:
                df = pd.read_csv("day14/logs.csv")
            except:
                df = pd.DataFrame(columns=["resume", "skills", "years_of_experience", "top_3_strengths"])
        else:
            df = pd.DataFrame(columns=["resume", "skills", "years_of_experience", "top_3_strengths"])


        df = pd.concat([df, pd.DataFrame([log_row])], ignore_index=True)
        df.to_csv("day14/logs.csv", index=False)

        return result
    
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}
