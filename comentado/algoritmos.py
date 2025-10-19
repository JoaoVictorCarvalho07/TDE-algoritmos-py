class FIFO:
    """
    Algoritmo FIFO (First In, First Out) - Primeiro a Entrar, Primeiro a Sair
    Remove sempre a página que está na memória há mais tempo
    """
    
    def __init__(self, quadros):
        """Inicializa o algoritmo com o número de quadros disponíveis"""
        self.num_quadros = quadros
        self.nome = "FIFO"
    
    def executar(self, sequencia):
        """
        Executa o algoritmo FIFO para uma sequência de páginas
        
        Args:
            sequencia: Lista com as páginas a serem acessadas
            
        Returns:
            memoria: Estado final da memória
            faltas_pagina: Número de faltas de página ocorridas
            historico: Histórico de todos os estados da memória
        """
        memoria = []  # Simula os quadros de memória física
        ordem_entrada = []  # Mantém a ordem de chegada das páginas
        faltas_pagina = 0  # Contador de faltas de página
        historico = []  # Registra cada estado da memória
        
        for pagina in sequencia:
            # Verifica se a página já está na memória
            if pagina not in memoria:
                faltas_pagina += 1  # Incrementa contador de faltas
                
                # Se ainda há espaço na memória, adiciona a página
                if len(memoria) < self.num_quadros:
                    memoria.append(pagina)
                    ordem_entrada.append(pagina)
                else:
                    # Remove a página que chegou primeiro (FIFO)
                    pagina_remover = ordem_entrada[0]
                    idx = memoria.index(pagina_remover)
                    memoria[idx] = pagina
                    
                    # Atualiza a ordem de entrada
                    ordem_entrada.remove(pagina_remover)
                    ordem_entrada.append(pagina)
            
            # Registra o estado atual da memória
            historico.append(memoria.copy())
        
        return memoria, faltas_pagina, historico

class LRU:
    """
    Algoritmo LRU (Least Recently Used) - Menos Recentemente Usado
    Remove sempre a página que foi acessada há mais tempo
    """
    
    def __init__(self, quadros):
        """Inicializa o algoritmo com o número de quadros disponíveis"""
        self.num_quadros = quadros
        self.nome = "LRU"
    
    def executar(self, sequencia):
        """
        Executa o algoritmo LRU para uma sequência de páginas
        
        Args:
            sequencia: Lista com as páginas a serem acessadas
            
        Returns:
            memoria: Estado final da memória
            faltas_pagina: Número de faltas de página ocorridas
            historico: Histórico de todos os estados da memória
        """
        memoria = []  # Simula os quadros de memória física
        tempo_acesso = {}  # Registra quando cada página foi acessada pela última vez
        faltas_pagina = 0  # Contador de faltas de página
        historico = []  # Registra cada estado da memória
        
        for tempo, pagina in enumerate(sequencia):
            # Atualiza o tempo do último acesso para esta página
            tempo_acesso[pagina] = tempo
            
            # Verifica se a página já está na memória
            if pagina not in memoria:
                faltas_pagina += 1  # Incrementa contador de faltas
                
                # Se ainda há espaço na memória, adiciona a página
                if len(memoria) < self.num_quadros:
                    memoria.append(pagina)
                else:
                    # Encontra a página que foi acessada há mais tempo (LRU)
                    pagina_lru = min(memoria, key=lambda p: tempo_acesso[p])
                    idx = memoria.index(pagina_lru)
                    memoria[idx] = pagina
            
            # Registra o estado atual da memória
            historico.append(memoria.copy())
        
        return memoria, faltas_pagina, historico

class MRU:
    """
    Algoritmo MRU (Most Recently Used) - Mais Recentemente Usado
    Remove sempre a página que foi acessada mais recentemente
    """
    
    def __init__(self, quadros):
        """Inicializa o algoritmo com o número de quadros disponíveis"""
        self.num_quadros = quadros
        self.nome = "MRU"
    
    def executar(self, sequencia):
        """
        Executa o algoritmo MRU para uma sequência de páginas
        
        Args:
            sequencia: Lista com as páginas a serem acessadas
            
        Returns:
            memoria: Estado final da memória
            faltas_pagina: Número de faltas de página ocorridas
            historico: Histórico de todos os estados da memória
        """
        memoria = []  # Simula os quadros de memória física
        tempo_acesso = {}  # Registra quando cada página foi acessada pela última vez
        faltas_pagina = 0  # Contador de faltas de página
        historico = []  # Registra cada estado da memória
        
        for tempo, pagina in enumerate(sequencia):
            # Atualiza o tempo do último acesso para esta página
            tempo_acesso[pagina] = tempo
            
            # Verifica se a página já está na memória
            if pagina not in memoria:
                faltas_pagina += 1  # Incrementa contador de faltas
                
                # Se ainda há espaço na memória, adiciona a página
                if len(memoria) < self.num_quadros:
                    memoria.append(pagina)
                else:
                    # Encontra a página que foi acessada mais recentemente (MRU)
                    pagina_mru = max(memoria, key=lambda p: tempo_acesso[p])
                    idx = memoria.index(pagina_mru)
                    memoria[idx] = pagina
            
            # Registra o estado atual da memória
            historico.append(memoria.copy())
        
        return memoria, faltas_pagina, historico
