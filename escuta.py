import time
from pynput.keyboard import Listener
import threading

# Variável para rastrear o último tempo em que houve atividade no teclado
ultimo_tempo_atividade = time.time()

# Função para atualizar o tempo de atividade e registrar no log
def atualizar_tempo_atividade(key):
    global ultimo_tempo_atividade
    ultimo_tempo_atividade = time.time()
    tecla = str(key)
    tempo_sem_atividade = ultimo_tempo_atividade - ultimo_tempo_atividade
    tempo_formatado = "{:.2f}".format(tempo_sem_atividade)
    with open("log_teclado.txt", "a") as arquivo_log:
        arquivo_log.write(f"Tecla pressionada: {tecla}\n")
        arquivo_log.write(f"Tempo sem atividade: {tempo_formatado} segundos\n")

# Função para verificar o tempo sem atividade e registrar em um arquivo de log
def verificar_tempo_sem_atividade():
    global ultimo_tempo_atividade
    while True:
        tempo_sem_atividade = time.time() - ultimo_tempo_atividade
        tempo_formatado = "{:.2f}".format(tempo_sem_atividade)
        with open("log_teclado.txt", "a") as arquivo_log:
            arquivo_log.write(f"Tempo sem atividade: {tempo_formatado} segundos\n")
        time.sleep(5)  # Verificar o tempo sem atividade a cada 5 segundos

# Iniciar a thread para verificar o tempo sem atividade
thread_sem_atividade = threading.Thread(target=verificar_tempo_sem_atividade)
thread_sem_atividade.daemon = True
thread_sem_atividade.start()

# Configurar o listener do teclado para rastrear a atividade
with Listener(on_press=atualizar_tempo_atividade) as listener:
    listener.join()  # Aguardar até que o listener seja interrompido (pode ser interrompido com Ctrl+C)
