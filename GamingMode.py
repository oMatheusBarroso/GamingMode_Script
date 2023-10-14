import subprocess
import time
import pyautogui as pygui

# Caminho padrão para os atalhos
path = "C:\\Arquivos de Desenvolvimento\\Learning_Python\\GamingMode_Script\\Atalhos"

# Atalhos dos programas no diretório
xbox = "\\XboxPcApp.exe.lnk"
battlenet = "\\Battle.net Launcher.exe.lnk"
epic = "\\EpicGamesLauncher.exe.lnk"
discord = "\\Discord.exe.lnk"
steam = "\\Steam.exe.lnk"

# Array para organizar ordem de execução dos programas
Apps = [xbox, battlenet, epic, discord, steam]

print("~~~ Inicializando Programas... ~~~")

# Repetição para execução dos programas
for app in Apps:
    try:
        opening = path + app
        print(f"\nAbrindo '{app}'!")
        subprocess.run(opening, shell=True)
    except FileNotFoundError:
        print(f"\nO arquivo '{opening}' não foi encontrado.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar executar o arquivo: {e}")
    else:
        print(f"\n '{app}' aberto com sucesso!")
        # pygui.hotkey('alt', 'f4')

    # Condicional para não mostrar a mensagem de próximo na execução do último programa
    if app != Apps[-1]:
        print("\nAguardando para abrir o próximo...")
        # Rotina de delay para não sobrecarregar o computador com muitos processos
        time.sleep(8)

# Add alguma rotina para fechar o programa caso ele pare em um processo e um tempo determinado extrapole

input("\nRotina Finalizada!! :D \nPressione Enter para sair...")
