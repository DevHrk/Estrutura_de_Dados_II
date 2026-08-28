Estrutura de Dados I — Arrays, Matrizes e Structs
1. Arrays (Vetores)

Um array é uma estrutura que armazena vários elementos do mesmo tipo, utilizando posições consecutivas de memória.

int numeros[5] = {10, 20, 30, 40, 50};

Características
Tamanho geralmente definido na criação.
Elementos acessados por índice.
Primeiro índice: 0.
Acesso direto: O(1).
printf("%d", numeros[2]); // 30

Percorrendo um array
for (int i = 0; i < 5; i++) {
    printf("%d ", numeros[i]);
}

2. Matrizes

Uma matriz é um array multidimensional. A mais comum é a matriz bidimensional, organizada em linhas e colunas.

int matriz[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

Acesso
matriz[1][2]; // 6


A primeira posição representa a linha e a segunda, a coluna:

matriz[linha][coluna]

Percorrendo uma matriz
for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        printf("%d ", matriz[i][j]);
    }
}

i → controla as linhas.
j → controla as colunas.
Percorrer uma matriz n × m custa O(n × m).
3. Structs

Uma struct permite criar um tipo de dado personalizado agrupando diferentes tipos de informações.

struct Aluno {
    char nome[50];
    int idade;
    float nota;
};

Criando uma variável
struct Aluno aluno1;

Acessando os campos
aluno1.idade = 20;
aluno1.nota = 8.5;


O operador . permite acessar os membros da estrutura.

4. Array de Structs

É possível combinar arrays e structs para armazenar vários registros.

struct Aluno alunos[3];


Cada posição representa um aluno:

alunos[0].idade = 20;
alunos[1].idade = 22;
alunos[2].idade = 19;


Isso é muito utilizado para representar cadastros, registros e conjuntos de objetos.

5. Struct dentro de Struct

Uma struct pode possuir outra struct como membro.

struct Endereco {
    char cidade[30];
    int numero;
};

struct Pessoa {
    char nome[50];
    struct Endereco endereco;
};


Acesso:

pessoa.endereco.numero;

6. Ponteiros e Structs

Quando trabalhamos com um ponteiro para uma struct, usamos -> para acessar seus membros.

struct Aluno *p;

p = &aluno1;

p->idade = 21;


É equivalente a:

(*p).idade = 21;

📌 Regra importante
. → variável normal de struct.
-> → ponteiro para struct.

🧠 Resumo Final
Estrutura	Característica
Array	Vários elementos do mesmo tipo
Matriz	Array com múltiplas dimensões
Struct	Agrupa dados de diferentes tipos
Array de Structs	Armazena vários registros
Ponteiro para Struct	Permite acessar uma struct através de um endereço

Ideia principal: arrays organizam dados do mesmo tipo, matrizes organizam esses dados em dimensões, e structs permitem representar dados relacionados de tipos diferentes.
