
import prefect
from prefect import task, Flow

@task
def plus_one(x):
    logger = prefect.context.get("logger")
    logger.info("test1")
    return x + 1

with Flow("hello-flow") as flow:
    # image="test"))
    plus_one(1)