from core import user_table, engine

conn = engine.connect()

ins = user_table.insert()

# new_user = ins.values(nome='Yuuki',
#                      idade=24,
#                      senha='Tokyo')
# conn.execute(new_user)

conn.execute(user_table.insert(), [
    {'nome': 'dan', 'idade': 24, 'senha': 'batatinhas'},
    {'nome': 'nati', 'idade': 26, 'senha': 'gatinhos123'},
    {'nome': 'tuila', 'idade': 19, 'senha': 'limonadas'},
    {'nome': 'ju', 'idade': 15, 'senha': 'lolis'},
    {'nome': 'asuna', 'idade': 24, 'senha': 'dans2'},             
])