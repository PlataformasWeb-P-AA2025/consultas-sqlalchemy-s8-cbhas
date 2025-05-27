from sqlalchemy.orm import sessionmaker
from clases import Entrega, Curso, Departamento, Tarea
from clases import engine
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

departamentos = (
    session.query(Departamento)
    .join(Departamento.cursos)
    .join(Curso.tareas)
    .join(Tarea.entregas)
    .filter(Entrega.calificacion <= 0.3)
    .all()
)

for d in departamentos:
    print(f"Departamento: {d.nombre} | Número de cursos: {len(d.cursos)}")
