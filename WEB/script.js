document.addEventListener('load', initialize())


function setSizeFrame(){
    let elemento = document.querySelector('#tela'); // obtem o campo do frame
    elemento.style.cssText = 'width: 80%; height: 700px;'; // seta a altura e largura do frame
}

function initialize(){
    setSizeFrame()
    onSiga()
}

function onSiga(){
    document.querySelector("#siga").style.cssText = 'color: white'
    mostrarSiga()
}

function mostrarSiga(){
    var newSrc = "https://siga.cps.sp.gov.br/ALUNO/login.aspx"
    document.getElementById('tela').src = newSrc;

}

function offSiga(){
    document.querySelector("#siga").style.cssText = 'color: black'
}

function onCalendario(){
    document.querySelector("#calendario").style.cssText = 'color: white'
    mostrarCalendario()
}

function mostrarCalendario(){
    var newSrc = "../PDFs/calendario.pdf"
    document.getElementById('tela').src = newSrc;

}

function offCalendario(){
    document.querySelector("#calendario").style.cssText = 'color: black'
}

function onHorario(){
    document.querySelector("#horario").style.cssText = 'color: white'
    mostrarHorario()
}

function mostrarHorario(){
    var newSrc = "../PDFs/horario.pdf"
    document.getElementById('tela').src = newSrc;

}

function offHorario(){
    document.querySelector("#horario").style.cssText = 'color: black'
}

const btn_Siga = document.getElementById('siga');

btn_Siga.addEventListener('click', clickSiga)

function clickSiga(){
    onSiga()
    offCalendario()
    offHorario()
}

const btn_Calendario = document.getElementById('calendario');

btn_Calendario.addEventListener('click', clickCalendario)

function clickCalendario(){
    onCalendario()
    offSiga()
    offHorario()
}

const btn_Horario = document.getElementById('horario');

btn_Horario.addEventListener('click', clickHorario)

function clickHorario(){
    onHorario()
    offSiga()
    offCalendario()
}