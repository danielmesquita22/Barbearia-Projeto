// Função para formatar a mensagem do WhatsApp com o serviço selecionado
function formatarMensagemWhatsApp(servico, preco) {
    const hoje = new Date();
    const dataFormatada = hoje.toLocaleDateString('pt-BR');
    return encodeURIComponent(`Olá! Gostaria de agendar um horário para ${servico} (R$ ${preco}). Data pretendida: ${dataFormatada}`);
}

// Função para verificar se está no horário de funcionamento
function verificarHorarioFuncionamento() {
    const agora = new Date();
    const hora = agora.getHours();
    const dia = agora.getDay(); // 0 = Domingo, 1-6 = Segunda-Sábado

    const horarioComercial = hora >= 9 && hora < 20;
    const horarioDomingo = hora >= 9 && hora < 14;
    const isDomingo = dia === 0;
    
    return isDomingo ? horarioDomingo : horarioComercial;
}

// Configurar os cards de serviço
document.addEventListener('DOMContentLoaded', function() {
    const cards = document.querySelectorAll('.servico-card');
    const telefone = '5511999999999'; // Substitua pelo número real

    cards.forEach(card => {
        const servico = card.querySelector('h3').textContent;
        const precoTexto = card.querySelector('.servico-preco').textContent;
        const preco = precoTexto.replace('R$ ', '').replace(',', '.');
        
        const botao = card.querySelector('.servico-agendar');
        
        botao.addEventListener('click', function(e) {
            e.stopPropagation(); // Evita que o onclick do card seja acionado
            
            if (!verificarHorarioFuncionamento()) {
                alert('Desculpe, estamos fora do horário de atendimento. Por favor, volte no nosso horário comercial.');
                return;
            }
            
            const mensagem = formatarMensagemWhatsApp(servico, preco);
            window.open(`https://wa.me/${telefone}?text=${mensagem}`, '_blank');
        });
    });
});

// Animação suave do scroll para links internos
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});