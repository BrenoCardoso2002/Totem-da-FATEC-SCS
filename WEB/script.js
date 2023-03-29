/*
    Essa primeira parte do código é a parte que cria variaveis constante que seram relativas aos componentes da tela.  
*/

const pagina = document // essa variavel referencia a pagina.
const tela = document.getElementById('tela') // essa variavel referencia o frame.
const bSiga = document.getElementById('siga') // essa variavel referencia o botão siga.
const bCalendario = document.getElementById('calendario') // essa variavel referencia o botão calendario.
const bHorario = document.getElementById('horario') // essa variavel referencia o botão horario.

/*
    Essa segunda parte do código é a parte que terá os eventos dos componentes.  
*/

pagina.addEventListener('load', initialize()) // evento de carregar página.
bSiga.addEventListener('click', clickSiga) // evento de click do botão siga
bCalendario.addEventListener('click', clickCalendario) // evento de click do botão calendario
bHorario.addEventListener('click', clickHorario) // evento de click do botão horario

/* 
    Essa terceira parte do código é a parte que terá as funções do programa:
*/

// função executada ao inicalizar a pagina:
function initialize(){
    ativaSiga() // chama a função que ativa o siga.
}

// função que ativa o siga:
function ativaSiga(){
    bSiga.style.cssText = 'color: white' // aqui muda a cor do texto do botão do siga.
    // essa parte aqui é a que coloca o site do Siga no frame:
    var newSrc = "https://siga.cps.sp.gov.br/ALUNO/login.aspx" // variavel com site do SIGA.
    tela.src = newSrc; // aqui coloca a variavel acima como o source do frame.
}

// função que desativa o siga:
function desativaSiga(){
    bSiga.style.cssText = 'color: black' // aqui muda a cor do texto do botão do siga.
}

// função que ativa o calendario:
function ativaCalendario(){
    bCalendario.style.cssText = 'color: white' // aqui muda a cor do texto do botão do calendario.
    // essa parte aqui é a que coloca PDF do calendario no frame:
    var newSrc = "../PDFs/calendario.pdf" // variavel com caminho do PDF do calendario.
    tela.src = newSrc; // aqui coloca a variavel acima como o source do frame.
}

// função que desativa o calendario:
function desativaCalendario(){
    bCalendario.style.cssText = 'color: black' // aqui muda a cor do texto do botão do calendario.
}

// função que ativa o horario:
function ativaHorario(){
    bHorario.style.cssText = 'color: white' // aqui muda a cor do texto do botão do horario.
    // essa parte aqui é a que coloca PDF do horario no frame:
    var newSrc = "../PDFs/horario.pdf" // variavel com caminho do PDF do horario.
    tela.src = newSrc; // aqui coloca a variavel acima como o source do frame.
}

// função que desativa o calendario:
function desativaHorario(){
    bHorario.style.cssText = 'color: black' // aqui muda a cor do texto do botão do horario.
}

// função de clique do botão siga:
function clickSiga(){
    ativaSiga() // chama a função que ativa o siga
    desativaCalendario() // chama a função que desativa o calendario
    desativaHorario() // chama a função que desativa o horario
}

// função de clique do botão calendario:
function clickCalendario(){
    ativaCalendario() // chama a função que ativa o calendario
    desativaHorario() // chama a função que desativa o horario
    desativaSiga() // chama a função que desativa o siga
}

// função de clique do botão horario:
function clickHorario(){
    ativaHorario() // chama a função que ativa o horario
    desativaCalendario() // chama a função que desativa o calendario
    desativaSiga() // chama a função que desativa o siga
}
