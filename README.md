# Sistema de Análise de Algoritmos de Substituição de Páginas

Este projeto implementa e compara três algoritmos clássicos de substituição de páginas em sistemas operacionais: **FIFO**, **LRU** e **MRU**. O sistema simula o gerenciamento de memória virtual e analisa o desempenho de cada algoritmo através de diferentes sequências de acesso.

## 🎯 Objetivo

Demonstrar e comparar o comportamento dos algoritmos de substituição de páginas, analisando quantas faltas de página cada um produz em diferentes cenários de acesso à memória.

## Membros
- Edmund Soares de Sousa
- João Victor Carvalho de Freitas
- Matheus Henrique Heinzen
- Vinicius Lima Teider

## Vídeo Explicativo
[![Watch the video](thumbnail)](linkdovideo)

## 📋 Algoritmos Implementados

### FIFO (First In, First Out)
- **Conceito**: Remove sempre a página que está na memória há mais tempo
- **Vantagem**: Simples de implementar
- **Desvantagem**: Pode remover páginas frequentemente usadas

### LRU (Least Recently Used)
- **Conceito**: Remove sempre a página que foi acessada há mais tempo
- **Vantagem**: Geralmente produz bom desempenho
- **Desvantagem**: Requer rastreamento de tempo de acesso

### MRU (Most Recently Used)
- **Conceito**: Remove sempre a página que foi acessada mais recentemente
- **Vantagem**: Pode ser eficaz em alguns padrões de acesso
- **Desvantagem**: Contraintuitivo, pode ter desempenho ruim

## 🗂️ Estrutura do Projeto

```
TDE-algoritmos-py/
├── comentado/              # Versão com comentários explicativos
│   ├── main.py            # Ponto de entrada do programa
│   ├── algoritmos.py      # Implementações dos algoritmos
│   ├── testador.py        # Gerenciador de testes
│   ├── analisador.py      # Análise de resultados
│   └── config.py          # Configurações dos testes
├── não-comentado/         # Versão original sem comentários
└── README.md              # Este arquivo
```

## 📊 Testes Realizados

O sistema executa três testes com sequências diferentes:

- **Teste A**: Sequência com padrão de acesso variado
- **Teste B**: Sequência com acesso a páginas mais dispersas  
- **Teste C**: Sequência com padrão de localidade temporal

Cada teste procura uma página específica no final da execução e verifica em qual quadro ela está armazenada.

## 📈 Saída do Programa

O programa exibe:

1. **Resultados por teste**: Estado final da memória, número de faltas e quadro da página procurada
2. **Análise de desempenho**: Comparação das faltas de página entre algoritmos
3. **Respostas finais**: Quadro onde cada algoritmo encontrou a página procurada
4. **Melhor algoritmo**: Qual política teve o menor número total de faltas

## 🔧 Configurações

- **Número de quadros**: 8 (configurável no `main.py`)
- **Sequências de teste**: Definidas em `config.py`

## 💡 Conceitos Demonstrados

- **Falta de página**: Quando uma página não está na memória física
- **Substituição de páginas**: Estratégia para liberar espaço na memória
- **Localidade temporal**: Tendência de acessar páginas usadas recentemente
- **Simulação de memória virtual**: Como o SO gerencia a memória


## 📝 Exemplo de Saída

```
SISTEMA DE ANALISE DE ALGORITMOS DE SUBSTITUICAO DE PAGINAS
FIFO | LRU | MRU
=================================================================

EXECUTANDO TESTE A
Sequencia: [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
Pagina procurada: 7

RESULTADOS TESTE A - Pagina 7:
--------------------------------------------------
FIFO   | Memoria: [8, 3, 16, 25, 7, 35, 45, 22] | Faltas: 13 | Quadro: 5
LRU    | Memoria: [16, 25, 7, 35, 45, 22, 8, 3] | Faltas: 12 | Quadro: 3
MRU    | Memoria: [4, 3, 16, 25, 7, 35, 45, 22] | Faltas: 14 | Quadro: 5

ANALISE DE DESEMPENHO DAS POLITICAS DE SUBSTITUICAO

Teste A:
  FIFO: 13 faltas de pagina
  LRU: 12 faltas de pagina
  MRU: 14 faltas de pagina

TOTAL DE FALTAS EM TODOS OS TESTES:
----------------------------------------
  FIFO: 42 faltas
  LRU: 38 faltas
  MRU: 44 faltas

MELHOR POLITICA GERAL: LRU
Total de faltas: 38

RESPOSTAS FINAIS DOS TESTES
==================================================

TESTE A - Qual quadro possui a pagina 7?
  FIFO: Quadro 5
  LRU: Quadro 3
  MRU: Quadro 5

Melhor politica de substituicao: LRU
```

## 📄 Licença

Este projeto é para fins educacionais e de estudo.
