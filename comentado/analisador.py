class AnalisadorResultados:
    """
    Classe responsável por analisar e apresentar os resultados dos testes
    dos algoritmos de substituição de páginas
    """
    
    def __init__(self):
        """Inicializa o analisador sem um algoritmo preferido ainda"""
        self.melhor_algoritmo = None
    
    def analisar_desempenho(self, resultados_gerais):
        """
        Analisa o desempenho de todos os algoritmos e determina qual é o melhor
        
        Args:
            resultados_gerais: Dicionário com todos os resultados dos testes
            
        Returns:
            melhor_algoritmo: Nome do algoritmo com melhor desempenho
            total_faltas: Dicionário com total de faltas por algoritmo
        """
        print("\n")
        print("ANALISE DE DESEMPENHO DAS POLITICAS DE SUBSTITUICAO\n")
        
        # Inicializa contadores para somar as faltas de todos os testes
        total_faltas = {'fifo': 0, 'lru': 0, 'mru': 0}
        
        # Analisa cada teste individualmente
        for teste_id, dados_teste in resultados_gerais.items():
            print(f"\nTeste {teste_id.upper()}:")
            
            # Mostra as faltas de cada algoritmo para este teste
            for algoritmo, resultado in dados_teste['resultados'].items():
                faltas = resultado['faltas']
                total_faltas[algoritmo] += faltas  # Soma ao total geral
                print(f"  {algoritmo.upper()}: {faltas} faltas de pagina")
        
        # Exibe o resumo geral de faltas
        print(f"\nTOTAL DE FALTAS EM TODOS OS TESTES:")
        print("-" * 40)
        
        for algoritmo, total in total_faltas.items():
            print(f"  {algoritmo.upper()}: {total} faltas")
        
        # Determina qual algoritmo teve o menor número de faltas
        self.melhor_algoritmo = min(total_faltas, key=total_faltas.get)
        
        print(f"\nMELHOR POLITICA GERAL: {self.melhor_algoritmo.upper()}")
        print(f"Total de faltas: {total_faltas[self.melhor_algoritmo]}")
        
        return self.melhor_algoritmo, total_faltas
    
    def mostrar_respostas_finais(self, resultados_gerais):
        """
        Mostra as respostas finais para cada teste, indicando em qual quadro
        cada algoritmo encontrou a página procurada
        
        Args:
            resultados_gerais: Dicionário com todos os resultados dos testes
        """
        print("\n" + "="*50)
        print("RESPOSTAS FINAIS DOS TESTES")
        print("="*50)
        
        # Para cada teste, mostra em qual quadro cada algoritmo encontrou a página
        for teste_id, dados_teste in resultados_gerais.items():
            pagina = dados_teste['pagina_procurada']
            print(f"\nTESTE {teste_id.upper()} - Qual quadro possui a pagina {pagina}?")
            
            # Mostra o resultado de cada algoritmo para esta página
            for algoritmo in ['fifo', 'lru', 'mru']:
                quadro = dados_teste['resultados'][algoritmo]['quadro']
                print(f"  {algoritmo.upper()}: Quadro {quadro}")
        
        # Mostra qual foi o melhor algoritmo geral
        print(f"\nMelhor politica de substituicao: {self.melhor_algoritmo.upper()}")
    