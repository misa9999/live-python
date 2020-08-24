def decorador(argumentos_decorador):
    print(argumentos_decorador)
    """
    Parametros do decorador

    """

    def decorador_real(func):
        print(func.__name__)
        """
        Receber a função
        """

        def execute_function(*argumentos_funcao):
            print(argumentos_funcao)
            """
            Executar a função
            """
            pass
       
        return execute_function
    
    return decorador_real



@decorador('Rose')
def soma(x, y):
    return x + y


soma(2, 2)