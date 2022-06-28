import prefect
from prefect import Task,Flow
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun
STORAGE = GitHub(
    repo="TR1234567/prefect_k8s-docker_test",
    path=f"flow-of-flow/workflow/{FLOW_NAME}.py"
)


class sent_number(Task):
    def run(self,x=2):
        print(x)
        return x

s = sent_number()
with Flow("flow-of-flow2"
        ,storage=Local(path=STORAGE,stored_as_script=True)
        ,run_config = KubernetesRun(image="flow-of-flow")) as flow:
    print('start workflow')
    s1 = s()

flow.register(project_name="flow-of-flow")