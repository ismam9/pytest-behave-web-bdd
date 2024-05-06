Feature: Archive Tabs Funcionality

  Background:
    Given el usuario accede a Google
    When acepta las cookies
    And escribe en el buscador por "archive.org"
    And se muestra los resultados de archive
    Then accede a la web de archive.org

  @example
  Scenario: Comprobación de pagina de inicio y tabs de navegación
    Given el usuario ya esta dentro de archive.org
    Then comprueba la navegacion y tabs que encuentra en la pagina

  @datatable
  Scenario: Comprobación de pagina de inicio y tabs de navegación
    Given el usuario ya esta dentro de archive.org
    Then accedemos a la pagina de registro
    And nos registramos con los siguientes datos
          |email_adress             |screen_name|choose_password|announcements|
          |ismam_98@hotmail.com     |isma       |12et3a3N*      |2            |
          #|dwellingsmusic@gmail.com |musicism   |13et3a3N*      |0           |
    When comprobamos que hemos realizado el registro correctamente

  Scenario Outline: Acceso a cada una de las tabs de navegación de la pagina principal
    Given el usuario ya esta dentro de archive.org
    When el usuario clicka en el "<tab>" de la barra de navegacion
    Then el usuario accede a cada "<content>" y comprueba que el acceso es correcto

    Examples: Tabs
      | tab                         | content  |
      | "Printed Chiffon Dress"     | "hola" |
      | "guapo"                     |  "adios" |