from workflows.first_workflow import my_task
from hatchet_client import hatchet
import asyncio

async def run_task():
    try:
        print("Running task...")
        result = await my_task.aio_run()
        print(f"Task result: {result}")
    except Exception as e:
        print(f"Error running task: {e}")

if __name__ == "__main__":
    asyncio.run(run_task())