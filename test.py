
import prefect
from prefect import task, Flow

@task
my_shell = ShellTask(shell="bash")

with Flow("hello-flow") as flow:
    task1 = my_shell(command="ls")
