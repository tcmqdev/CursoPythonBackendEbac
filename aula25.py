# Dado um endereço IP válido (IPv4), retorne uma versão ajustada desse endereço IP. 
# Um endereço IP ajustado substitui cada ponto "." por "[.]" para evitar que o endereço IP seja interpretado como um link.
# Exemplo: 1.1.1.1 ==> 1[.]1[.]1[.]1

# 1. Receber  a string do endereço IP como entrada.

endereco_ip = input("Digite o endereço IP: ")

# 2. Substituir cada ponto "." por "[.]".

novo_endereco_ip = ""

for i in endereco_ip:
    if i == ".":
        novo_endereco_ip += "[.]"
    else:
        novo_endereco_ip += i

print("Endereço IP ajustado:", novo_endereco_ip)

# endereco_ip_ajustado = endereco_ip.replace(".", "[.]")
# print(endereco_ip_ajustado)
