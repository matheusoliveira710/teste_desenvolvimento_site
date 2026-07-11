function mostrarStatus(mensagem, cor) {
    const statusDiv = document.getElementById('mensagem-status');
    statusDiv.innerText = mensagem;
    statusDiv.style.backgroundColor = cor;
    statusDiv.style.display = 'block';
    
    // Esconde após 5 segundos
    setTimeout(() => { statusDiv.style.display = 'none'; }, 5000);
}

async function agendar() {
    const btn = document.getElementById('btnAgendar');
    const nome = document.getElementById('nome').value;
    const telefone = document.getElementById('telefone').value;
    const email = document.getElementById('email').value;
    const horario = document.getElementById('horario').value;

    // 1. Desabilita logo de início
    btn.disabled = true;
    btn.innerText = "Agendando...";

    // 2. Validação básica
    if (nome === "" || horario === "" || email === "") {
        alert("Por favor, preencha todos os campos!");
        btn.disabled = false; // Reativa para o usuário poder tentar de novo
        btn.innerText = "Agendar";
        return; // Sai da função aqui
    }

    // 3. Verificação de uso único
    const agendamentosFeitos = JSON.parse(localStorage.getItem('agendamentos')) || [];
    const jaAgendou = agendamentosFeitos.find(item => item.email === email);

    if (jaAgendou) {
        alert("Você já realizou o agendamento!");
        btn.disabled = false; // Reativa para o usuário poder tentar de novo
        btn.innerText = "Agendar";
        return; // Sai da função aqui
    }

    // 4. Envio para o Discord
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
            mostrarStatus("Sucesso! Agendamento enviado.", "#d4edda");
            document.getElementById('formAgendamento').reset();
        } else {
            mostrarStatus("Erro ao conectar com servidor.", "#f8d7da");
        }
    } catch (error) {
        alert("Erro técnico ao conectar com o Discord.");
    } finally {
        // O finally reativa caso tenha chegado no try/catch
        btn.disabled = false;
        btn.innerText = "Agendar";
    }
}