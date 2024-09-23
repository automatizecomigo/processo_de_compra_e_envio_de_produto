Feature: cadastrar dados para o envio do produto

  Scenario: cadastrar dados para envio do produto
    Given que esteja na tela de login
    When feito o login com credenciais validas
    And preecho os dados necessarios para o envio do produto
    Then devo verificar se o produto foi enviado com sucesso