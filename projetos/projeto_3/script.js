// aqui vai a API de conversão de moedas
function converter() {
    const valor = parseFloat(document.getElementById('valor').value);
    const moeda = document.getElementById('moeda').value;
    const resultado = document.getElementById('resultado');
    const simbolos = {
        USD: "$",
        EUR: "€",
        GBP: "£",
        JPY: "¥"
    };
    if (isNaN(valor)) {
        resultado.textContent = "Por favor, digite um valor válido em reais.";
        return;
    }
    if (moeda === "") {
        resultado.textContent = "Erro, por favor selecione uma moeda!";
        return;
    }
    fetch("https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_0EnEK29NWnAECwYPtHdGqF3i1n6NGaWbd31TBx8t")
        .then(response => response.json())
        .then(data => {
            console.log("API funcionando!");
            const brl = data.data.BRL;
            const cotacao = data.data[moeda];
            const valorEmUSD = valor / brl;
            const valorConvertido = valorEmUSD * cotacao;
            console.log(valorConvertido);
            let simbolo = "";
            if (moeda === "USD") {
                simbolo = "$";
            }
            else if (moeda === "EUR") {
                simbolo = "€";
            }
            else if (moeda === "GBP") {
                simbolo = "£";
            }
            else if (moeda === "JPY") {
                simbolo = "¥";
            }
            console.log("BRL:", data.data.BRL);
            console.log("Moeda:", moeda);
            console.log("Cotação:", cotacao);
            resultado.textContent = `Convertendo R$${valor} para ${simbolo}${valorConvertido.toFixed(2)}`;
        });
}
