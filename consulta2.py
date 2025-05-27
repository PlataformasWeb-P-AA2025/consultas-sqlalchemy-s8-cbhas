from sqlalchemy.orm import sessionmaker
from clases import Entrega, Curso, Departamento, Tarea
from clases import engine
from sqlalchemy import func

Session = sessionmaker(bind=engine)
session = Session()


departamentos = (
    session.query(Departamento)
    .join(Curso) # Une con la tabla Curso a través de la relación de Departamento
    .join(Tarea) # Une con la tabla Tarea por la relación de Curso
    .join(Entrega) # Une con la tabla Entrega por la relación de Tarea
    .filter(Entrega.calificacion <= 0.3).all() # Filtra entregas con calificación menor o igual a 0.3
)

# Imprime el nombre del departamento y el número de cursos asociados
for d in departamentos:
    print(f"Departamento: {d.nombre} | Número de cursos: {len(d.cursos)}")
