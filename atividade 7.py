import psutil
import time
from datetime import datetime

try:
    while True:
        
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        
        cpu = psutil.cpu_percent(interval=1)
        
    
        linha = f"{agora} - CPU: {cpu}%\n"
        
        # Salva no arquivo
        with open("cpu_log.txt", "a") as arquivo:
            arquivo.write(linha)
        
        
        print(linha.strip())
        
        
        time.sleep(4)

except KeyboardInterrupt:
    print("\nLogger encerrado.")