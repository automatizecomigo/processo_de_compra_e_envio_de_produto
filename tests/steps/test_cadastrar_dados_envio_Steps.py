from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page

scenarios('../feature/cadastrar_dados_envio.feature')

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


@when("preecho os dados necessarios para o envio do produto")
def preencho_dados_para_envio_produto(browser: Page):
    browser.goto('https://www.saucedemo.com/cart.html')
    browser.get_by_text('Checkout').click()
    browser.locator('[placeholder="First Name"]').fill('Rafael')
    browser.locator('[placeholder="Last Name"]').fill('Pantoja')
    browser.locator('[placeholder="Zip/Postal Code"]').fill('69077-765')
    browser.get_by_text('Continue').click()



@then("devo verificar se o produto foi enviado com sucesso")
def verifico_se_produto_foi_enviado_com_sucesso(browser: Page):
    expect(browser.get_by_text('SauceCard #31337', exact=True)).to_be_visible()
    browser.get_by_text('Finish', exact=True).click()
    expect(browser.get_by_text('Thank you for your order!', exact=True))