from sqlalchemy.orm import sessionmaker
from clases import Entrega

from clases import engine
Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega).all()

for entrega in entregas:
    curso = entrega.tarea.curso
    if curso.departamento.nombre == "Arte":
        print(f"Tarea: {entrega.tarea.titulo} | Estudiante: {entrega.estudiante.nombre} | "
              f"Calificación: {entrega.calificacion} | Instructor: {curso.instructor.nombre} | "
              f"Departamento: {curso.departamento.nombre}")
