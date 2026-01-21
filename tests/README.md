# Финальный проект — вторая часть (Яндекс Самокат)

**Автор:** Таир Искаков  
**Когорта:** 38  

## Состав репозитория
- `queries.sql` — SQL-запросы для проверки данных в БД
- `configuration.py` — настройки API
- `data.py` — тело запроса для создания заказа
- `sender_stand_requests.py` — функции работы с API
- `tests/test_order_api.py` — автотест API
- `artifacts/screenshot_test_result.png` — скрин запуска теста

## Запуск тестов
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pytest -v