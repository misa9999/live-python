from bottle import jinja2_view, route, run, request, response


@route("/<area>")
@jinja2_view("/home/blackrose/Documents/git/aulas/livesPython/live09/paginas/teste.html")
def teste(area):
    """Rederizando uma view com o decorador do jinja."""
    return dict(nome=area)


@route("/user", method="GET")
@jinja2_view("/home/blackrose/Documents/git/aulas/livesPython/live09/paginas/user.html")
def user():
    links = ["home", "about", "help"]
    return dict(links=links)


@route('/user', method='POST')
@jinja2_view('/home/blackrose/Documents/git/aulas/livesPython/live09/paginas/user.html')
def user_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'yuuki' and password == 'asuna' or \
        request.get_cookie('user') == 'yuuki':

        response.set_cookie('user', 'yuuki')
        links = ['home', 'user_space', 'help', 'metrics']

        return dict(string='Você esta logado', links=links)
    else:
        response.set_cookie('user', 'None')
        links = ["home", "about", "help"]
        return dict(string='ERRO você não está logado', links=links)


run(port=8080)
