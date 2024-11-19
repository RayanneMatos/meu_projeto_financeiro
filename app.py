from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Lista de transações em memória
transactions = []

# Página inicial: Mostra o saldo e links para cadastrar e ver relatório
@app.route('/')
def index():
    total_balance = sum(t['amount'] if t['type'] == 'receita' else -t['amount'] for t in transactions)
    return render_template('index.html', balance=total_balance)

# Página para adicionar transação
@app.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction_type = request.form['type']
        amount = request.form['amount'].replace(',', '.')  # Substitui a vírgula por ponto
        amount = float(amount)  # Converte para float
        description = request.form['description']
        
        new_transaction = {
            'type': transaction_type,
            'amount': amount,
            'description': description,  # Adicionando a descrição à transação
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        transactions.append(new_transaction)
        return redirect(url_for('index'))
    
    return render_template('add_transaction.html')

# Página de relatório: lista de todas as transações
@app.route('/report')
def report():
    receitaTotal = sum(t['amount'] for t in transactions if t['type'] == 'receita')
    despesaTotal = sum(t['amount'] for t in transactions if t['type'] == 'despesa')
    total_balance = receitaTotal - despesaTotal
    return render_template('report.html', balance=total_balance, transactions=transactions, receitaTotal=receitaTotal, despesaTotal=despesaTotal)

if __name__ == '__main__':
    app.run(debug=True)