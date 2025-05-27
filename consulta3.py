from sqlalchemy.orm import sessionmaker
from clases import Estudiante, Entrega, Tarea
from clases import engine

Session = sessionmaker(bind=engine)
session = Session()

# Buscar tareas donde las entregas pertenecen a esos estudiantes
tareas = (
    session.query(Tarea)
    .join(Entrega)  # Une tareas con entregas debido a la relación de Tarea
    .join(Estudiante)  # Une entregas con estudiantes porque cada entrega tiene un estudiante
    .filter( # Filtra por los nombres de los estudiantes específicos utilizando el operador OR
        (Estudiante.nombre == "Jennifer Bolton") |
        (Estudiante.nombre == "Elaine Perez") |
        (Estudiante.nombre == "Heather Henderson") |
        (Estudiante.nombre == "Charles Harris")
    )
    .all()
)

# Mostrar nombre de la tarea y número de entregas
for t in tareas:
    print(f"Tarea: {t.titulo} | Número de entregas: {len(t.entregas)}")
