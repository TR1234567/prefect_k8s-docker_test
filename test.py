from prefect import task
from prefect.engine import TaskRunner


@task
def number_task():
    logger = prefect.context["logger"]
    logger.info("Hello!")
    return 42

runner = TaskRunner(task=number_task)
state = runner.run()