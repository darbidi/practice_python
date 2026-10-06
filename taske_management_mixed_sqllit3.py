import sqlite3
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
        self.task_type="worktask"
        super().__init__(title, open_date,due_date,task_owner,sprint)

class PersonalTask(Task):
    def __init__(self, title, open_date,due_date,task_owner,sprint):
        self.task_type="personaltask"
        self.reviewer = None
        super().__init__(title, open_date,due_date,task_owner,sprint)
class Team():
    def __init__(self,team_id,name,member_count):
        self.name = name
        self.member_count = member_count
        self.team_id = team_id
        self.tasks = []
    def add_task(self,task_obj):
        self.tasks.append(task_obj)
        # ۱. اتصال به دیتابیس (اگر فایلی به این اسم نباشه، خودش همون لحظه می‌سازدش)
        conn = sqlite3.connect('task_manager.db')
        # ۲. ساخت یک کرسر (Cursor) - کرسر مثل یک ربات نامه‌رسانه که دستورات SQL ما رو می‌بره تو دیتابیس اجرا می‌کنه
        cursor = conn.cursor()
        cursor.execute(
            '''insert into Task( task_type, title, open_date, due_date, task_owner, sprint, reviewer, team_id)
               values ( ?, ?, ?, ?, ?, ?, ?, ?)''',
            ( task_obj.task_type, task_obj.title, task_obj.open_date, task_obj.due_date, task_obj.task_owner, task_obj.sprint, task_obj.reviewer,self.team_id))
        conn.commit()
        conn.close()
        print(f"تسک '{task_obj.title}' به صورت خودکار در دیتابیس ذخیره شد! ")
    def show_tasks(self):
        for task in self.tasks:
            print(task)

task_1=WorkTask("Task 1",'1405/04/01','1405/04/03','Roya','bahar','pasargad_bank')
team_1=Team(1,"Team 1",1)
team_1.add_task(task_1)


