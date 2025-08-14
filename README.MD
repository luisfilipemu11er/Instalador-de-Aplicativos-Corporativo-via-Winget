##

Instalador de Aplicativos Corporativo via Winget
Autor: Luis Filipe Bras Muller
Versão: 1.0
Data da Última Atualização: 14 de Agosto de 2025

🎯 Objetivo do Projeto
Este script foi desenvolvido com o intuito de otimizar e padronizar o processo de instalação de aplicativos essenciais em máquinas Windows, com um foco especial no ambiente corporativo.

No dia a dia de departamentos de TI e suporte técnico, a configuração de um novo computador para um colaborador é uma tarefa repetitiva e que consome um tempo valioso. O processo manual de baixar e instalar cada programa individualmente está sujeito a erros, inconsistências de versão e à instalação de softwares indesejados (adware).

Este automatizador centraliza e acelera essa tarefa, permitindo que, com um único comando, um técnico ou o próprio usuário possa selecionar e instalar um conjunto pré-aprovado de aplicativos de forma silenciosa e eficiente.

❓ Por que usar este script?

Economia de Tempo: Reduz drasticamente o tempo de configuração de uma nova máquina, de horas para minutos.

Padronização: Garante que todos os colaboradores tenham o mesmo conjunto de softwares aprovados e nas versões corretas, evitando problemas de compatibilidade.

Segurança: Ao usar o winget, os aplicativos são baixados de fontes oficiais e seguras. Além disso, a instalação silenciosa evita que o usuário instale acidentalmente barras de ferramentas ou adware.

Autonomia para o Usuário: Permite que novos colaboradores realizem parte do seu próprio setup de forma guiada e segura, liberando a equipe de TI para tarefas mais complexas.

🚀 Como Utilizar

Pré-requisitos:

Python: É necessário ter o Python instalado na máquina. Você pode baixá-lo em python.org.

Winget: O Gerenciador de Pacotes do Windows (winget) deve estar disponível. Ele já vem instalado nas versões mais recentes do Windows 10 e 11.

Execução:

Salve o arquivo instalador.py numa pasta no seu computador.

Abra um terminal (PowerShell ou Prompt de Comando) nessa mesma pasta.

Execute o script com o comando:

python instalador.py

Siga as instruções na tela: digite os números dos programas que deseja instalar, separados por vírgula ou espaço, e pressione Enter.

Confirme a sua seleção e aguarde a conclusão das instalações.

🔧 Como Customizar

Para adicionar, remover ou alterar os programas disponíveis no menu, basta editar a lista APPS_WINGET no início do arquivo instalador.py.

Cada programa é um dicionário com duas chaves:

"nome": O nome amigável que aparecerá no menu.

"comando": O comando base do winget para a instalação.

Exemplo para adicionar o Keepass:

Encontre o ID do Keepass com winget search Keepass (o ID é DominikReichl.KeePass).
Adicione a seguinte linha à lista APPS_WINGET:

{"nome": "KeePass", "comando": "winget install -e --id DominikReichl.KeePass"},

Site para busca de ID de programas:

(https://winget.run/)
(https://winstall.app/)

⚙️ Funcionalidades Detalhadas
Menu Interativo: Permite ao usuário escolher quais aplicativos de uma lista pré-definida ele deseja instalar.

Instalação Silenciosa: Os programas são instalados em segundo plano, sem a necessidade de interação do usuário.

Instalação sem Privilégios de Administrador: O script utiliza o parâmetro --scope user, tentando instalar os aplicativos apenas para o usuário atual.

Seleção Múltipla: O usuário pode instalar vários programas de uma só vez.

Validação de Entrada: O script trata erros comuns do usuário, como digitar letras em vez de números ou selecionar opções inválidas.

⚠️ Solução de Problemas Comuns
Erro: 'winget' não é reconhecido como um comando interno...

Causa: O Gerenciador de Pacotes do Windows não está instalado ou o seu caminho não está nas variáveis de ambiente do sistema.

Solução: Verifique se tem a versão mais recente do "Instalador de Aplicativo" na Microsoft Store.

Erro: ❌ ERRO ao instalar [Nome do Programa].

Causa: O instalador do programa específico pode ter falhado, mesmo no modo silencioso, ou pode exigir permissão de administrador que foi negada.

Solução: Tente executar o terminal como Administrador antes de rodar o script. Se o erro persistir, o problema pode ser específico do pacote daquele programa no winget.

💡 Melhorias Futuras
[ ] Adicionar suporte para instaladores locais (.exe / .msi) que estejam na mesma pasta.

[ ] Criar uma interface gráfica simples (usando bibliotecas como Tkinter ou PyQt).

[ ] Ler a lista de programas de um arquivo externo (como um .json ou .csv) para facilitar a customização sem alterar o código.

[ ] Adicionar uma função para desinstalar programas usando o mesmo menu.

🛠️ Tecnologias Utilizadas
Python 3: Linguagem principal do script.

Winget (Gerenciador de Pacotes do Windows): Ferramenta utilizada para buscar e instalar os aplicativos.

##
