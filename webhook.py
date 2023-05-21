import subprocess

def stop_and_restart_container():
    # Ustavitev trenutno zagnanega Docker kontejnerja
    subprocess.run(['docker', 'stop', 'eager_hamilton'])

    # Prenesite najnovejšo različico kontejnerja iz Docker Container Registry
    subprocess.run(['docker', 'pull', 'samarcic/sa_vaje_marcic:index.html'])

    # Ponovni zagon kontejnerja z najnovejšo različico
    subprocess.run(['docker', 'start', 'eager_hamilton'])
# Izvajanje operacij ob prejemu webhooks klica
stop_and_restart_container()


