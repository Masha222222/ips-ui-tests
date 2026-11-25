import allure
from playwright.sync_api import expect


class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.pump_name = page.get_by_placeholder("например, student_ivanov", exact=True)
        self.apply_button = page.get_by_role("button", name="Применить")
        self.glucose_input = page.get_by_placeholder("glucose_value")
        self.send_button = page.get_by_role("button", name="Отправить")

    @allure.step("Открыть дашборд")
    def open(self):
        self.page.goto("https://ips.alexgallax-edu.ru/dashboard")

    @allure.step("Выбрать тестовую помпу {pump_id}")
    def select_pump(self, pump_id):
        self.pump_name.fill(pump_id)
        self.apply_button.click()

    @allure.step("Отправить значение глюкозы {value} через Devpanel")
    def send_glucose(self, value):
        self.glucose_input.fill(value)
        self.send_button.click()

    def expect_glucose(self, value, level):
        expect(
            self.page.get_by_text(value, exact=True),
            f"На дашборде должно появиться значение глюкозы {value}",
        ).to_be_visible()
        expect(
            self.page.get_by_text(level, exact=True),
            f"Для значения {value} должна появиться подпись «{level}»",
        ).to_be_visible()