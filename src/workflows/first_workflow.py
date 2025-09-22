from hatchet_sdk import Context
from hatchet_client import hatchet
from pydantic import BaseModel


class SimpleOutput(BaseModel):
    meaning_of_life: int


@hatchet.task(name="first-task")
def my_task(ctx: Context) -> SimpleOutput:
    print("executed task")
    return SimpleOutput(meaning_of_life=42)
