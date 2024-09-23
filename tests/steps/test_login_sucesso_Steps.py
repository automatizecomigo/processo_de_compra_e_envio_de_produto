from pytest_bdd import given, when, then, scenarios
from playwright.sync_api import expect, Page


scenarios('../feature/login_sucesso.feature')

login = 'standard_user'
password = 'secret_sauce'


@given('que o usuário acessa a página de login do saucedemo')
def pagina_de_login(browser: Page):
    browser.goto('https://www.saucedemo.com/')



@when('o usuário preenche o campo de usuário com "standard_user" e senha com "secret_sauce"')
def preenche_campos(browser: Page):
    browser.locator('[placeholder="Username"]').fill(login)
    browser.locator('[placeholder="Password"]').fill(password)
    browser.locator('[type="submit"]').click()



@then("o usuário é redirecionado paras a página de produtos")
def verifica_redirecionamento(browser: Page):
    expect(browser.get_by_text('Products')).to_be_visible()
