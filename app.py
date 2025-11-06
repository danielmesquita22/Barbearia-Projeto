from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3, os

app = Flask(__name__)
app.secret_key = "chave_super_secreta"

# --- Função para conectar no banco ---
def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- Login ---
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        senha = request.form['senha']
        conn = get_db()
        admin = conn.execute("SELECT * FROM admin WHERE usuario=? AND senha=?", (usuario, senha)).fetchone()
        if admin:
            session['usuario'] = usuario
            return redirect(url_for('dashboard'))
    return render_template('admin_login.html')

# --- Painel principal ---
@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('admin_login'))
    conn = get_db()
    servicos = conn.execute("SELECT * FROM servicos").fetchall()
    return render_template('admin_dashboard.html', servicos=servicos)

# --- Logout ---
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    app.run(debug=True)
