from dml import db_insert, db_select, db_update

from pprint import pprint 

# db_insert('Dan', '98989898', 'dan@gmail.com')
# db_insert('kat', '98989898', 'kat@gmail.com')
# db_insert('leia', '98989898', 'leia@gmail.com')
# db_insert('leticia', '98989898', 'leticia@gmail.com')
# db_insert('rafaela', '98989898', 'rafaela@gmail.com')
# db_insert('renata', '98989898', 'renata@gmail.com')

pprint(db_select('98989898', 'phone'))