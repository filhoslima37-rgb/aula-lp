import psutil
import time


net_io_antes = psutil.net_io_counters()

while True:
    
    time.sleep(1)
    
    
    net_io_depois = psutil.net_io_counters()
    
    
    bytes_enviados = net_io_depois.bytes_sent - net_io_antes.bytes_sent
    bytes_recebidos = net_io_depois.bytes_recv - net_io_antes.bytes_recv
    
    
    net_io_antes = net_io_depois
    
    
    print(f"Upload: {bytes_enviados} B/s | Download: {bytes_recebidos} B/s")