// aqui vai a API de conversão de moedas

function converter() {
    const valor = parseFloat(document.getElementById('valor').value);
    const moeda = document.getElementById('moeda').value;
    const resultado = document.getElementById('resultado');
    if (isNaN(valor)) {
        resultado.textContent = "Por favor, digite um valor válido em reais.";
        return;
    }
    //parsefloat("")
    resultado.textContent = valor + " " + moeda;
}
