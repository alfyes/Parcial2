Feature: Recorrido de pantallas
  Background: Crear carro
    Given I press "btn_create_car"
    And I enter text "Aveo" into field with id "edt_name"
    And I go back
    And I press "menu_save"
    And I wait for 2 seconds

  Scenario: Otros Ingresos
    Given I swipe left
    And I wait for 2 seconds
    And take screenshot with name "rcpt_sc1_menu"
    And I touch the "Aveo" text
    # Boton +
    Then I press image button number 2
    And I wait for 2 seconds
    And take screenshot with name "rcpt_sc1_floatmenu"
    # Boton other income
    And I press image button number 2
    And I enter text "Titulo 1" into field with id "edt_title"
    And I enter text "1000" into field with id "edt_mileage"
    And I enter text "215" into field with id "edt_price"
    And I go back
    And I wait for 2 seconds
    And take screenshot with name "rcpt_sc1_income"
    And I press "menu_save"
    And I touch the "OTHER INCOME" text
    And I see the text "Titulo 1"
    And I wait for 2 seconds
    And take screenshot with name "rcpt_sc1_listincome"

  Scenario: Informacion sobre car report
    Given I swipe left
    And I wait for 2 seconds
    And I touch the "Settings" text
    And I wait for 2 seconds
    And take screenshot with name "rcpt_sc2_settingsmenu"

    Then I touch the "About Car Report" text
    And I wait for 2 seconds
    And take screenshot with name "rcpt_sc2_about"
    And I see the text "LICENSES"
