import allure

@allure.title("Успешная проверка сложения")
@allure.description("Этот тест делает одну проверку: корректность операции сложения.")
def test_math_ok():
    with allure.step("Складываем 2 и 2"):
        assert 2 + 4 == 6

@allure.title("Специально упавший тест")
def test_math_fail():
    with allure.step("Проверяем, что 2 + 2 равно 7"):
        assert 2 + 2 == 7
