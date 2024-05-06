from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click_element(driver, locator):
    try:
        element = driver.find_element(*locator)
        element.click()
        print(f"Click correcto al elemento: {locator}")
    except Exception as e:
        print(f"No se pudo hacer clic en el elemento: {locator}. Error: {e}")


def wait_and_click(driver, locator):
    timeout = 15
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        print(f"El elemento: {locator} es visible correctamente")
        element.click()
        print(f"Click al elemento correctamente: {locator}")
    except TimeoutException:
        print(f"Tiempo de espera agotado para hacer clic en el elemento: {locator}")


def wait_for_element_to_display(driver, locator):
    timeout = 15
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        print(f"El elemento {locator} es visible correctamente")
    except TimeoutException:
        print(f"Tiempo de espera agotado para el elemento {locator}. Elemento no encontrado.")
    except Exception as e:
        print(f"Error al esperar el elemento {locator}: {e}")


def wait_for_elements_to_display(driver, xpath):
    timeout = 15
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_all_elements_located(By.XPATH, xpath))
        print(f"El elemento: {xpath} es visible correctamente")
    except Exception as e:
        print(f"Tiempo de espera superado: {timeout} seg. Elemento no visible {xpath}. Error: {e}")


def wait_and_scroll_to(driver, locator):
    timeout = 15
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        print(f"El elemento: {locator} es visible correctamente")
        scroll_to_element(driver, driver.find_element(*locator))
        print(f"Se hace scroll correctamente al elemento: {locator}")
    except TimeoutException:
        print(f"Tiempo de espera agotado para el elemento: {locator}. Elemento no encontrado.")


def send_keys(driver, locator, string):
    try:
        element = driver.find_element(*locator)
        element.send_keys(string)
        print(f"Se envio: '{string}' al elemento: {locator}")
    except NoSuchElementException:
        print(f"No se ha podido enviar: {string} al elemento: {locator}")


def send_keys_shadow(element, string):
    try:
        element.send_keys(string)
        print(f"Se envio: '{string}' al elemento: {element}")
    except NoSuchElementException:
        print(f"No se ha podido enviar: {string} al elemento: {element}")


def wait_and_send_keys(driver, locator, string):
    try:
        wait_for_element_to_display(driver, locator)
        send_keys(driver, locator, string)
        print(f"Se envio correctamente: '{string}' al elemento: {locator}")
    except Exception as e:
        print(f"No se puedo enviar: {string} correctamente al {locator}")


def wait_scroll_and_send_keys(driver, locator, string):
    try:
        wait_and_scroll_to(driver, locator)
        send_keys(driver, locator, string)
        press_tecla(driver, 'ENTER')
        print(f"Se envio correctamente: '{string}' al elemento: {locator}")
    except TimeoutException:
        print(f"No se puedo enviar: {string} correctamente al {locator}")


def press_tecla(driver, key, locator=None):
    if key == 'ENTER':
        key = Keys.ENTER
    elif key == 'ESCAPE':
        key = Keys.ESCAPE

    try:
        if locator:
            element = driver.find_element(*locator)
            element.send_keys(key)
            print(f"Se simuló la pulsación de '{key}' en el elemento: {locator}")
        else:
            driver.switch_to.active_element.send_keys(key)
            print(f"Se simuló la pulsación de '{key}' en el elemento activo")
    except NoSuchElementException:
        print(f"No se pudo encontrar el elemento: {locator} para simular la pulsación de '{key}'")


def scroll_to_element(driver, locator):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(*locator))
        print(f"Se hace scroll correctamente al elemento: {locator}")
    except Exception as e:
        print(f"No se pudo hacer scroll hacia el elemento: {locator}. Error: {e}")


def scroll_to(driver, element):
    try:
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        print(f"Se hace scroll correctamente al elemento: {element}")
    except Exception as e:
        print(f"No se pudo hacer scroll hacia el elemento: {element}. Error: {e}")


def scroll_bottom(driver):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(f"Se hace scroll correctamente al final de la página")
    except Exception as e:
        print(f"No se pudo hacer scroll hacia el final de la página. Error: {e}")


def scroll_top(driver):
    try:
        driver.execute_script("window.scrollTo(0, 0);")
        print(f"Se hace scroll correctamente arriba de la página")
    except Exception as e:
        print(f"No se pudo hacer scroll hacia arriba de la página. Error: {e}")


'''def get_shadow_element(parent, selector_css):
    try:
        # Ejemplo de JavaScript para encontrar un elemento dentro del Shadow DOM
        element = f'return document.querySelector("{parent}").shadowRoot.querySelector("{selector_css}");'

        cssSelectorForHost1 = "app-root";
        String
        cssSelectorForHost2 = "ia-topnav[locallinks='true']";
        String
        cssSelectorForHost3 = "primary-nav";
        Thread.sleep(1000);
        SearchContext
        shadow0 = driver.findElement(By.cssSelector("app-root")).getShadowRoot();
        Thread.sleep(1000);
        SearchContext
        shadow1 = shadow0.findElement(By.cssSelector("ia-topnav[locallinks='true']")).getShadowRoot();
        Thread.sleep(1000);
        SearchContext
        shadow2 = shadow1.findElement(By.cssSelector("primary-nav")).getShadowRoot();
        Thread.sleep(1000);
        shadow2.findElement(By.cssSelector("svg"));
    except Exception as e:
        print(f"No se pudo obtener el elemento shadow de: {e}")'''


def find_element_with_shadow_root(driver, *args):
    # Comprobamos que se hayan proporcionado al menos dos argumentos
    if driver is None:
        raise ValueError("Se necesitan el driver")
    if len(args) < 2:
        raise ValueError("Se necesitan al menos dos argumentos")

    'app-root', 'ia-topnav[locallinks="true"]', 'primary-nav', 'svg'

    # Obtenemos el primer elemento con el driver de Selenium
    root_element = driver.find_element(By.CSS_SELECTOR, args[0]).shadow_root  # 'app-root'

    if not len(args) >= 2 and not args[-2]:
        element = root_element.find_element(By.CSS_SELECTOR, args[1]).shadow_root
        return element, root_element
    elif len(args) >= 2 and args[-2]:
        element = driver.find_element(By.CSS_SELECTOR, args[0]).shadow_root  # 'app-root'
        for selector in args[1:-1]:
            # Buscamos el elemento dentro del shadow host
            element = element.find_element(By.CSS_SELECTOR, selector).shadow_root
            # element = 'ia-topnav[locallinks="true"]'
            # element = 'primary-nav'
            if args[-2]:
                root_element = element
        element = element.find_element(By.CSS_SELECTOR, args[-1])
        return element, root_element
