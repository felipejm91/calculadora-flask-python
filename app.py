from flask import Flask, request, render_template
from controllers import calculadora

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calc():
    resultado = 0

    if request.method == 'POST':
        n1 = request.form.get('numero1')
        n2 = request.form.get('numero2')

        if request.form.get('soma'):
            resultado = calculadora.soma(n1, n2)
        elif request.form.get('subtracao'):
            resultado = calculadora.subtracao(n1, n2)
        elif request.form.get('divisao'):
            resultado = calculadora.divisao(n1, n2)
        elif request.form.get('multiplicacao'):
            resultado = calculadora.multiplicacao(n1, n2)

    return render_template('calculadora.html', resultado=resultado)


if __name__ == '__main__':
    app.run()
