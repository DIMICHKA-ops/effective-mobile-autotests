# Автотесты для effective-mobile.ru

Автоматизированные тесты для проверки навигации по главной странице effective-mobile.ru.

## Установка и запуск

### Локальный запуск:
```bash
# Установка зависимостей
pip install -r requirements.txt

# Установка браузеров
playwright install

# Запуск тестов
python -m pytest

# Запуск с подробным выводом
python -m pytest -v

# Запуск с генерацией Allure отчетов
python -m pytest -v --alluredir=allure-results

# Просмотр отчета Allure
allure serve allure-results

Запуск в Docker:

# Сборка образа
docker build -t effective-tests .

# Запуск тестов
docker run effective-tests

Тестовое покрытие

Тесты проверяют переходы по разделам главной страницы:

Навигация в раздел "О нас"

Навигация в раздел "Услуги"

Навигация в раздел "Контакты"

Навигация в раздел "Портфолио"

Структура проекта

effective-mobile-test/
├── pages/           # Page Object модели
│   └── main_page.py
├── tests/           # Тестовые сценарии
│   └── test_main_page.py
├── utils/           # Вспомогательные утилиты
│   └── config.py
├── requirements.txt # Зависимости Python
├── Dockerfile       # Конфигурация Docker
├── pytest.ini       # Конфигурация Pytest
├── conftest.py      # Фикстуры Pytest
└── README.md        # Документация

Используемые технологии

Python 3.10

Playwright

Pytest

Allure Framework

Docker

Особенности реализации

Использование паттерна Page Object Model

Поддержка запуска в Docker-контейнере

Генерация детализированных отчетов Allure

Проверка навигации по якорным ссылкам

## Результаты тестирования

**Все тесты успешно проходят:**
- Навигация в раздел "О нас" 
- Навигация в раздел "Услуги"
- Навигация в раздел "Контакты"
- Навигация в раздел "Портфолио"

**Поддержка запуска:**
- Локально (Python 3.10 + Playwright)
- В Docker контейнере

**Генерация отчетов:**
- Детальные отчеты Allure
- Скриншоты при ошибках (если настроено)
