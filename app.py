import psycopg2, requests

TOKEN_ADRES = ' '

def get_connection():
    return psycopg2.connect(
        dbname="base",
        user="postgres",
        password=" ",
        host="localhost",
        port="5432"
    )

def update_price():
    url = f"https://api.dexscreener.com/latest/dex/search?q={TOKEN_ADRES}"
    response = requests.get(url)
    data = response.json()
    pair = data['pairs'][0]

    token_name = pair['baseToken']['name']
    price = float(pair['priceUsd'])

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO token_price (token_address, token_name, price_usd, last_updated)
        VALUES (%s, %s, %s, now())
        ON CONFLICT (token_address) DO UPDATE SET
            token_name = EXCLUDED.token_name,
            price_usd = EXCLUDED.price_usd,
            last_updated = now()
    """, (TOKEN_ADRES, token_name, price))
    conn.commit()
    cur.close()
    conn.close()

    print(f"Обновлено: {token_name} — {price} USD")

if __name__ == "__main__":
    update_price()
