window.addEventListener('load', () => {
    let btn = document.getElementById('btn-submit');

    let calculoCoordenada = (formulario) => {
        let formElements = formulario.querySelectorAll('.formElement');
        let coordenada = 0;

        for(let i = 0; i < formElements.length; i++) {
            let aux = formElements[i].getElementsByTagName('select')[0].value;
            coordenada += parseInt(aux);
        }

        return coordenada;
    }

    btn.addEventListener('click', (e) => {
        e.preventDefault();

        let formulario_complejidad = document.querySelector('#preguntas-complejidad');
        let formulario_tecnologias = document.querySelector('#preguntas-tegnologia');

        let x = calculoCoordenada(formulario_complejidad);
        let y = calculoCoordenada(formulario_tecnologias);

        location.href ="/?x=" + x + "&y=" + y;
    });
});