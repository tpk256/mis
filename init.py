from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Subject, Question, Teacher, Topic, subject_teacher_association


engine = create_engine('postgresql://admin:admin@postgres/mydatabase')
Base.metadata.create_all(engine)
ses = sessionmaker(bind=engine)()

for i in range(10):
    sub = Subject(title=str(i) + " - sub")
    ses.add(sub)
    teachers = []
    for j in range(i):
        teachers.append(Teacher(name=f"Анна Петровна {j}"))

    ses.commit()
    for t in teachers:
        t.subjects.append(sub)
        ses.add(t)

    ses.commit()

    topic = Topic(title="New topic", subject_id=sub.id)
    ses.add(topic)
    ses.commit()

    que = Question(text="text", ans="ans", topic_id=topic.id)
    ses.add(que)
    ses.commit()
