const visor = document.getElementById("visor");
const botoes = document.querySelectorAll("button");

botoes.forEach(botao => {
    botao.addEventListener("click", () => {
            if (botao.textContent === "⌫") {
                visor.value = visor.value.slice(0, -1);
            }
            else if (botao.textContent === "C") {
                visor.value = "";   
            }
            else if (botao.textContent === "=") {
                visor.value = eval(visor.value);
            }
            else {
                visor.value += botao.textContent;
            }
    });
});
