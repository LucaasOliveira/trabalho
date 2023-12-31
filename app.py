from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados de exemplo para o glossário e tarefas
glossario = []
tarefas = []

@app.route('/')
def index():
    return render_template('index.html')

# Rotas para o glossário
@app.route('/glossario')
def listar_glossario():
    return render_template('glossario.html', glossario=glossario)

@app.route('/glossario/adicionar', methods=['GET', 'POST'])
def adicionar_termo():
    if request.method == 'POST':
        termo = request.form['termo']
        glossario.append(termo)
        return redirect(url_for('listar_glossario'))
    return render_template('adicionar_termo.html')

@app.route('/glossario/alterar/<termo>', methods=['GET', 'POST'])
def alterar_termo(termo):
    if request.method == 'POST':
        novo_termo = request.form['novo_termo']
        index = glossario.index(termo)
        glossario[index] = novo_termo
        return redirect(url_for('listar_glossario'))
    return render_template('alterar_termo.html', termo=termo)

@app.route('/glossario/deletar/<termo>')
def deletar_termo(termo):
    glossario.remove(termo)
    return redirect(url_for('listar_glossario'))

# Rotas para tarefas
@app.route('/tarefas')
def listar_tarefas():
    return render_template('tarefas.html', tarefas=tarefas)

@app.route('/tarefas/adicionar', methods=['GET', 'POST'])
def adicionar_tarefa():
    if request.method == 'POST':
        tarefa = request.form['tarefa']
        tarefas.append(tarefa)
        return redirect(url_for('listar_tarefas'))
    return render_template('adicionar_tarefa.html')

@app.route('/tarefas/alterar/<tarefa>', methods=['GET', 'POST'])
def alterar_tarefa(tarefa):
    if request.method == 'POST':
        nova_tarefa = request.form['nova_tarefa']
        index = tarefas.index(tarefa)
        tarefas[index] = nova_tarefa
        return redirect(url_for('listar_tarefas'))
    return render_template('alterar_tarefa.html', tarefa=tarefa)

@app.route('/tarefas/deletar/<tarefa>')
def deletar_tarefa(tarefa):
    tarefas.remove(tarefa)
    return redirect(url_for('listar_tarefas'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
