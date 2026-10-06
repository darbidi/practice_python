import sqlite3
# ۱. اتصال به دیتابیس (اگر فایلی به این اسم نباشه، خودش همون لحظه می‌سازدش)
conn=sqlite3.connect('task_manager.db')
# ۲. ساخت یک کرسر (Cursor) - کرسر مثل یک ربات نامه‌رسانه که دستورات SQL ما رو می‌بره تو دیتابیس اجرا می‌کنه
cursor=conn.cursor()
# ۳. نوشتن و اجرای دستور SQL
# از سه تا کوتیشن (''') استفاده می‌کنیم تا بتونیم کوئری رو تو چند خط تمیز بنویسی
cursor.execute('''create table if not exists Team(
                  team_id integer primary key,
                  name text,
                  member_count integer)''')

cursor.execute('''create table if not exists Task(
                    task_id integer primary key,
                    task_type text,
                    title text,
                    open_date text,
                    due_date text,
                    task_owner text,
                    sprint integer,
                    reviewer text,
                    team_id integer
                   )''')

cursor.execute('''insert into Task(task_id, task_type ,title,open_date,due_date,task_owner,sprint,reviewer,team_id)
                                   values ( ?,?,?,?,?,?,?,?,?)''',(105,'worktask','Task 1', '1405/04/01', '1405/04/03', 'Roya', 2, 'bahar', 1))
cursor.execute('''select * from Task''')
all_tasks=cursor.fetchall()
#print(all_tasks)
for task in all_tasks:
    print(task)
conn.commit()

conn.close()

print("دیتابیس و جدول با موفقیت ساخته شدند!")
