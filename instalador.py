import  subprocess 
import os

APPS_WINGET = [
    {"nome": "OpenVPN Connect", "comando": "winget install -e --id OpenVPNTechnologies.OpenVPNConnect"},
    {"nome": "Google Chrome", "comando": "winget install --id=Google.Chrome -e --silent"},
    {"nome": "Microsoft VS Code", "comando": "winget install --id=Microsoft.VisualStudioCode -e --silent"},
    {"nome": "7-Zip", "comando": "winget install --id=7zip.7zip -e --silent"},
    {"nome": "VLC Media Player", "comando": "winget install --id=VideoLAN.VLC -e --silent"},
    {"nome": "Notepad++", "comando": "winget install --id=Notepad++.Notepad++ -e --silent"},
    {"nome": "Java JRE (OpenJDK 17)", "comando": "winget install --id=Microsoft.OpenJDK.17 -e --silent"},
    {"nome": "AnyDesk", "comando": "winget install --id=AnyDesk.AnyDesk -e --silent"},
    {"nome": "Microsoft Teams", "comando": "winget install --id=Microsoft.Teams -e --silent"},
    {"nome": "LibreOffice", "comando": "winget install --id=TheDocumentFoundation.LibreOffice -e --silent"},
]

def by_criador():
    print("--------------------------------------------------")
    print("------------by Luis Filipe B. Muller--------------")
    print("--------------------------------------------------")

def mostrar_menu(catalogo_de_apps):
    print("\n----------------------------------------------")
    print(" SELECIONE OS PROGRAMAS QUE DESEJA INSTALAR")
    print("----------------------------------------------")
    for indice, app in enumerate(catalogo_de_apps, start=1):
        print(f" [{indice}] - {app['nome']}")
    print("----------------------------------------------")

def obter_escolhas_do_usuario(total_de_opcoes):
    escolhas_validas = []

    while not escolhas_validas:
        entrada_usuario = input(">> Digite os números dos programas separados por vírgula (ex: 2, 4, 6): ")
        
        numero_str = entrada_usuario.replace(',', ' ').split()

        if not numero_str:
            print("AVISO: Nenhuma opção digitada. Tente novamente.")
            continue

        try:
            numeros_int = [int(num) for num in numero_str]
            opcoes_invalidas = [num for num in numeros_int if not 1 <= num <= total_de_opcoes]
            
            if opcoes_invalidas:
                print(f"ERRO: Os números {opcoes_invalidas} são inválidos. Por favor, escolha apenas entre 1 e {total_de_opcoes}.")
            else:
               
                escolhas_validas = sorted(list(set(numeros_int)))
        except ValueError:
            print("ERRO: Por favor, digite apenas números. Tente novamente.")
            
    return escolhas_validas

def instalar_programas_selecionados(lista_de_instalacao):
    total = len(lista_de_instalacao)
    print("\n--- INICIANDO INSTALAÇÕES ---")
    for i, app in enumerate(lista_de_instalacao, start=1):
        try:
            print(f"\n[{i}/{total}] Instalando: {app['nome']}...")
            comando_completo = app['comando'] + " --silent --accept-source-agreements --accept-package-agreements"
            subprocess.run(comando_completo, shell=True, check=True, capture_output=True, text=True)
            print(f"{app['nome']} instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"ERRO ao instalar {app['nome']}. Detalhes: {e.stderr}")
        except KeyError:
            print(f"ERRO DE CONFIGURAÇÃO: O app '{app['nome']}' não tem a chave 'comando' definida corretamente.")
        except FileNotFoundError:
            print("ERRO: O comando 'winget' não foi encontrado. Verifique se o Gerenciador de Pacotes do Windows está instalado.")
            break


if __name__ == "__main__":
    by_criador()
    
    mostrar_menu(APPS_WINGET)
    
    escolhas = obter_escolhas_do_usuario(len(APPS_WINGET))
    
    apps_para_instalar = [APPS_WINGET[indice - 1] for indice in escolhas]
    
    print("\nOs seguintes programas serão instalados:")
    for app in apps_para_instalar:
        print(f"  - {app['nome']}")
    
    confirmacao = input("\n>> Deseja continuar com a instalação? (s/n): ").lower()
    
    if confirmacao == 's' or confirmacao == 'sim':
        instalar_programas_selecionados(apps_para_instalar)
        print("\nTodas as instalações selecionadas foram concluídas!")
    else:
        print("\nInstalação cancelada pelo usuário.")


