import prefect
from prefect import Task,Flow
from prefect.storage import Local
from prefect.run_configs import KubernetesRun



class sent_number(Task):
    def run(self,x=2):
        print(x)
        return x

s = sent_number()
with Flow("flow-of-flow2"
        ,storage=Local(path="/app/component/flow2.py",stored_as_script=True)
        ,run_config = KubernetesRun(image="flow-of-flow")) as flow:
    print('start workflow')
    s1 = s()

flow.register(project_name="flow-of-flow")