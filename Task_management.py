class Task():
    def __init__(self, title, open_date,due_date,task_owner,sprint):
        self.title = title
        self.open_date = open_date
        self.due_date = due_date
        self.task_owner = task_owner
        self.sprint = sprint
class WorkTask(Task):
    def __init__(self,title, open_date,due_date,task_owner,reviewer,sprint):
        self.reviewer = reviewer
        super().__init__(title, open_date,due_date,task_owner,sprint)
class Team():
    def __init__(self,name,member_count):
        self.name = name
        self.member_count = member_count
        self.tasks = []
    def add_task(self,task_obj):
        self.tasks.append(task_obj)
    def show_tasks(self):
        for task in self.tasks:
            print(task)

class PersonalTask(Task):
    def __init__(self, title, open_date,due_date,task_owner,sprint):
        super().__init__(title, open_date,due_date,task_owner,sprint)


task_1=WorkTask("Task 1",'1405/04/01','1405/04/03','Roya','bahar','pasargad_bank')
team_1=Team("Team 1",1)
team_1.add_task(task_1)
team_1.show_tasks()
