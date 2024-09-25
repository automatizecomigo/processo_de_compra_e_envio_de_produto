Feature: selecionar alguns produtos e enviar para o carrinho

  Scenario: selecionar produtos e enviar para o carrinho
    Given que o usuário acessa a página de login do saucedemo
    When  o usuário preenche as credencias validas
    And acessa a tela home de escolher alguns produtos e envia para o carrinho
    Then valido se os produtos foram adicionado corretamente