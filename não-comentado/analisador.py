class AnalisadorResultados:
    def __init__(self):
        self.melhor_algoritmo = None
    
    def analisar_desempenho(self, resultados_gerais):
        print("\n")
        print("ANALISE DE DESEMPENHO DAS POLITICAS DE SUBSTITUICAO\n")
        
        total_faltas = {'fifo': 0, 'lru': 0, 'mru': 0}
        
        for teste_id, dados_teste in resultados_gerais.items():
            print(f"\nTeste {teste_id.upper()}:")
            
            for algoritmo, resultado in dados_teste['resultados'].items():
                faltas = resultado['faltas']
                total_faltas[algoritmo] += faltas
                print(f"  {algoritmo.upper()}: {faltas} faltas de pagina")
        
        print(f"\nTOTAL DE FALTAS EM TODOS OS TESTES:")
        print("-" * 40)
        
        for algoritmo, total in total_faltas.items():
            print(f"  {algoritmo.upper()}: {total} faltas")
        
        self.melhor_algoritmo = min(total_faltas, key=total_faltas.get)
        
        print(f"\nMELHOR POLITICA GERAL: {self.melhor_algoritmo.upper()}")
        print(f"Total de faltas: {total_faltas[self.melhor_algoritmo]}")
        
        return self.melhor_algoritmo, total_faltas
    
    def mostrar_respostas_finais(self, resultados_gerais):
        print("\n" + "="*50)
        print("RESPOSTAS FINAIS DOS TESTES")
        print("="*50)
        
        for teste_id, dados_teste in resultados_gerais.items():
            pagina = dados_teste['pagina_procurada']
            print(f"\nTESTE {teste_id.upper()} - Qual quadro possui a pagina {pagina}?")
            
            for algoritmo in ['fifo', 'lru', 'mru']:
                quadro = dados_teste['resultados'][algoritmo]['quadro']
                print(f"  {algoritmo.upper()}: Quadro {quadro}")
        
        print(f"\nMelhor politica de substituicao: {self.melhor_algoritmo.upper()}")
    