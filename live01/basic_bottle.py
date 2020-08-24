from bottle import route, run


@route('/')
def index():
    return "Olá pessoas"


if __name__ == "__main__":
    run()
