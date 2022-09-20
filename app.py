from flask import Flask, request, render_template
from controllers import calculadora

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calc():
    resultado = 0

    if request.method == 'POST':
        n1 = request.form.get('numero1')
        n2 = request.form.get('numero2')

        if request.form.get('nSoma'):
            resultado = calculadora.soma(n1, n2)
        elif request.form.get('nSubtracao'):
            resultado = calculadora.subtracao(n1, n2)
        elif request.form.get('nDivisao'):
            resultado = calculadora.divisao(n1, n2)
        elif request.form.get('nMultiplicacao'):
            resultado = calculadora.multiplicacao(n1, n2)

    return render_template('calculadora.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=False)
