import undetected_chromedriver as uc

CHROME_BINARY_PATH = "/usr/bin/chromium"  # Update this path if necessary

def main():
    driver = uc.Chrome(binary_location=CHROME_BINARY_PATH)
    driver.get('https://www.example.com')
    print("Title:", driver.title)
    input("Press enter to close the browser...")
    driver.quit()
if __name__ == "__main__":
    main()