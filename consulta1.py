from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from clases import *
from config import cadena_base_datos

engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

resultados = session.query(
    Tarea.titulo.label("titulo_tarea"),
    Estudiante.nombre.label("nombre_estudiante"),
    Entrega.calificacion,
    Instructor.nombre.label("nombre_instructor"),
    Departamento.nombre.label("nombre_departamento")
).join(Entrega.tarea).join(Tarea.curso).join(Curso.departamento).join(Curso.instructor).join(Entrega.estudiante).filter(Departamento.nombre == "Arte").all()

for r in resultados:
    print(f"Tarea: {r.titulo_tarea} | Estudiante: {r.nombre_estudiante} | Calificación: {r.calificacion} | Instructor: {r.nombre_instructor} | Departamento: {r.nombre_departamento}\n")
