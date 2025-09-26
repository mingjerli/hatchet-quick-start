from hatchet_sdk import Context
from hatchet_client import hatchet
from pydantic import BaseModel


class SimpleOutput(BaseModel):
    meaning_of_life: int


@hatchet.task(name="first-task")
def my_task(workflow_input, ctx: Context) -> SimpleOutput:
    print("executed task")
    print(f"workflow input: {workflow_input}")
    print(f"context: {ctx}")
    return SimpleOutput(meaning_of_life=542)
