from algoritmos import FIFO, LRU, MRU
from config import SEQUENCIAS_TESTE

class GerenciadorTestes:
    def __init__(self, num_quadros=8):
        self.num_quadros = num_quadros
        self.algoritmos = {
            'fifo': FIFO(num_quadros),
            'lru': LRU(num_quadros),
            'mru': MRU(num_quadros)
        }
    
    def obter_sequencias_teste(self):
        return SEQUENCIAS_TESTE
    
    def executar_teste(self, teste_id, sequencia, pagina_procurada):
        resultados = {}
        
        for nome_algoritmo, algoritmo in self.algoritmos.items():
            memoria, faltas, historico = algoritmo.executar(sequencia)
            
            if pagina_procurada in memoria:
                quadro = memoria.index(pagina_procurada) + 1
            else:
                quadro = "Nao encontrada"
            
            resultados[nome_algoritmo] = {
                'memoria': memoria,
                'faltas': faltas,
                'quadro': quadro,
                'historico': historico
            }
        
        return resultados
    
    def executar_todos_testes(self):
        sequencias = self.obter_sequencias_teste()
        resultados_gerais = {}
        
        for teste_id, dados in sequencias.items():
            print(f"\nEXECUTANDO TESTE {teste_id.upper()}")
            print(f"Sequencia: {dados['sequencia']}")
            print(f"Pagina procurada: {dados['pagina_procurada']}")
            
            resultados_teste = self.executar_teste(
                teste_id, 
                dados['sequencia'], 
                dados['pagina_procurada']
            )
            
            resultados_gerais[teste_id] = {
                'resultados': resultados_teste,
                'pagina_procurada': dados['pagina_procurada']
            }
            
            self.mostrar_resultados_teste(teste_id, resultados_teste, dados['pagina_procurada'])
        
        return resultados_gerais
    
    def mostrar_resultados_teste(self, teste_id, resultados, pagina_procurada):
        print(f"\nRESULTADOS TESTE {teste_id.upper()} - Pagina {pagina_procurada}:")
        print("-" * 50)
        
        for algoritmo, dados in resultados.items():
            print(f"{algoritmo.upper():<6} | Memoria: {dados['memoria']} | Faltas: {dados['faltas']:2d} | Quadro: {dados['quadro']}")