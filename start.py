import subprocess
import os

def run_server():
    subprocess.run('cd sneaker_store && venv\\Scripts\\activate', shell=True)


    command = "cd sneaker_store && python manage.py runserver"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    run_server()