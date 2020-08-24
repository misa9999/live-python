from sqlalchemy import update
from core import user_table, engine

conn = engine.connect()

u = update(user_table).where(user_table.c.nome == 'yuuki')

# u = u.values(nome='yuuki')
# u = u.values(idade=(user_table.c.idade - 4))
u = u.values(idade=19)

result = conn.execute(u)

print(result.rowcount)