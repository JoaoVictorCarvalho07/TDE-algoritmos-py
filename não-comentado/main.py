from testador import GerenciadorTestes
from analisador import AnalisadorResultados

def main():
    print("SISTEMA DE ANALISE DE ALGORITMOS DE SUBSTITUICAO DE PAGINAS")
    print("FIFO | LRU | MRU")
    print("=" * 65)
    
    num_quadros = 8
    
    gerenciador = GerenciadorTestes(num_quadros)
    analisador = AnalisadorResultados()
    
    resultados_gerais = gerenciador.executar_todos_testes()
    analisador.analisar_desempenho(resultados_gerais)
    
    analisador.mostrar_respostas_finais(resultados_gerais)

if __name__ == "__main__":
    main()