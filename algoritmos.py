class FIFO:
    def __init__(self, quadros):
        self.num_quadros = quadros
        self.nome = "FIFO"
    
    def executar(self, sequencia):
        memoria = []
        ordem_entrada = []
        faltas_pagina = 0
        historico = []
        
        for pagina in sequencia:
            if pagina not in memoria:
                faltas_pagina += 1
                if len(memoria) < self.num_quadros:
                    memoria.append(pagina)
                    ordem_entrada.append(pagina)
                else:
                    pagina_remover = ordem_entrada[0]
                    idx = memoria.index(pagina_remover)
                    memoria[idx] = pagina
                    ordem_entrada.remove(pagina_remover)
                    ordem_entrada.append(pagina)
            historico.append(memoria.copy())
        
        return memoria, faltas_pagina, historico

class LRU:
    def __init__(self, quadros):
        self.num_quadros = quadros
        self.nome = "LRU"
    
    def executar(self, sequencia):
        memoria = []
        tempo_acesso = {}
        faltas_pagina = 0
        historico = []
        
        for tempo, pagina in enumerate(sequencia):
            tempo_acesso[pagina] = tempo
            
            if pagina not in memoria:
                faltas_pagina += 1
                if len(memoria) < self.num_quadros:
                    memoria.append(pagina)
                else:
                    pagina_lru = min(memoria, key=lambda p: tempo_acesso[p])
                    idx = memoria.index(pagina_lru)
                    memoria[idx] = pagina
            
            historico.append(memoria.copy())
        
        return memoria, faltas_pagina, historico

class MRU:
    def __init__(self, quadros):
        self.num_quadros = quadros
        self.nome = "MRU"
    
    def executar(self, sequencia):
        memoria = []
        tempo_acesso = {}
        faltas_pagina = 0
        historico = []
        
        for tempo, pagina in enumerate(sequencia):
            tempo_acesso[pagina] = tempo
            
            if pagina not in memoria:
                faltas_pagina += 1
                if len(memoria) < self.num_quadros:
                    memoria.append(pagina)
                else:
                    pagina_mru = max(memoria, key=lambda p: tempo_acesso[p])
                    idx = memoria.index(pagina_mru)
                    memoria[idx] = pagina
            
            historico.append(memoria.copy())
        
        return memoria, faltas_pagina, historico
