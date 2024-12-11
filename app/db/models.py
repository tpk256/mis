from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

subject_teacher_association = Table(
    'subject_teacher', Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id'), primary_key=True),
    Column('teacher_id', Integer, ForeignKey('teachers.id'), primary_key=True)
)


class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, nullable=False)
    ans = Column(String, nullable=True)
    topic_id = Column(Integer, ForeignKey('topics.id'), nullable=False)

    topic = relationship("Topic", back_populates="questions")


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

    teachers = relationship(
        "Teacher",
        secondary=subject_teacher_association,
        back_populates="subjects"
    )
    topics = relationship("Topic", back_populates="subject")


class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    subjects = relationship(
        "Subject",
        secondary=subject_teacher_association,
        back_populates="teachers"
    )


class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id'), nullable=False)

    subject = relationship("Subject", back_populates="topics")
    questions = relationship("Question", back_populates="topic")
