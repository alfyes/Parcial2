Feature: Crear vehiculo

    Scenario: Solo nombre.
        Given I wait for 3 seconds
        And take screenshot with name "crvh_sc1_ppal" 
        And I press "btn_create_car"
        Then I enter text "Aveo" into field with id "edt_name"
        And take screenshot with name "crvh_sc1_listo"
        And I press "menu_save"
        And take screenshot with name "crvh_sc1_creado"

    Scenario: Nombre y color
        Given I wait for 3 seconds
        And take screenshot with name "crvh_sc2_ppal" 
        And I press "btn_create_car"
        Then I enter text "Aveo" into field with id "edt_name"
        And I press "btn_color"
        And I wait for 3 seconds
        And take screenshot with name "crvh_sc2_colores"
        And I press the "ACEPTAR" button
        And take screenshot with name "crvh_sc2_listo"
        And I press "menu_save"
        And take screenshot with name "crvh_sc2_creado"
