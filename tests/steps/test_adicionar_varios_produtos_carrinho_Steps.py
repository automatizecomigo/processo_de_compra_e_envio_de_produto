from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page
from credenciais import login, password

scenarios('../feature/adicionar_varios_produtos_carrinho.feature')


@given('que o usuário acessa a página de login do saucedemo')
def pagina_de_login(browser: Page):
    browser.goto('https://www.saucedemo.com/')


@when("o usuário preenche as credencias validas")
def preenche_as_credenciais_validas(browser: Page):
    browser.locator('[placeholder="Username"]').fill(login)
    browser.locator('[placeholder="Password"]').fill(password)
    browser.locator('[type="submit"]').click()


@when("acessa a tela home de escolher alguns produtos e envia para o carrinho")
def acessa_tela_home_com_a_lista_dos_produtos_selecionar_produtos_enviar_para_carrinho(browser: Page):
    browser.get_by_text('Sauce Labs Backpack', exact=True).click()
    browser.get_by_text('Add to cart', exact=True).click()
    browser.get_by_text('Back to products', exact=True).click()

    browser.get_by_text('Sauce Labs Bike Light', exact=True).click()
    browser.get_by_text('Add to cart', exact=True).click()
    browser.get_by_text('Back to products', exact=True).click()

    browser.get_by_text('Sauce Labs Bolt T-Shirt', exact=True).click()
    browser.get_by_text('Add to cart', exact=True).click()
    browser.get_by_text('Back to products', exact=True).click()

    browser.get_by_text('Sauce Labs Fleece Jacket', exact=True).click()
    browser.get_by_text('Add to cart', exact=True).click()
    browser.get_by_text('Back to products', exact=True).click()


@then("valido se os produtos foram adicionado corretamente")
def validar_se_produtos_foram_adicionador_corretamente_ao_carrinho(browser: Page):
    browser.goto('https://www.saucedemo.com/cart.html')
    expect(browser.get_by_text('Sauce Labs Backpack'))
    expect(browser.get_by_text('Sauce Labs Bike Light'))
    expect(browser.get_by_text('Sauce Labs Bolt T-Shirt'))
    expect(browser.get_by_text('Sauce Labs Bolt T-Shirt'))
    expect(browser.get_by_text('Sauce Labs Fleece Jacket'))
