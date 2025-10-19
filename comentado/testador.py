# Importações necessárias para o gerenciamento dos testes
from algoritmos import FIFO, LRU, MRU
from config import SEQUENCIAS_TESTE

class GerenciadorTestes:
    """
    Classe responsável por gerenciar e executar todos os testes
    dos algoritmos de substituição de páginas
    """
    
    def __init__(self, num_quadros=8):
        """
        Inicializa o gerenciador de testes
        
        Args:
            num_quadros: Número de quadros de memória disponíveis (padrão: 8)
        """
        self.num_quadros = num_quadros
        
        # Cria instâncias de todos os algoritmos para teste
        self.algoritmos = {
            'fifo': FIFO(num_quadros),
            'lru': LRU(num_quadros),
            'mru': MRU(num_quadros)
        }
    
    def obter_sequencias_teste(self):
        """
        Retorna as sequências de teste configuradas
        
        Returns:
            SEQUENCIAS_TESTE: Dicionário com todas as sequências de teste
        """
        return SEQUENCIAS_TESTE
    
    def executar_teste(self, teste_id, sequencia, pagina_procurada):
        """
        Executa um teste específico com todos os algoritmos
        
        Args:
            teste_id: Identificador do teste (a, b, c)
            sequencia: Lista de páginas a serem acessadas
            pagina_procurada: Página que deve ser encontrada no final
            
        Returns:
            resultados: Dicionário com resultados de todos os algoritmos
        """
        resultados = {}
        
        # Executa cada algoritmo com a mesma sequência
        for nome_algoritmo, algoritmo in self.algoritmos.items():
            memoria, faltas, historico = algoritmo.executar(sequencia)
            
            # Verifica se a página procurada está na memória final
            if pagina_procurada in memoria:
                quadro = memoria.index(pagina_procurada) + 1  # +1 porque quadros começam em 1
            else:
                quadro = "Nao encontrada"
            
            # Armazena todos os resultados do algoritmo
            resultados[nome_algoritmo] = {
                'memoria': memoria,
                'faltas': faltas,
                'quadro': quadro,
                'historico': historico
            }
        
        return resultados
    
    def executar_todos_testes(self):
        """
        Executa todos os testes configurados com todos os algoritmos
        
        Returns:
            resultados_gerais: Dicionário com todos os resultados de todos os testes
        """
        sequencias = self.obter_sequencias_teste()
        resultados_gerais = {}
        
        # Executa cada teste configurado
        for teste_id, dados in sequencias.items():
            print(f"\nEXECUTANDO TESTE {teste_id.upper()}")
            print(f"Sequencia: {dados['sequencia']}")
            print(f"Pagina procurada: {dados['pagina_procurada']}")
            
            # Executa o teste com todos os algoritmos
            resultados_teste = self.executar_teste(
                teste_id, 
                dados['sequencia'], 
                dados['pagina_procurada']
            )
            
            # Armazena os resultados para análise posterior
            resultados_gerais[teste_id] = {
                'resultados': resultados_teste,
                'pagina_procurada': dados['pagina_procurada']
            }
            
            # Mostra os resultados deste teste
            self.mostrar_resultados_teste(teste_id, resultados_teste, dados['pagina_procurada'])
        
        return resultados_gerais
    
    def mostrar_resultados_teste(self, teste_id, resultados, pagina_procurada):
        """
        Exibe os resultados de um teste específico de forma organizada
        
        Args:
            teste_id: Identificador do teste
            resultados: Resultados de todos os algoritmos para este teste
            pagina_procurada: Página que estava sendo procurada
        """
        print(f"\nRESULTADOS TESTE {teste_id.upper()} - Pagina {pagina_procurada}:")
        print("-" * 50)
        
        # Mostra os resultados de cada algoritmo de forma tabular
        for algoritmo, dados in resultados.items():
            print(f"{algoritmo.upper():<6} | Memoria: {dados['memoria']} | Faltas: {dados['faltas']:2d} | Quadro: {dados['quadro']}")