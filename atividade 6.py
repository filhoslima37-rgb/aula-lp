import psutil
import time

try:
    while True:
        
        cpu_total = psutil.cpu_percent(interval=1)
        
        
        cpu_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)
        
        
        print(f"\nCPU Total: {cpu_total}%")
        
        
        for i, uso in enumerate(cpu_por_nucleo):
            print(f"Núcleo {i}: {uso}%", end=" | ")
        
        print()  

except KeyboardInterrupt:
    print("\nPrograma encerrado.")