# Importações necessárias para o funcionamento do sistema
from testador import GerenciadorTestes
from analisador import AnalisadorResultados

def main():
    """
    Função principal que coordena todo o processo de análise dos algoritmos.
    Este programa testa e compara três algoritmos de substituição de páginas:
    - FIFO (First In, First Out)
    - LRU (Least Recently Used) 
    - MRU (Most Recently Used)
    """
    # Exibe o cabeçalho do sistema
    print("SISTEMA DE ANALISE DE ALGORITMOS DE SUBSTITUICAO DE PAGINAS")
    print("FIFO | LRU | MRU")
    print("=" * 65)
    
    # Define o número de quadros de memória disponíveis para os testes
    num_quadros = 8
    
    # Cria o gerenciador de testes e o analisador de resultados
    gerenciador = GerenciadorTestes(num_quadros)
    analisador = AnalisadorResultados()
    
    # Executa todos os testes com os diferentes algoritmos
    resultados_gerais = gerenciador.executar_todos_testes()
    
    # Analisa o desempenho comparativo dos algoritmos
    analisador.analisar_desempenho(resultados_gerais)
    
    # Mostra as respostas finais de cada teste
    analisador.mostrar_respostas_finais(resultados_gerais)

# Garante que o programa só execute quando chamado diretamente
if __name__ == "__main__":
    main()