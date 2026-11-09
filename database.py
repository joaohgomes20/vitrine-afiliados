"""
database.py - Gerenciamento do banco de dados SQLite para o site de afiliados
"""
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "afiliados.db")
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.sql")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

    # Verifica se já existem produtos cadastrados
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM products")
    count = cursor.fetchone()[0]

    if count == 0:
        sample_products = [
            (
                "Fone de Ouvido Bluetooth Sem Fio TWS com Cancelamento de Ruído",
                "Shopee",
                "Eletrônicos",
                89.90,
                39.90,
                "55% OFF",
                "Achadinho",
                "https://images.unsplash.com/photo-1590658268037-6bf12165a8df?w=600&auto=format&fit=crop&q=80",
                "https://shopee.com.br"
            ),
            (
                "Fritadeira Elétrica Air Fryer 4L Inox 1500W Antiaderente",
                "Mercado Livre",
                "Casa",
                389.00,
                269.90,
                "30% OFF",
                "Mais Vendido",
                "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80",
                "https://mercadolivre.com.br"
            ),
            (
                "Luminária de Mesa Inteligente LED RGB com Carregador por Indução",
                "Shopee",
                "Casa",
                129.90,
                64.50,
                "50% OFF",
                "Top Oferta",
                "https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600&auto=format&fit=crop&q=80",
                "https://shopee.com.br"
            ),
            (
                "Mouse Gamer Ergonômico RGB 7 Botões 7200 DPI Alta Precisão",
                "Mercado Livre",
                "Gamer",
                119.00,
                59.90,
                "49% OFF",
                "Menor Preço",
                "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=600&auto=format&fit=crop&q=80",
                "https://mercadolivre.com.br"
            ),
            (
                "Garrafa Térmica Inox 1 Litro a Vácuo Parede Dupla 24h Quente/Frio",
                "Amazon",
                "Casa",
                99.90,
                54.90,
                "45% OFF",
                "Achadinho",
                "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=600&auto=format&fit=crop&q=80",
                "https://amazon.com.br"
            ),
            (
                "Suporte Articulado Dobrável para Notebook e Tablet Alumínio",
                "Shopee",
                "Eletrônicos",
                79.90,
                38.90,
                "51% OFF",
                "Recomendado",
                "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=600&auto=format&fit=crop&q=80",
                "https://shopee.com.br"
            )
        ]

        cursor.executemany(
            """
            INSERT INTO products 
            (title, store, category, original_price, promotional_price, discount_tag, badge, image_url, affiliate_url)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            sample_products
        )
        conn.commit()

    conn.close()

def get_products(search=None, store=None, category=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM products WHERE 1=1"
    params = []

    if search:
        query += " AND (title LIKE ? OR store LIKE ? OR category LIKE ?)"
        wildcard = f"%{search}%"
        params.extend([wildcard, wildcard, wildcard])

    if store and store.lower() != 'todos':
        query += " AND LOWER(store) = LOWER(?)"
        params.append(store)

    if category and category.lower() != 'todas':
        query += " AND LOWER(category) = LOWER(?)"
        params.append(category)

    query += " ORDER BY id DESC"
    cursor.execute(query, params)
    products = cursor.fetchall()
    conn.close()
    return products

def get_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

def add_product(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO products 
        (title, store, category, original_price, promotional_price, discount_tag, badge, image_url, affiliate_url)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            data["title"],
            data["store"],
            data["category"],
            float(data["original_price"]) if data.get("original_price") else None,
            float(data["promotional_price"]),
            data.get("discount_tag", ""),
            data.get("badge", ""),
            data["image_url"],
            data["affiliate_url"]
        )
    )
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def delete_product(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))
    conn.commit()
    conn.close()

def increment_click(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET clicks_count = clicks_count + 1 WHERE id = ?", (product_id,))
    conn.commit()
    cursor.execute("SELECT affiliate_url FROM products WHERE id = ?", (product_id,))
    row = cursor.fetchone()
    conn.close()
    return row["affiliate_url"] if row else None

def get_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) as total_products, COALESCE(SUM(clicks_count), 0) as total_clicks FROM products")
    stats = cursor.fetchone()
    conn.close()
    return stats
