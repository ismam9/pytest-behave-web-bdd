from behave import *

from features.pages.GooglePage import GooglePage


@then(u'accede a la web de archive.org')
def step_impl(context):
    try:
        context.google_page = GooglePage(context.driver)
        context.archive_page = context.google_page.accedemos_archive()
        print('Accedemos a la web de archive.org')
    except Exception as e:
        print(f"[ERROR]. No se ha podido acceder a la web. Error: {e.__cause__}")

@given(u'el usuario ya esta dentro de archive.org')
def step_impl(context):
    context.archive_page.comprobacion_dentro_archiveorg()
    print('Dentro de archive.org')


@then(u'accedemos a la pagina de registro')
def step_impl(context):
    print("acedemos al Sign up")


@then(u'nos registramos con los siguientes datos')
def step_impl(context):
    for row in context.table:
        print(row["email_adress"])
        print(row["screen_name"])
        print(row["choose_password"])
        print(row["announcements"])

    print("nos registramos con los datos")


@when(u'comprobamos que hemos realizado el registro correctamente')
def step_impl(context):
    print("acedemos al se comrpueba que hemos realizdo el registro correctamente")


@then(u'comprueba la navegacion y tabs que encuentra en la pagina')
def step_impl(context):
    print('Navegacion y tabs se encuentran en la página')


@when('el usuario clicka en el "{tab}" de la barra de navegacion')
def step_impl(context, tab):
    print('el usuario click en barra de navegacion')


@then('el usuario accede a cada "{content}" y comprueba que el acceso es correcto')
def step_impl(context, content):
    print('el usuario accede al tab x y es correcto')
