from prefect import task
from prefect.engine import TaskRunner


@task
def number_task():
    logger = prefect.context["logger"]
    logger.info("Hello!")
    return 42


with  Flow("hello-flow") as flow 
    f.add_task(number_task)
