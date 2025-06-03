import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    url = "https://www.cm-viana-castelo.pt/agenda/"
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_count = 0
    max_scrolls = 10  # Para evitar scroll infinito

    while scroll_count < max_scrolls:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Aumentado para 5 segundos
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        scroll_count += 1

    eventos = driver.find_elements(By.CSS_SELECTOR, "div.event-001-inner-content")
    print(f"Eventos encontrados: {len(eventos)}")

    for evento in eventos:
        data = evento.find_element(By.CSS_SELECTOR, "div.event-001-inner-date-inner").text.strip()
        titulo = evento.find_element(By.CSS_SELECTOR, "h2.event-001-inner-text-inner").text.strip()
        link_element = evento.find_element(By.XPATH, "./ancestor::a[1]")
        link = link_element.get_attribute("href") if link_element else "Sem link"

        print({
            "titulo": titulo,
            "data": data,
            "link": link
        })

finally:
    driver.quit()
