from prefect.run_configs import KubernetesRun
from prefect.storage import Local

from prefect import Flow, Parameter, task, context



@task
def hello():
    return '1'

with Flow("flow-of-flow",storage=Local(path='app/workflow/kubetest.py'),
        run_config = KubernetesRun(image="tr1234567/wf-test",labels=[])) as flow:
    logger = context.get("logger")
    logger.info("start workflow")
    r = hello()
    logger.info(r"Hello kube {}".format(r))
    logger.info("End")

flow.register(project_name="flow-kube")
    
