from prefect.run_configs import KubernetesRun
from prefect.storage import GitHub

from prefect import Flow, Parameter, task, context

STORAGE = GitHub(
    repo="TR1234567/prefect_k8s-docker_test",
    path=f"flow-of-flow/workflow/kubetest.py"
)

@task
def hello():
    logger = context.get("logger")
    logger.info("Hello kube!")

with Flow("flow-of-flow",storage=STORAGE,
        run_config = KubernetesRun(image="tr1234567/wf-test")) as flow:
    logger = context.get("logger")
    logger.info("start workflow")
    hello()
    logger.info("End")

flow.register(project_name="flow-of-flow")
    
