import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(filename="log.txt", level=logging.INFO, format="%(asctime)s — %(message)s")

def main():
    print("Программа genacryptocomgit запущена.")
    logging.info("Программа успешно запущена.")

if __name__ == "__main__":
    main()
