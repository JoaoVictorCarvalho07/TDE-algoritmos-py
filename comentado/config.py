# Configurações dos testes para análise dos algoritmos de substituição de páginas
# Cada teste contém uma sequência de páginas e uma página específica a ser procurada

SEQUENCIAS_TESTE = {
    # Teste A: Sequência com padrão de acesso variado
    'a': {
        'sequencia': [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7],
        'pagina_procurada': 7,  # Página que queremos encontrar no final
        'descricao': 'Teste A - Pagina 7'
    },
    
    # Teste B: Sequência com acesso a páginas mais dispersas
    'b': {
        'sequencia': [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11],
        'pagina_procurada': 11,  # Página que queremos encontrar no final
        'descricao': 'Teste B - Pagina 11'
    },
    
    # Teste C: Sequência com padrão de localidade temporal
    'c': {
        'sequencia': [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11],
        'pagina_procurada': 11,  # Página que queremos encontrar no final
        'descricao': 'Teste C - Pagina 11'
    }
}