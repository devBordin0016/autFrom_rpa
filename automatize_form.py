from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


options = Options()
options.add_experimental_option("detach", True)

drive_chrome = webdriver.Chrome(options=options)
drive_chrome.get("https://demoqa.com/automation-practice-form")

t.sleep(2)

frist_name = drive_chrome.find_element(By.ID, "firstName")
frist_name.send_keys("Fernando")
t.sleep(2)

last_name = drive_chrome.find_element(By.ID, "lastName")
last_name.send_keys("Bordin")
t.sleep(2)

email = drive_chrome.find_element(By.ID, "userEmail")
email.send_keys("devbordin@gmail.com")
t.sleep(2)

check_sex = drive_chrome.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
check_sex.click()
t.sleep(2)

phone_number = drive_chrome.find_element(By.ID, 'userNumber')
phone_number.send_keys("1996772016")
t.sleep(2)

date = drive_chrome.find_element(By.ID, "dateOfBirthInput")
drive_chrome.execute_script("arguments[0].value = '16 Dez 2000';", date)
t.sleep(2)

subject = drive_chrome.find_element(By.ID, 'subjectsInput')
subject.send_keys("Boy")
t.sleep(2)

hobbies = drive_chrome.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']")
hobbies.click()
t.sleep(2)

upload_picture = drive_chrome.find_element(By.ID, 'uploadPicture')
upload_picture.send_keys(r"C:\Users\FernandoBordin\Pictures\Screenshots\test_picture.png")
t.sleep(2)

current_address = drive_chrome.find_element(By.ID, 'currentAddress')
current_address.send_keys("Rua Altinopolis, 346, Sao Paulo, Agua Fria, SP")
t.sleep(2)

# Preenche o campo de Estado
state_input = drive_chrome.find_element(By.ID, "react-select-3-input")
state_input.send_keys("Haryana")
state_input.send_keys(Keys.ENTER)

# Aguarda um momento para a cidade ser carregada
t.sleep(2)

# Preenche o campo de Cidade
city_input = drive_chrome.find_element(By.ID, "react-select-4-input")
city_input.send_keys("Karnal")
city_input.send_keys(Keys.ENTER)
t.sleep(2)

button_submit = drive_chrome.find_element(By.ID, 'submit')
drive_chrome.execute_script("arguments[0].scrollIntoView(true);", button_submit)
button_submit.click()
t.sleep(2)

t.sleep(6)
drive_chrome.quit()
