import psutil
import time
import os

try:
    # Primeira leitura da rede
    net_antes = psutil.net_io_counters()

    while True:
        # Limpa a tela (Windows/Linux)
        os.system("cls" if os.name == "nt" else "clear")

        print("===== PAINEL DE MONITORAMENTO =====\n")

        # ==========================
        # CPU
        # ==========================
        cpu = psutil.cpu_percent(interval=1)
        print(f"CPU Total: {cpu}%")

        # ==========================
        # RAM
        # ==========================
        ram = psutil.virtual_memory()
        ram_usada_mb = ram.used / (1024 ** 2)

        print(f"RAM: {ram.percent}% ({ram_usada_mb:.2f} MB usados)")

        # ==========================
        # DISCO (partição principal)
        # ==========================
        disco = psutil.disk_usage('/')
        livre_gb = disco.free / (1024 ** 3)

        print(f"Disco Livre: {livre_gb:.2f} GB")

        # ==========================
        # REDE
        # ==========================
        net_depois = psutil.net_io_counters()

        upload = net_depois.bytes_sent - net_antes.bytes_sent
        download = net_depois.bytes_recv - net_antes.bytes_recv

        net_antes = net_depois

        print(f"Upload: {upload/1024:.2f} KB/s")
        print(f"Download: {download/1024:.2f} KB/s")

        # Espera mais 1 segundo (já teve 1s da CPU)
        time.sleep(1)

except KeyboardInterrupt:
    print("\nPainel encerrado.")