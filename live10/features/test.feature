# language: pt

Funcionalidade: Cadastro

Cenario: Efetuar cadastro com sucesso
    Quando inserir o nome "yuuki"
    E inserir o sobrenome "asuna"
    E inserir o usuario "yuukiasuna"
    E inserir o sexo "Feminino"
    E inserir o senha "1234567"
    E inserir o email "yuukixasuna@gmail.com"
    E inserir o nascimento "27/11/1994"
    Entao clicar no botão "Enviar"
    E a mensagem deverá ser exibida
    
