document.addEventListener('DOMContentLoaded', function() {

    const radiosTipoVenda = document.querySelectorAll('input[name="tipo_venda"]');

    radiosTipoVenda.forEach(radio => {
        radio.addEventListener('change', function() {
            const etapa1 = document.getElementById('etapaVenda1');
            const etapa2 = document.getElementById('etapaVenda2');

            etapa1.style.display = 'none';
            etapa2.style.display = 'block';
        })
    })
})