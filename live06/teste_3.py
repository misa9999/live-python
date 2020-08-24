""""

closure
"""

from pdb import set_trace

# Ola, Ahoy, Hello


def externa(id):
    dic = {'pt': 'Olá', 'pi': 'Ahoy', 'en': 'Hello'}

    def interna(nome):
        print(f'{dic[id]} {nome}')
    return interna

'''
func = externa('pi')
func('Dan')
func('BlacRose')
'''

@externa
def greet_user():
    print(f'{id} {nome}')


greet_user('danilo')