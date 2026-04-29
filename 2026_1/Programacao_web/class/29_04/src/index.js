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

// Reinicia a partida
reset = function () {
    window.location.reload();
}

// Seta