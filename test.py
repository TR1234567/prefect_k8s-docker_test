
import prefect
from prefect import task, Flow

@task
def show():
    logger = prefect.context.get("logger")
    logger.info("flow run ")

with Flow("hello-flow") as flow:
    # image="test"))
    show()