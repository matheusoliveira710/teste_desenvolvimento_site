async function agendar() {
    const nome = document.getElementById('nome').value;
    const telefone = document.getElementById('telefone').value;
    const email = document.getElementById('email').value;
    const horario = document.getElementById('horario').value;

    if (nome === "" || horario === "" || email === "") {
        alert("Por favor, preencha todos os campos!");
        return;
    }

    // --- Lógica de verificação de uso único ---
    // Recupera a lista de agendamentos do navegador
    const agendamentosFeitos = JSON.parse(localStorage.getItem('agendamentos')) || [];

    // Verifica se já existe esse e-mail na lista
    const jaAgendou = agendamentosFeitos.find(item => item.email === email);

    if (jaAgendou) {
        alert("Você já realizou um agendamento com este e-mail, ou usando o mesmo horário!");
        return;
    }

    // --- Envio para o Discord ---
    const webhookURL = "https://discord.com/api/webhooks/1525267227983483042/mXQzbXonA-unN_4-fheXXBTXKe2m_TUcie6HVkKQRRmtUUk1qdXcXkHpu3cqfIbf-Kz3";
    const payload = {
        content: `📅 **Novo Agendamento!**\n👤 Cliente: ${nome}\n📞 Telefone: ${telefone}\n📧 Email: ${email}\n⏰ Horário: ${horario}`
    };

    try {
        const response = await fetch(webhookURL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            // --- Salva o agendamento no navegador para não permitir repetir ---
            agendamentosFeitos.push({ email: email });
            localStorage.setItem('agendamentos', JSON.stringify(agendamentosFeitos));

            alert(`Agendamento realizado com sucesso!`);
        } else {
            alert("Erro ao enviar para o Discord.");
        }
    } catch (error) {
        alert("Erro técnico ao conectar com o Discord.");
    }
}