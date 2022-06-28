import prefect
from prefect import Task,Flow
from prefect.storage import GitHub
from prefect.run_configs import KubernetesRun
STORAGE = GitHub(
    repo="TR1234567/prefect_k8s-docker_test",
    path=f"flow-of-flow/workflow/flow2.py"
)


class sent_number(Task):
    def run(self,x=2):
        print(x)
        return x

s = sent_number()
with Flow("flow-of-flow2"
        ,storage=STORAGE
        ,run_config = KubernetesRun(image="tr1234567/wf-test")) as flow:
    print('start workflow')
    s1 = s()

flow.register(project_name="flow-of-flow")