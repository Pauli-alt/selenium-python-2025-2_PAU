from behave import given, when, then
from selenium import webdriver
from pages.lastfm_home_page import LastFmHomePage
from pages.lastfm_results_page import LastFmResultsPage
from pages.lastfm_artist_page import LastFmArtistPage

@given('el usuario esta en el home page de last.fm')
def step_home_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.last.fm/")
    context.lastfm_home = LastFmHomePage(context.driver)

@when('el usuario busca el artista "{artist_name}"')
def step_search_artist(context, artist_name):
    context.lastfm_home.search_artist(artist_name)
    context.lastfm_results = LastFmResultsPage(context.driver)


@when('presiona el link del primer resultado')
def step_press_link(context):
    context.lastfm_results.press_link()
    context.lastfm_artist = LastFmArtistPage(context.driver)

@then('la fecha del ultimo release debe ser "{expected_date}"')
def step_compare_dates(context, expected_date):

    actual_date = context.lastfm_artist.get_latest_releases()
    assert actual_date == expected_date, f"release date dont match"