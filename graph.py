from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from state import BlogState
from nodes import (
    researcher_node,
    writer_node,
    editor_node,
    route_after_editor,
)


def build_graph():
    graph = StateGraph(BlogState)

    graph.add_node("researcher", researcher_node)
    graph.add_node("writer", writer_node)
    graph.add_node("editor", editor_node)

    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "writer")
    graph.add_edge("writer", "editor")

    graph.add_conditional_edges(
        "editor",
        route_after_editor,
        {
            "end": END,
            "writer": "writer",
        },
    )

    checkpointer = InMemorySaver()

    return graph.compile(checkpointer=checkpointer)


app = build_graph()