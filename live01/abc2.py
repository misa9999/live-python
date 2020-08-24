def eh_par(val: int) -> bool:
    """Função que verifica se o número é par

    Arguments:
        val {int} --  valor de entrada do tipo inteiro

    Returns:
        bool -- retorna true se o número for par e false se for impar

     """
    if isinstance(val, int) or isinstance(val, float):
        return True if val % 2 == 0 else False
    else:
        return False
