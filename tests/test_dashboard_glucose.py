import allure
import pytest


@allure.title("Дашборд показывает значение {value} и подпись «{level}»")
@pytest.mark.parametrize(
    "value, level",
    [
        ("6.0", "Норма"),
        ("12.0", "Высокий"),
    ],
    ids=["normal", "high"],
)
def test_dashboard_shows_glucose(dashboard, test_pump_id, value, level):
    dashboard.open()
    dashboard.select_pump(test_pump_id)
    dashboard.send_glucose(value)

    dashboard.expect_glucose(value, level)