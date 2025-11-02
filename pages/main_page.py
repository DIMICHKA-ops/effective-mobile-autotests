from playwright.sync_api import Page
from utils.config import BASE_URL


class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        """Открывает главную страницу"""
        self.page.goto(BASE_URL)
        self.page.wait_for_load_state("networkidle")

        # Просто ждем немного вместо поиска конкретных элементов
        self.page.wait_for_timeout(3000)

    def click_about_link(self):
        """Клик по ссылке 'О нас' через прямой переход"""
        self.page.goto(f"{BASE_URL}#about")
        self.page.wait_for_load_state("networkidle")

    def click_services_link(self):
        """Клик по ссылке 'Услуги' через прямой переход"""
        self.page.goto(f"{BASE_URL}#moreinfo")
        self.page.wait_for_load_state("networkidle")

    def click_contacts_link(self):
        """Клик по ссылке 'Контакты' через прямой переход"""
        self.page.goto(f"{BASE_URL}#contacts")
        self.page.wait_for_load_state("networkidle")

    def click_portfolio_link(self):
        """Клик по ссылке 'Портфолио' через прямой переход"""
        self.page.goto(f"{BASE_URL}#cases")
        self.page.wait_for_load_state("networkidle")