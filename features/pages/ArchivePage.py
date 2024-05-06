import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from features import actions
from features.pages.ArchiveObject import ArchiveObject

class ArchivePage:

    def __init__(self, driver):
        self.driver = driver
        self.archive_object = ArchiveObject()

    def comprobacion_dentro_archiveorg(self):
        print('[INFO]: Esperamos a que que se cargue a web' + '\n')
        #element = actions.get_shadow_element(self.driver, self.go_home_archive_logo)
        #actions.wait_for_element_to_display(self.driver, (By.CSS_SELECTOR, self.archive_object.go_home_archive_logo))

        '''root = self.driver.find_element(By.CSS_SELECTOR, 'app-root').shadow_root
        shadow_host1 = root.find_element(By.CSS_SELECTOR, 'ia-topnav[locallinks="true"]').shadow_root
        shadow_host2 = shadow_host1.find_element(By.CSS_SELECTOR, 'primary-nav').shadow_root
        element = shadow_host2.find_element(By.CSS_SELECTOR, 'svg')
        WebDriverWait(shadow_host2, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg"))
        )
        element.click()'''

        element, host = actions.find_element_with_shadow_root(self.driver, 'app-root', 'ia-topnav[locallinks="true"]',
                                                              'primary-nav', 'svg')
        print("Elemento final:", element)
        print("Root más cercano:", host)
        WebDriverWait(host, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "svg"))
        )
        element.click()
        time.sleep(2)
        element, host = actions.find_element_with_shadow_root(self.driver, 'app-root', 'home-page',
                                                              'ia-wayback-search[basehost="https://web.archive.org"]',
                                                              '#url')
        print("Elemento final:", element)
        print("Root más cercano:", host)
        WebDriverWait(host, 10).until(
            EC.element_to_be_clickable(element)
        )
        #element.click()
        actions.send_keys_shadow(element, "The Lord Of Rings")
        time.sleep(2)

        '''# Esperar a que aparezca un elemento dentro del Shadow DOM
        berechnen_button = WebDriverWait(shadow_root, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "nav > div.branding > a"))
        )

        # Hacer clic en el elemento dentro del Shadow DOM
        berechnen_button.click()'''

