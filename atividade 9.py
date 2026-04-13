import psutil

# ==========================
# DISPOSITIVOS DE E/S (COMENTÁRIO TEÓRICO)
# ==========================
# Dispositivos de Entrada:
# - Teclado: permite digitar informações
# - Mouse: interação com o sistema
# - Scanner: digitaliza documentos
# - Microfone: entrada de áudio
#
# Dispositivos de Saída:
# - Monitor: exibe imagens
# - Impressora: imprime documentos
# - Alto-falantes: saída de som
#
# Dispositivos de Entrada e Saída (E/S):
# - HD / SSD: leitura e escrita de dados
# - Pendrive: armazenamento portátil
# - Placa de rede: envia e recebe dados
#
# OBS: O Python (psutil) consegue detectar principalmente
# dispositivos de armazenamento, não todos os periféricos.

# ==========================
# LISTAR PARTIÇÕES
# ==========================
particoes = psutil.disk_partitions()

print("===== DISPOSITIVOS DE ARMAZENAMENTO =====\n")

for i, p in enumerate(particoes):
    print(f"[{i}] Dispositivo: {p.device} | Ponto de montagem: {p.mountpoint}")

# ==========================
# ESCOLHER PARTIÇÃO
# ==========================
try:
    escolha = int(input("\nEscolha o número da partição: "))
    part = particoes[escolha]

    print("\n===== INFORMAÇÕES DA PARTIÇÃO =====")
    print(f"Dispositivo: {part.device}")
    print(f"Ponto de montagem: {part.mountpoint}")
    print(f"Sistema de arquivos: {part.fstype}")

    uso = psutil.disk_usage(part.mountpoint)

    print(f"Total: {uso.total / (1024**3):.2f} GB")
    print(f"Usado: {uso.used / (1024**3):.2f} GB")
    print(f"Livre: {uso.free / (1024**3):.2f} GB")
    print(f"Uso (%): {uso.percent}%")

except (IndexError, ValueError):
    print("Opção inválida.")