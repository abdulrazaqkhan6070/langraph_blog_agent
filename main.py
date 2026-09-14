from fastapi import FastAPI
from pydantic import BaseModel

from graph import app


api = FastAPI(title="AI Blog Writer API")


class BlogRequest(BaseModel):
    topic: str


@api.post("/blog")
def create_blog(request: BlogRequest):

    config = {
        "configurable": {
            "thread_id": "api-blog-1"
        }
    }

    initial_state = {
        "topic": request.topic,
        "research": "",
        "draft": "",
        "feedback_history": [],
        "approved": False,
        "revision_count": 0,
    }

    for _event in app.stream(
        initial_state,
        config,
        stream_mode="updates",
    ):
        pass

    final_state = app.get_state(config)

    return {
        "topic": request.topic,
        "draft": final_state.values["draft"],
        "approved": final_state.values["approved"],
        "revision_count": final_state.values["revision_count"],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        api,
        host="127.0.0.1",
        port=8000
    )

# & "C:\Program Files\Python314\python.exe" main.py(terminal 1)
# & "C:\Program Files\Python314\python.exe" test_api.py(terminal 2)