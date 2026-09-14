from typing import Annotated
from typing_extensions import TypedDict
import operator


class BlogState(TypedDict):
    topic: str
    research: str
    draft: str
    feedback_history: Annotated[list[str], operator.add]
    approved: bool
    revision_count: int