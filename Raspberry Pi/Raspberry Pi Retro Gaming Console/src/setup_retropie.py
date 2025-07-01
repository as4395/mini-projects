import os
import subprocess

def update_system():
    subprocess.run(['sudo', 'apt', 'update'], check=True)
    subprocess.run(['sudo', 'apt', 'upgrade', '-y'], check=True)

def install_git():
    subprocess.run(['sudo', 'apt', 'install', '-y', 'git'], check=True)

def clone_retropie():
    subprocess.run(['git', 'clone', '--depth=1',
                    'https://github.com/RetroPie/RetroPie-Setup.git'], check=True)

def run_setup_script():
    os.chdir('RetroPie-Setup')
    subprocess.run(['chmod', '+x', 'retropie_setup.sh'], check=True)
    subprocess.run(['sudo', './retropie_setup.sh'], check=True)

if __name__ == '__main__':
    update_system()
    install_git()
    clone_retropie()
    run_setup_script()
