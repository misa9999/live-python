# language: pt

Funcionalidade: Soma
"""
Sendo um usuário eu quero somar dois números para que seja possível
receber seu resultado
"""

Cenario: Soma de inteiros positivos
    Quando somar "2" e "2"
    Então o resultado deve ser "4"

Cenario: Soma de inteiros negativos
    Quando somar "-3" e "-3"
    Então o resultado deve ser "-6"