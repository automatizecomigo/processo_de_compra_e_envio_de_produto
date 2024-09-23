from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page


scenarios('../feature/add_produto_carrinho.feature')

login = 'standard_user'
password = 'secret_sauce'


@given('que esteja na tela de login')
def pagina_de_login(browser: Page):
    browser.goto('https://www.saucedemo.com/')


@when("feito o login com credenciais validas")
def fazer_login_com_credenciais_validas(browser: Page):
    browser.locator('[placeholder="Username"]').fill(login)
    browser.locator('[placeholder="Password"]').fill(password)
    browser.locator('[type="submit"]').click()


@when("escolho um produto e adiciono ao carrinho")
def selecionar_um_produto(browser: Page):
    browser.get_by_text('Sauce Labs Onesie', exact=True).click()
    browser.get_by_text('Add to cart').click()


@then("devo verificar se o produto foi adicionado corretamente")
def validar_se_o_produto_foi_adicionaro_ao_carrinho_corretamente(browser: Page):
    browser.goto('https://www.saucedemo.com/cart.html')
    expect(browser.get_by_text('Sauce Labs Onesie')).to_be_visible()