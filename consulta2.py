from sqlalchemy.orm import sessionmaker
from clases import Entrega, Curso, Departamento, Tarea
from clases import engine
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()

departamentos = (
    session.query(Departamento)
    .join(Departamento.cursos)   # Une departamentos con cursos porque un departamento tiene varios cursos
    .join(Curso.tareas)           # Une cursos con tareas porque un curso tiene varias tareas de un departamento
    .join(Tarea.entregas)         # Une tareas con entregas porque una tarea tiene varias entregas 
    .filter(Entrega.calificacion <= 0.3) # Filtra las entregas con calificación menor o igual a 0.3
    .all()
)

# Imprime el nombre del departamento y el número de cursos asociados
for d in departamentos:
    print(f"Departamento: {d.nombre} | Número de cursos: {len(d.cursos)}")
