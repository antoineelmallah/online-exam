from entities.entity import Session, engine, Base
from entities.exam import Exam

# generate database schema if needed
Base.metadata.create_all(engine)

# start session
session = Session()

# check for existing data
exams = session.query(Exam).all()

if len(exams) == 0:
    
    # create and persist mock exam
    python_exam = Exam('Test Exam', 'Test your knowledge', 'script')
    session.add(python_exam)
    session.commit()
    session.close()

    # reload exams
    exams = session.query(Exam).all()

# Show existing exams
    print('### Exams:')
    for exam in exams:
        print(f'({exam.id}) {exam.title} - {exam.description}')