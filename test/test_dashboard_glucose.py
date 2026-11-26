import allure
import pytest


@allure.title("Дашборд показывает значение {value} и подпись «{level}»")
@pytest.mark.parametrize(
    "value, level",
    [
        pytest.param("4.4", "Низкий", id="below-lower-bound"),
        pytest.param("4.5", "Низкий", id="at-lower-bound"),
        pytest.param("4.6", "Норма", id="above-lower-bound"),
        pytest.param("9.9", "Норма", id="below-upper-bound"),
        pytest.param("10.0", "Высокий", id="at-upper-bound"),
        pytest.param("10.1", "Высокий", id="above-upper-bound"),
    ],
)

def test_dashboard_shows_glucose(dashboard, test_pump_id, value, level):
    dashboard.open()
    dashboard.select_pump(test_pump_id)
    dashboard.send_glucose(value)

    dashboard.expect_glucose(value, level)