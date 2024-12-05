from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to your ChromeDriver
driver_path = r"../chromedriver.exe"

# Create a Service object
service = Service(driver_path)

# Pass the Service object to the WebDriver
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.google.com")

# Print the page title
print("Page title is:", driver.title)

# Close the browser
driver.quit()