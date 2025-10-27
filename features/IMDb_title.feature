Feature: Buscar una pelicula o serie en imdb.com y validar el nombre del titulo y el puntaje de rating
    Scenario: Validar el nombre y rating de la pelicula Inception
        Given El usuario esta en el home page de imdb.com
        When El usuario busca el titulo "Inception" 
        And El usuario presiona el enlace del primer resultado
        Then El nombre del titulo debe ser "El origen"
        And El rating del titulo debe ser "8,8"