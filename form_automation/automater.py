from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument("-incognito")

for i in range(1,25):
    browser = webdriver.Chrome(executable_path='.\chromedriver.exe', options=option)
    browser.get("form link here")
    radiobuttons = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoice")
    submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")

    radiobuttons[1].click()
    radiobuttons[6].click()
    radiobuttons[8].click()
    radiobuttons[13].click()
    radiobuttons[15].click()
    radiobuttons[18].click()
    radiobuttons[20].click()
    radiobuttons[24].click()
    radiobuttons[26].click()
    submitbutton[0].click()
    browser.close()