const visor = document.getElementById("visor");
const botoes = document.querySelectorAll("button");

botoes.forEach(botao => {
    botao.addEventListener("click", () => {
            if (botao.textContent === "C") {
                visor.value = "";
            }
            else {
                visor.value += botao.textContent;
            }
    });
});
