# dexscreener-token
Python-скрипт для получения актуальной цены токена с Dexscreener и сохранения её в PostgreSQL.

---

## Требования

* Python 3.10+
* Библиотеки: `psycopg2`, `requests`
* PostgreSQL с таблицей:

```sql
CREATE TABLE IF NOT EXISTS token_price (
    token_address TEXT PRIMARY KEY,
    token_name TEXT NOT NULL,
    price_usd NUMERIC NOT NULL,
    last_updated TIMESTAMP NOT NULL
);
```

---

## Настройка

1. Установите зависимости:

```bash
pip install psycopg2 requests
```

2. Вставьте ваш токен адрес в `TOKEN_ADRES`:

```python
TOKEN_ADRES = 'ВАШ_АДРЕС_ТОКЕНА'
```

3. Обновите данные для подключения к базе в функции `get_connection()`:

```python
return psycopg2.connect(
    dbname="base",
    user="postgres",
    password="ВАШ_ПАРОЛЬ",
    host="localhost",
    port="5432"
)
```

---

## Запуск

```bash
python app.py
```

Пример вывода:

```
Обновлено: TokenName — 0.123 USD
```

Скрипт:

* Получает данные токена с Dexscreener API.
* Вставляет запись в таблицу `token_price`.
* Если токен уже есть в таблице, обновляет цену и время последнего обновления.
