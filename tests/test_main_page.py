import pytest
import allure
from playwright.sync_api import expect
from pages.main_page import MainPage


class TestMainPageNavigation:
    """Тесты навигации по главной странице effective-mobile.ru"""

    @allure.title("Переход в раздел 'О нас'")
    def test_navigate_to_about_section(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_about_link()

        # Проверяем URL содержит якорь #about
        expect(page).to_have_url("https://effective-mobile.ru/#about")

    @allure.title("Переход в раздел 'Услуги'")
    def test_navigate_to_services_section(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_services_link()

        expect(page).to_have_url("https://effective-mobile.ru/#moreinfo")

    @allure.title("Переход в раздел 'Контакты'")
    def test_navigate_to_contacts_section(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_contacts_link()

        expect(page).to_have_url("https://effective-mobile.ru/#contacts")

    @allure.title("Переход в раздел 'Портфолио'")
    def test_navigate_to_portfolio_section(self, page):
        main_page = MainPage(page)
        main_page.open()
        main_page.click_portfolio_link()

        expect(page).to_have_url("https://effective-mobile.ru/#cases")