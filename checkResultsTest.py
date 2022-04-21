from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Функция для преобразования строки в число
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False

# Инициализируем драйвер браузера и переходим на нужный сайт
driver = webdriver.Chrome()
driver.get("https://info.swsu.ru/index.php?action=auth")

# Находим поля для ввода текста и сразу вводим в них требуемые значения, подтверждая авторизацию
driver.find_element_by_id("loginemail").send_keys('login')
driver.find_element_by_id("password").send_keys('pass')
driver.find_element_by_name("click_autorize").click()

# Воспользуемся явным ожиданием
# Данный метод ожидает прогрузки всей страницы
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located
    )
finally:
    # Находим элемент - вкладка Студент и кликаем по нему
    driver.find_element_by_css_selector(".navbar-nav li:nth-child(2)").click()

# Находим во вкладке элемент - Рейтинг и кликаем по нему
driver.find_element_by_xpath("//*[@class='dropdown-menu show']/li[7]").click()
# Находим нашу текущую группу, а именно первый ссылочный элемент и кликаем по нему
driver.find_element_by_xpath("//div[contains(text(), 'ИБ-01м')]/a").click()
# Выбираем необходимый семестр
driver.find_element_by_xpath("//*[contains(text(), 'Третий семестр')]").click()

# Инициализируем неявное ожидание
driver.implicitly_wait(5)
# Объявляем переменные, result - для хранения результата сложения баллов
result = 0
# sum - для хранения значения, содержащегося в колонке Итоговый бал
sum = int(driver.find_element_by_xpath("//tr[3]/td[18]").text)
print(sum)

# Считываем все баллы из 3 строки (т.е. 3 предмета в списке), парсим и складываем в result
for i in range(7, 18):
    value = intTryParse(driver.find_element_by_xpath(f"//tr[3]/td[{i}]").text)
    print(value)
    if value[1]:
        result += int(value[0])

# Проверяем, корректно ли отображается сумма баллов на сайте
assert result == sum

driver.quit()