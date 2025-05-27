from sqlalchemy.orm import sessionmaker
from clases import Entrega

from clases import engine
Session = sessionmaker(bind=engine)
session = Session()

# Consulta todas las filas de la tabla entrega y las guarda en una lista llamada entregas
entregas = session.query(Entrega).all()

# Recorre cada entrega, una por una
for e in entregas:
    # Unimos la entrega con el curso y el departamento
    # para filtrar las entregas de tareas del departamento de Arte
    curso = e.tarea.curso
    if curso.departamento.nombre == "Arte":
        print(f"Tarea: {e.tarea.titulo} | Estudiante: {e.estudiante.nombre} | "
              f"Calificación: {e.calificacion} | Instructor: {curso.instructor.nombre} | "
              f"Departamento: {curso.departamento.nombre}")
