import time

from selenium.webdriver.common.by import By

from features.pages.ArchivePage import ArchivePage
from features.pages.GoogleObject import GoogleObject
from features import actions


class GooglePage:

    def __init__(self, driver):
        self.driver = driver
        self.google_object = GoogleObject()

    def wait_modal_cookies(self):
        #self.driver.find_element(By.XPATH, self.google_object.cookies_tab_xpath).click()
        print('[INFO]: Esperamos a que aparezca el modal de las cookies' + '\n')
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.modal_cookies_logo))
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.modal_cookies_idioma))
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.modal_cookies_titulo))
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.modal_cookies_texto))
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.modal_cookies_login))

    def scroll_and_click_aceptar_cookies(self):
        #self.driver.find_element(By.XPATH, self.google_object.cookies_tab_xpath).click()
        print('[INFO]: Realizamos scroll al elemento de aceptar/rechazar cookies' + '\n')
        '''actions.wait_for_elements_to_display(self.driver, self.google_object.modal_rechazar_aceptar)
        actions.scroll_to(self.driver, self.google_object.modal_rechazar_aceptar + "[1]")
        actions.click_element(self.driver, self.google_object.modal_rechazar_aceptar + "[1]")'''
        actions.wait_and_scroll_to(self.driver, (By.XPATH, self.google_object.modal_rechazar_aceptar + "[1]"))
        actions.wait_and_click(self.driver, (By.XPATH, self.google_object.modal_rechazar_aceptar + "[1]"))

    def scroll_and_click_rechazar_cookies(self):
        #self.driver.find_element(By.XPATH, self.google_object.cookies_tab_xpath).click()
        print('Esperamos a que aparezca el modal de las cookies' + '\n')
        '''actions.wait_for_elements_to_display(self.driver, self.google_object.modal_rechazar_aceptar)
        actions.scroll_to(self.driver, self.google_object.modal_rechazar_aceptar + "[2]")
        actions.click_element(self.driver, self.google_object.modal_rechazar_aceptar + "[2]")'''
        actions.wait_and_scroll_to(self.driver, (By.XPATH, self.google_object.modal_rechazar_aceptar + "[2]"))
        actions.wait_and_click(self.driver, (By.XPATH,self.google_object.modal_rechazar_aceptar + "[2]"))

    def wait_search_box_google(self):
        #self.driver.find_element(By.XPATH, self.google_object.cookies_tab_xpath).click()
        print('Esperamos a que aparezca el modal de las cookies' + '\n')
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.google_colored_logo))
        actions.wait_for_element_to_display(self.driver, (By.XPATH, self.google_object.google_search_box))

    def send_key_search_box_google(self, string):
        #self.driver.find_element(By.XPATH, self.google_object.cookies_tab_xpath).click()
        print('Esperamos a que aparezca el modal de las cookies' + '\n')
        '''actions.wait_for_elements_to_display(self.driver, self.google_object.google_search_box)
        actions.send_keys(self.driver, self.google_object.google_search_box, "archive.org")
        actions.press_tecla(self.driver, 'ENTER', self.google_object.google_search_box)'''

        '''actions.wait_and_send_keys(self.driver, self.google_object.google_search_box, "archive.org")
        actions.press_tecla(self.driver, 'ENTER')'''

        actions.wait_scroll_and_send_keys(self.driver, (By.XPATH, self.google_object.google_search_box), string)
        time.sleep(5)

    def comprobamos_resultados_search_google(self):
        #self.driver.find_element(By.XPATH, self.google_object.cookies_tab_xpath).click()
        print('Esperamos a que aparezca el modal de las cookies' + '\n')
        actions.wait_for_elements_to_display(self.driver, (By.XPATH, self.google_object.google_results))
        for results in self.driver.find_elements(By.XPATH, self.google_object.google_results):
            actions.scroll_to(self.driver, results)
            time.sleep(2)

        size = len(self.google_object.google_results)
        print(f"Se muestran: {size} resultados.")

        actions.scroll_top(self.driver)
        actions.scroll_bottom(self.driver)

        actions.wait_and_scroll_to(self.driver, (By.XPATH, self.google_object.google_results + "[1]"))

        archive_elemts = self.driver.find_elements(By.XPATH, self.google_object.google_results_archive_elemts)
        print(f"Se muestran: {len(archive_elemts)} resultados con url https://archive.org")

        actions.wait_and_scroll_to(self.driver, (By.XPATH, self.google_object.google_results_archive_elemts + "/parent::div/parent::div" + "[1]"))


    def accedemos_archive(self):
        actions.scroll_top(self.driver)
        time.sleep(1)

        actions.wait_and_click(self.driver, (By.XPATH, self.google_object.google_results_archive_elemts + "/parent::div/parent::div" + "[1]"))
        time.sleep(5)

        return ArchivePage(self.driver)
