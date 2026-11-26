import re

import allure
import pytest
from playwright.sync_api import expect
NORMAL_GLUCOSE_VALUE = "6.0"

@allure.title("После отправки глюкозы {value} счётчик тревог растёт на 1")
@pytest.mark.parametrize(
    "value",
    [
        pytest.param("4.4", id="low"),
        pytest.param("10.1", id="high"),
    ],
)
def test_alert_count_increases_by_one(dashboard, test_pump_id, value):
    dashboard.open()
    dashboard.select_pump(test_pump_id)

    before = dashboard.read_alert_count()
    dashboard.send_glucose(value)

    expected = before + 1
    expect(
        dashboard.alerts_link,
        f"После отправки {value} счётчик тревог должен вырасти "
        f"с {before} до {expected}",
    ).to_have_accessible_name(re.compile(rf"Тревоги\s+{expected}$"))


@allure.title("При нормальном уровне глюкозы новая тревога не появляется")
def test_normal_glucose_does_not_add_alert(dashboard, test_pump_id):
    dashboard.open()
    dashboard.select_pump(test_pump_id)
    before = dashboard.read_alert_count()

    dashboard.send_glucose(NORMAL_GLUCOSE_VALUE)
    dashboard.expect_glucose(NORMAL_GLUCOSE_VALUE, "Норма")

    after = dashboard.read_alert_count()
    assert after == before, (
        f"При глюкозе {NORMAL_GLUCOSE_VALUE} счётчик тревог должен "
        f"остаться {before}, получено {after}"
    )