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
        ## 1. Rerun in VS Code Terminal (Without Docker)




# ```cmd
# # Navigate to your project folder
# cd /d F:\Desktop\project_completed\langraph_blog_agent

# # Start the FastAPI server using your local Python environment
# python main.py

# # In another VS Code terminal, run the API testing script
# python test_api.py

# # Type a topic when prompted. Type 'exit' to stop the testing script.
# ```

# ## 2. Rerun in CMD (With Docker)

# ```cmd
# :: Navigate to your project folder
# cd /d F:\Desktop\project_completed\langraph_blog_agent

# :: Start the Docker container and FastAPI server
# :: Map port 8000 and load API credentials from .env
# docker run --rm -p 8000:8000 --env-file .env ai-blog-writer

# :: In a second CMD window, test the API with a POST request
# curl -X POST http://127.0.0.1:8000/blog -H "Content-Type: application/json" -d "{\"topic\":\"Machine Learning\"}"

# :: To stop the Docker container, press Ctrl+C in the server window
# ```

# **Note:** For the VS Code method, keep the server running in one terminal and run `python test_api.py` in a second terminal. For Docker, keep the container running in one CMD window and send the `curl` request from another.
