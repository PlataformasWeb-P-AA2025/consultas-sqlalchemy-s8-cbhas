from sqlalchemy.orm import sessionmaker
from clases import Curso, Entrega, Tarea
from clases import engine

Session = sessionmaker(bind=engine)
session = Session()

# Obtenemos todos los cursos
cursos = session.query(Curso).all()

for c in cursos:
    entregas = (
        session.query(Entrega) # Obtenemos todas las entregas
        .join(Tarea) # Unimos con la tabla Tarea para acceder a las tareas del curso
        .filter(Tarea.curso_id == c.id) # Filtramos las tareas que pertenecen al curso actual
        .all()
    )

    suma = 0
    cantidad = len(entregas) # Se calcula el número de entregas para el curso actual

    # Sumamos todas las calificaciones de las entregas
    for e in entregas:
        suma += e.calificacion

    # Si la cantidad es mayor a 0 calculamos el promedio de calificaciones
    if cantidad > 0:
        promedio = suma / cantidad
    # Si no hay entregas, el promedio es 0
    else:
        promedio = 0

    print(f"Curso: {c.titulo} | Promedio de calificaciones: {promedio:.2f}")
