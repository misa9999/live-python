"""
uma breve introdução sobre rotas

Dinâmicas e estáticas.
"""

from bottle import run, route


@route('/')
def index():
    """Rota estática para o index do site."""
    return '<h1>Olá live de python</h1>'


@route('/<person>')
def index(person):
    """Exemplo de rota dinâmica."""
    if person == 'teste':
        return 'Voĉe não é bem vindo'
    return f'<h1>Olá {person}</h1>'


run(port=8080)