import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://info.swsu.ru/index.php?action=auth")
time.sleep(5)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Ищем поле для ввода текста
loginField = driver.find_element_by_id("loginemail")
passField = driver.find_element_by_id("password")

# Заполним поля логин и пароль выбранными значениями
loginField.send_keys("loginAdmina")
passField.send_keys("passAdmina")
time.sleep(5)

# Найдем кнопку, которая отправит запрос на авторизацию
submit_button = driver.find_element_by_name("click_autorize")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
submit_button.click()
time.sleep(5)

# После, убедимся, что авторизация прошла неуспешно - найдя поле с уведомлением и проверив его содержимое
notification = driver.find_element(By.CSS_SELECTOR, '.alert')
assert "Логин или пароль неверный." in notification.text

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()