import subprocess
import time
import pyautogui as pygui

path = "C:\\Arquivos de Desenvolvimento\\Learning_Python\\GamingMode_Script\\Atalhos"

xbox = "\\XboxPcApp.exe.lnk"
battlenet = "\\Battle.net Launcher.exe.lnk"
steam = "\\Steam.exe.lnk"
epic = "\\EpicGamesLauncher.exe.lnk"
discord = "\\Discord.exe.lnk"

Apps = [xbox, battlenet, epic, discord]

print("~~~ Inicializando Programas... ~~~")

for app in Apps:
    try:
        open = (path + app)
        print(f"\nAbrindo '{app}'!")
        subprocess.run(open, shell=True)
    except FileNotFoundError:
        print(f"\nO arquivo '{open}' não foi encontrado.")
    except Exception as e:
        print(f"\nOcorreu um erro ao tentar executar o arquivo: {e}")
    else:
        print(f"\n '{app}' aberto com sucesso!")
        #pygui.hotkey('alt', 'f4')

    if(app != Apps[-1]):
        print("\nAguardando para abrir o próximo...")
        time.sleep(8)

input("\nRotina Finalizada!! :D \nPressione Enter para sair...")