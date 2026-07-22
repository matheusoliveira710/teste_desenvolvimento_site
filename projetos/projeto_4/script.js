const ctx = document.getElementById('meuGrafico').getContext('2d');
let meuGrafico = new Chart(ctx, {
    type: 'pie',
    data: {
        labels: [],
        datasets: [{
            data: [],
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
        }]
    }
});

document.getElementById('formFinanceiro').addEventListener('submit', function(e) {
    e.preventDefault();

    const categoria = document.getElementById('categoria').value;
    
    // Substitui vírgula por ponto e converte para decimal
    const valorTexto = document.getElementById('valor').value.replace(',', '.');
    const valor = parseFloat(valorTexto);

    // Validação para garantir que é um número válido
    if (isNaN(valor)) {
        alert("Por favor, digite um valor numérico válido.");
        return;
    }

    // Adiciona ao gráfico
    meuGrafico.data.labels.push(categoria);
    meuGrafico.data.datasets[0].data.push(valor);
    
    meuGrafico.update();
    this.reset();
});
