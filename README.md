# 🛍️ Vitrine de Afiliados ("Achadinhos & Promoções")

Um site completo e moderno para revender produtos como afiliado do **Mercado Livre**, **Shopee**, **Amazon**, **Magalu** e outras lojas parceiras.

---

## 🌟 Recursos Principais

1. **Vitrine Moderna ("Achadinhos")**:
   - Layout responsivo (otimizado para celular e computador) com visual profissional.
   - Cards com foto, badge da loja (Mercado Livre em amarelo, Shopee em laranja, Amazon em azul), preços ("De" e "Por"), desconto calculado e selos como *Achadinho* e *Mais Vendido*.
   - Filtros instantâneos por **Loja** (Shopee, Mercado Livre, Amazon) e **Categoria** (Eletrônicos, Casa, Gamer, Moda, Beleza).
   - Barra de busca por nome de produto.
   - Botão para canal VIP de ofertas no WhatsApp / Telegram.

2. **Rastreamento de Cliques (`/redirect/<id>`)**:
   - Quando o visitante clica em "Pegar Promoção", o site computa o clique no banco de dados antes de redirecionar para o seu link de parceiro.

3. **Painel de Controle Visual (`/admin`)**:
   - Cadastre novos produtos preenchendo um formulário no navegador (sem precisar escrever código ou SQL).
   - Preview da imagem em tempo real.
   - Tabela para acompanhar quantos cliques cada produto recebeu.
   - Botão de exclusão rápida.

4. **Banco de Dados Local (SQLite)**:
   - Os produtos, links e cliques ficam salvos com segurança no arquivo `afiliados.db`.

---

## 🚀 Como Executar o Site

1. Abra o terminal na pasta do projeto:
   ```bash
   cd C:\Users\joaoh\.gemini\antigravity\scratch\vitrine-afiliados
   ```

2. Instale as dependências (caso ainda não tenha feito):
   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor:
   ```bash
   python app.py
   ```

4. Abra no seu navegador:
   * **Vitrine pública de ofertas:** [http://localhost:5000](http://localhost:5000)
   * **Painel para cadastrar produtos:** [http://localhost:5000/admin](http://localhost:5000/admin)

---

## 💡 Como Funciona o Trabalho de Afiliado na Prática?

1. **Faça o cadastro nos programas oficiais:**
   * **Shopee Afiliados:** [affiliate.shopee.com.br](https://affiliate.shopee.com.br)
   * **Mercado Livre Afiliados:** [afiliados.mercadolivre.com.br](https://afiliados.mercadolivre.com.br)
   * **Amazon Associados:** [associados.amazon.com.br](https://associados.amazon.com.br)

2. **Garimpe bons produtos:**
   * Procure produtos com boas avaliações (4.8+ estrelas) e bom desconto.

3. **Copie seu link de afiliado:**
   * O portal de afiliados gera um link exclusivo para você (ex: `https://shope.ee/xyz...` ou `https://mercadolivre.com/sec/...`).

4. **Cadastre no painel `/admin`:**
   * Cole o título, preço, a foto e o seu link de afiliado. O produto entra no ar imediatamente na sua vitrine!
