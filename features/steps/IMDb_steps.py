from behave import given, when, then
from selenium import webdriver
from pages.IMDb_home_page import IMDbHomePage
from pages.IMDb_results_page import IMDbResultPage
from pages.IMDb_title_page import IMDbTitlePage


@given('El usuario esta en el home page de imdb.com')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.imdb.com/")
    context.IMDb_home= IMDbHomePage(context.driver)
      
@when('El usuario busca el titulo "{title_name}"')
def step_search_page(context,title_name):
    context.IMDb_home.search_title(title_name)
    context.IMDb_result = IMDbResultPage(context.driver)
    
@when('El usuario presiona el enlace del primer resultado')
def step_press_link(context):
    context.IMDb_result.press_link()
    context.IMDb_title = IMDbTitlePage(context.driver)
    
@then('El nombre del titulo debe ser "{title_name}"')
def step_compare_names(context, title_name):
    actual_name = context.IMDb_title.get_title()
    assert actual_name == title_name, f"title's names don't match"

@then('El rating del titulo debe ser "{rating_value}"')
def step_compare_ratings(context, rating_value):
    actual_value = context.IMDb_title.get_rating()
    assert actual_value == rating_value, f"title's ranking don't match"


