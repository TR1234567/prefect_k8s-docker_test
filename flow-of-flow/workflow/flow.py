from prefect import Flow, Parameter, task, context
from prefect.tasks.prefect import create_flow_run, wait_for_flow_run
from prefect.run_configs import KubernetesRun
from prefect.storage import GitHub
import sys
sys.path.append('./')
from component import *
from prefect import Parameter

STORAGE = GitHub(
    repo="TR1234567/prefect_k8s-docker_test",
    path=f"flow-of-flow/workflow/flow.py"
)

@task
def plus_show(x,y):
    logger = context.get("logger")
    r = x + y
    print(r)
    logger.info(f"{r}")
    return r
    

with Flow("flow-of-flow",storage=STORAGE,
        run_config = KubernetesRun(image="tr1234567/wf-test")) as flow:
    print('start workflow')
    logger = context.get("logger")
    fl1 = create_flow_run(flow_name="flow-of-flow1")
    fl2 = create_flow_run(flow_name="flow-of-flow2")
    f = plus_show(fl1 , fl2 )

    logger.info(f"{f}")
    
    fl3 = create_flow_run(flow_name="flow-of-flow3")
    fl4 = create_flow_run(flow_name="flow-of-flow3")
    g = plus_show(f,fl3)
    h = plus_show(g,fl4)
    logger.info(f"{g}")


    

flow.register(project_name="flow-of-flow")