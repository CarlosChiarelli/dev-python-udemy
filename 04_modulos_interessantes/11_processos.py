"""Para executar processos no SO."""
import subprocess

# Windows - ping 127.0.0.1
# Linux - ping 127.0.0.1 -c 4

proc = subprocess.run(
    ['ping', '127.0.0.1', '-c', '4'], capture_output=True, text=True
)

proc2 = subprocess.run(['ls', '-a'], capture_output=True, text=True)

saida = proc.stdout
print(saida)

print(proc2.stdout)
