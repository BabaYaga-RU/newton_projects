// Deixar a div do jogo escondida no momento que a página é carregada
window.onload = function (){
    document.getElementById('game').style.visibility = 'hidden';
}

// Cria um objeto do jogador
function Jogador(nome, forma){
    this.nome = nome;
    this.forma = forma;
}

// Variaveis que armazena os dados dos jogadores
var jogador1, jogador2;

// Jogador da rodada
var jogadorAtual;
var forms = ['X', 'O'];

/*
    0 1 2
    3 4 5
    6 7 8
*/
var tabuleiro = new Array(9);

// Função que inicia o jogo
initGame = function (){
    var nomeJogador1 = document.getElementById('jogador1').Value;
    var nomeJogador2 = document.getElementById('jogador2').Value;
    jogador1 = new Jogador(nomeJogador1, 0) //X
    jogador2 = new Jogador(nomeJogador2, 0) //O

    jogadorAtual = jogador1;
    setLabelJogadorAtual();

    // Apos definição de jogadores, exibe a div e inicia o jogo
    document.getElementById('game').style.visibility = 'visible';
}

// Reinicia a pagina
reset = function () {
    window.location.reload();
}

// Seta o nome do jogador da rodada na pagina HTML
setLabelJogadorAtual = function () {
    document.getElementById('jogadorAtual').innerHTML = "Jogador atual: " + jogadorAtual.nome;
}

/*
Verifica se o tabuleiro esta completamente preenchido, 
se estiver, significa que ninguem venceu a rodada
*/
tabuleiroIsFilled = function () {
    var preenchido = 0;
    for (var i = 0; i < tabuleiro.length; i++){
        if (tabuleiro[i] != undefined){
            preenchido ++;
        }
    }
    return preenchido == tabuleiro.length;
}

/*
Verifica a existencia de ocorrencias de um mesmo elemento (X ou O) nas linhas do tabuleiro,
procurando um vencedor
*/
allElements

/*
Preenche a célula da tabela HTML escolhida pelo usuario ao clicar, 
além de cuidar do jogador atual da rodada e chamar as funções de verificações de algum ganhador
*/
setOnCeil = function (cel, pos) {
    if (tabuleiro[pos] == undefined) {
        cel.innerHTML = formas[jogadorAtual.forma];
        tabuleiro[pos] = formas[jogadorAtual.forma];

        // Define o jogador da rodada
        (jogadorAtual.forma == 0) ? jogadorAtual = jogador2 : jogadorAtual = jogador1;
        setLabelJogadorAtual();
    } else alert('Ops. ')
}