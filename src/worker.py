from hatchet_client import hatchet
from workflows.first_workflow import my_task


def main() -> None:
    print(f"Registering task: {my_task}")
    print(f"Task type: {type(my_task)}")
    worker = hatchet.worker("test-worker", slots=1, workflows=[my_task])
    print("Worker created, starting...")
    worker.start()


if __name__ == "__main__":
    main()
