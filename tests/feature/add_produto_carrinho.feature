Feature: adicionar produtos ao carrinho

  Scenario: Escolher e adicionar um tipo de produto ao carrinho
    Given que esteja na tela de login
    When feito o login com credenciais validas
    When escolho um produto e adiciono ao carrinho
    Then devo verificar se o produto foi adicionado corretamente