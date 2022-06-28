import prefect
from prefect import Task, context, Flow
import time
from prefect.storage import Local
from prefect.run_configs import KubernetesRun
from prefect import Parameter


class sent_number(Task):
    def run(self,x=10000):
        
        time.sleep(5)
        

        return x

s = sent_number()
with Flow("flow-of-flow3"
        ,storage=Local(path="/app/component/flow3.py",stored_as_script=True)
        , run_config =KubernetesRun(image="flow-of-flow")) as flow:
    print('start workflow')
    logger = context.get("logger")
    logger.info("Start wait")
    number = Parameter("x", default="10")
    s1 = s(number)
    logger.info("Finnish")
    print(s1)

flow.register(project_name="flow-of-flow")