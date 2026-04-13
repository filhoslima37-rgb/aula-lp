import psutil
import platform
import subprocess

def pegar_numero_serie():
    try:
        # Funciona no Windows
        comando = "wmic cpu get ProcessorId"
        resultado = subprocess.check_output(comando, shell=True).decode()
        return resultado.split("\n")[1].strip()
    except:
        return "Não disponível"

# Nome/modelo da CPU
nome_cpu = platform.processor()

# Núcleos
nucleos_fisicos = psutil.cpu_count(logical=False)
nucleos_logicos = psutil.cpu_count(logical=True)

# Frequência
freq = psutil.cpu_freq()

# Número de série
serial = pegar_numero_serie()

# Exibição
print("===== INFORMAÇÕES DA CPU =====")
print(f"Modelo: {nome_cpu}")
print(f"Núcleos físicos: {nucleos_fisicos}")
print(f"Núcleos lógicos: {nucleos_logicos}")

if freq:
    print(f"Frequência atual: {freq.current:.2f} MHz")
    print(f"Frequência máxima: {freq.max:.2f} MHz")

print(f"Número de série: {serial}")