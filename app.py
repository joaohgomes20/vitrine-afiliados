"""
app.py - Servidor Web Flask para Vitrine de Afiliados (Achadinhos & Ofertas)
"""
import os
from flask import Flask, render_template, request, redirect, abort
from database import init_db, get_products, add_product, delete_product, increment_click, get_stats

app = Flask(__name__)

# Garante que o banco de dados e as tabelas estejam prontos
with app.app_context():
    init_db()

@app.route("/")
def home():
    search = request.args.get("q", "").strip()
    store = request.args.get("loja", "").strip()
    category = request.args.get("categoria", "").strip()

    products = get_products(search=search, store=store, category=category)
    return render_template(
        "index.html", 
        products=products, 
        search=search, 
        store=store, 
        category=category
    )

@app.route("/redirect/<int:product_id>")
def redirect_affiliate(product_id):
    """
    Registra o clique no banco de dados e redireciona para a loja parceira
    com o código do afiliado!
    """
    target_url = increment_click(product_id)
    if not target_url:
        abort(404)
    return redirect(target_url, code=302)

@app.route("/admin")
def admin():
    products = get_products()
    stats = get_stats()
    return render_template("admin.html", products=products, stats=stats)

@app.route("/admin/add", methods=["POST"])
def admin_add():
    title = request.form.get("title", "").strip()
    store = request.form.get("store", "Shopee").strip()
    category = request.form.get("category", "Geral").strip()
    original_price = request.form.get("original_price", "").strip()
    promotional_price = request.form.get("promotional_price", "").strip()
    discount_tag = request.form.get("discount_tag", "").strip()
    badge = request.form.get("badge", "").strip()
    image_url = request.form.get("image_url", "").strip()
    affiliate_url = request.form.get("affiliate_url", "").strip()

    # Cálculo automático de porcentagem de desconto caso o usuário não preencha
    if not discount_tag and original_price and promotional_price:
        try:
            orig = float(original_price)
            promo = float(promotional_price)
            if orig > promo and orig > 0:
                pct = int(round(((orig - promo) / orig) * 100))
                discount_tag = f"{pct}% OFF"
        except ValueError:
            pass

    data = {
        "title": title,
        "store": store,
        "category": category,
        "original_price": float(original_price) if original_price else None,
        "promotional_price": float(promotional_price),
        "discount_tag": discount_tag,
        "badge": badge,
        "image_url": image_url,
        "affiliate_url": affiliate_url
    }

    add_product(data)
    return redirect("/admin")

@app.route("/admin/delete/<int:product_id>", methods=["POST"])
def admin_delete(product_id):
    delete_product(product_id)
    return redirect("/admin")

if __name__ == "__main__":
    print("\n🚀 Vitrine de Afiliados rodando!")
    print("👉 Acesse a vitrine pública: http://localhost:5000")
    print("👉 Acesse o painel admin:    http://localhost:5000/admin\n")
    app.run(host="127.0.0.1", port=5000, debug=True)
