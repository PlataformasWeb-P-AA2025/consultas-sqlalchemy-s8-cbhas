from sqlalchemy.orm import sessionmaker
from clases import Entrega, Curso, Departamento, Tarea

from clases import engine
Session = sessionmaker(bind=engine)
session = Session()

entregas = (
    session.query(Entrega)
    .join(Entrega.tarea)                # Une con la tabla Tarea
    .join(Entrega.estudiante)           # Une con la tabla Estudiante
    .join(Entrega.tarea, Tarea.curso)   # Une con la tabla Curso a través de Tarea
    .join(Curso.departamento)           # Une con la tabla Departamento
    .join(Curso.instructor)             # Une con la tabla Instructor
    .filter(Departamento.nombre == "Arte")  # Filtra solo departamento Arte
    .all()
)

for e in entregas:
    print(f"Tarea: {e.tarea.titulo} | Estudiante: {e.estudiante.nombre} | "
          f"Calificación: {e.calificacion} | Instructor: {e.tarea.curso.instructor.nombre} | "
          f"Departamento: {e.tarea.curso.departamento.nombre}")
