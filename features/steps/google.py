from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

from features.pages.GooglePage import GooglePage

@given(u'el usuario accede a Google')
def step_impl(context):
    google_page = GooglePage(context.driver)
    try:
        google_page.wait_modal_cookies()
        print("[OK]. El usuario accede a Google y espera al modal del cookies correctamente")
    except Exception as e:
        print(f"[ERROR]. No se ha podido esperar al modal de las cookies de google. Error: {e.__cause__}")

@when(u'acepta las cookies')
def step_impl(context):
    google_page = GooglePage(context.driver)
    try:
        google_page.scroll_and_click_aceptar_cookies()
        print("[OK]. El usuario acepta las cookies correctamente")
    except Exception as e:
        print(f"[ERROR]. El usuario no ha podido aceptar las cookies. Error: {e.__cause__}")

@when(u'escribe en el buscador por "{web}"')
def step_impl(context, web):
    google_page = GooglePage(context.driver)
    try:
        google_page.wait_search_box_google()
        google_page.send_key_search_box_google(web)
        print(f"[OK]. El usuario envia busca por {web} correctamente en google")
    except Exception as e:
        print(f"[ERROR]. El usuario no ha podido realizar la busqueda por {web} correctamente. Error: {e.__cause__}")


@when(u'se muestra los resultados de archive')
def step_impl(context):
    google_page = GooglePage(context.driver)
    try:
        google_page.comprobamos_resultados_search_google()
        print("[OK]. Se muestran los resultados correctamente")
    except Exception as e:
        print(f"[ERROR]. El usuario no ha podido comprobar los resultado de la busqueda. Error: {e.__cause__}")

