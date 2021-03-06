import prefect
from prefect import Task, context, Flow
import time
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun
from prefect import Parameter
STORAGE = GitHub(
    repo="TR1234567/prefect_k8s-docker_test",
    path=f"flow-of-flow/workflow/flow3.py"
)

class sent_number(Task):
    def run(self,x=10000):
        
        time.sleep(5)
        

        return x

s = sent_number()
with Flow("flow-of-flow3"
        ,storage=STORAGE
        , run_config =KubernetesRun(image="tr1234567/wf-test")) as flow:
    print('start workflow')
    logger = context.get("logger")
    logger.info("Start wait")
    number = Parameter("x", default="10")
    s1 = s(number)
    logger.info("Finnish")
    print(s1)

flow.register(project_name="flow-of-flow")