import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

load_dotenv()


gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0
)


groq_llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)


def call_llm(prompt: str) -> str:

    try:
        print("Trying Gemini...")

        response = gemini_llm.invoke(prompt)

        content = response.content

        if isinstance(content, list):
            return "".join(
                item.get("text", "") if isinstance(item, dict) else str(item)
                for item in content
            )

        return str(content)

    except Exception as e:

        print("Gemini failed. Switching to Groq...")
        print("Reason:", e)

        response = groq_llm.invoke(prompt)

        return str(response.content)