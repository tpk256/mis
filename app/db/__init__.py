from sqlalchemy.orm import Session

from .models import Subject, Topic, Teacher, Question
from models import (Subject as SubjectPyDantic,
                    Teacher as TeacherPyDantic,
                    Topic as TopicPyDantic,
                    Question as QuestionPyDantic)


def get_subjects_pydantic(db: Session) -> list[SubjectPyDantic]:
    subjects = db.query(Subject).all()
    return [SubjectPyDantic.from_orm(subject) for subject in subjects]


def get_topics_pydantic(db: Session, subject_id: int) -> list[TopicPyDantic]:
    topics = db.query(Topic).filter(Topic.subject_id == subject_id).all()
    return [TopicPyDantic.from_orm(topic) for topic in topics]


def get_teachers_pydantic(db: Session, subject_id) -> list[TeacherPyDantic]:
    subject = db.query(Subject).filter(Subject.id == subject_id).first()
    return [TeacherPyDantic.from_orm(teacher) for teacher in subject.teachers]


def get_questions_pydantic(db: Session, topic_id: int) -> list[QuestionPyDantic]:
    questions = db.query(Question).filter(Question.topic_id == topic_id).all()
    return [QuestionPyDantic.from_orm(question) for question in questions]

