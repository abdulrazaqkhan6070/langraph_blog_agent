from state import BlogState
from llm import call_llm


def researcher_node(state: BlogState) -> BlogState:
    topic = state["topic"]

    prompt = f"""
    Find a few useful facts about '{topic}'
    that can be used to write a short blog post.
    """

    result = call_llm(prompt)

    return {"research": result}


def writer_node(state: BlogState) -> BlogState:
    topic = state["topic"]
    research = state["research"]
    feedback_history = state["feedback_history"]

    feedback_text = ""

    if feedback_history:
        feedback_text = (
            f"Previous feedback to address: {feedback_history[-1]}"
        )

    prompt = f"""
    Write a short blog post (3-4 sentences) about '{topic}'.

    Use this research:
    {research}

    {feedback_text}
    """

    result = call_llm(prompt)

    return {"draft": result}


def editor_node(state: BlogState) -> BlogState:
    draft = state["draft"]

    prompt = f"""
    You are a strict editor. Review this blog post draft:

    ---
    {draft}
    ---

    If it's good enough to publish, reply with exactly:
    APPROVED

    If it needs improvement, reply with exactly:
    REVISE: <one-sentence feedback>
    """

    response = call_llm(prompt)
    current_count = state.get("revision_count", 0)

    if response.strip().startswith("APPROVED"):
        return {
            "approved": True,
            "revision_count": current_count + 1,
        }

    feedback = response.replace("REVISE:", "").strip()

    return {
        "feedback_history": [feedback],
        "approved": False,
        "revision_count": current_count + 1,
    }


def route_after_editor(state: BlogState) -> str:

    if state["approved"]:
        return "end"

    if state["revision_count"] >= 3:
        print("Max revisions reached — publishing best available draft.")
        return "end"

    return "writer"