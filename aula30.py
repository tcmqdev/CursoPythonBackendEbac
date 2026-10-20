# Dada uma string s consistindo apenas dos caracteres 'a' e 'b', retorne verdadeiro se cada 'a' aparecer antes de cada 'b' na string. Caso contrário, retorne falso.

minha_string = "abababab"

if 'ba' not in minha_string:
    print("Verdadeiro: cada 'a' aparece antes de cada 'b'")
else:
    print("Falso: há 'b' antes de 'a'")


#def verificar_ordem(s):
    # Encontra a última posição do caractere 'a'
#    ultima_a = s.rfind('a')
    # Encontra a primeira posição do caractere 'b'
#    primeira_b = s.find('b')
    
    # Se não houver 'a' ou não houver 'b', retorna verdadeiro
#    if ultima_a == -1 or primeira_b == -1:
#        return True
    
    # Se a última 'a' estiver antes da primeira 'b', retorna verdadeiro
#    if ultima_a < primeira_b:
#        return True
#    else:
#        return False
    
