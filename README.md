# Machine Learning

## Introdução

Projeto desenvolvido se trata de um estudo de machine learning, o qual tem objetivo de treinar através de uma base de imagens e identificar dois personagens utilizando de técnicas passadas em aula.

## Stack Utilizada :shipit:
- Electron
- React Js
- Python

**Personagens Selecionados para estudo:Os Simpsons - Milhouse e Apu**

Funcionamento de interface desenvolvido utilizando Electron Js com conteúdo renderizado em React Js c/ (Typescript);
Funcionamento de processamento de imagens utilizando Python e algumas bibliotecas externas;

## Executável

Na pasta **final_build** está a versão final do build, o qual é possivel executar o **machine-learning.exe**
- Caso não queira executar o treinamento: 
*na pasta **preprocessado** é possivel encontrar os arquivos de treinamento **data.h5 e labels.h5** já processados.
basta copiar e colar no caminho **"raiz/final_build/resources/python/output/"**, e executar o **machine-learning.exe***

**Obs: Treinamento pode levar horas para ser concluído corretamente.**

## Características do Treino

Arquivo presente na raiz do projeto **caracteristicas.arff** se trata dos dados de treino já extraidos para um padrão de arquivo, pronto para leitura através do programa Weka.

## Instalação

Windows & Linux

```sh
cd electron
npm install --save
npm install -g
```

## Start

Para execução em ambiente de desenvolvimento utilize os comandos abaixo.
**Comando deve ser executado dentro da pasta "electron".**
```sh
npm start
```


## Build

É possivel gerar uma versão executavel, para isso utilize dos comandos abaixo.
**Comando deve ser executado dentro da pasta "electron".**
```sh
npm run build
```

## Release History

* 1.0.0
    * Primeira versão modelo funcional com interface
* 0.1.0
    * Primeira versão modelo funcional de analise em python (sem interface)
* 0.0.1
    * Estudo das técnicas

## Credits

Phillipe Vieira - Developer

Clavison Zapelini - Teacher
