class GoogleObject:
    modal_cookies_logo = "//img[@alt='Google' and @srcset]"
    modal_cookies_idioma = "//button[contains(@aria-label, 'Seleccionar idioma')]"
    modal_cookies_login = "//div[contains(text(), 'Iniciar sesión')]"
    #//button[@role='link']/div
    modal_cookies_titulo = "//h1[contains(text(), 'Antes de ir a Google')]"
    modal_cookies_texto = "//h1[contains(text(), 'Antes de ir a Google')]/following-sibling::div"
    #modal_aceptar_cookies = "//h1[contains(text(), 'Antes de ir a Google')]/h1"
    #modal_rechazar_cookies = "//h1[contains(text(), 'Antes de ir a Google')]/h1"
    modal_rechazar_aceptar = "//button/div[@role='none' and contains(text(), 'todo')]"

    google_colored_logo = "//style/following-sibling::img"
    google_search_box = "//*[contains(@title, 'Buscar')]"

    google_results = "//div[@jscontroller and @style='width:600px']"
    google_results_archive_elemts = "//div[@jscontroller and @style='width:600px']//cite[contains(text(), 'https://archive.org')]"
