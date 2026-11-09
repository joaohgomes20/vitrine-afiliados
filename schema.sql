-- schema.sql
-- Tabela de Produtos para o site de Afiliados (Achadinhos)

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    store TEXT NOT NULL,              -- 'Mercado Livre', 'Shopee', 'Amazon', 'Magalu'
    category TEXT NOT NULL,           -- 'Eletrônicos', 'Casa', 'Moda', 'Beleza', 'Gamer'
    original_price REAL,              -- Preço "De" (ex: 299.90)
    promotional_price REAL NOT NULL,  -- Preço "Por" (ex: 189.90)
    discount_tag TEXT,                -- '35% OFF', 'Frete Grátis', 'Menor Preço'
    badge TEXT,                       -- 'Mais Vendido', 'Achadinho', 'Top Oferta', ou vazio
    image_url TEXT NOT NULL,          -- URL da foto do produto
    affiliate_url TEXT NOT NULL,      -- Seu link de afiliado
    clicks_count INTEGER DEFAULT 0,   -- Contador de cliques
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_products_store ON products(store);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
