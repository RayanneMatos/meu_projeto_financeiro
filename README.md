# Meu Projeto Financeiro

Um aplicativo web simples para gerenciamento financeiro pessoal, que permite registrar receitas e despesas, calcular o saldo e visualizar relatórios de transações.

## Funcionalidades

- **Exibição do Saldo Total**: A página inicial mostra o saldo atual, calculado com base nas transações registradas.
- **Registro de Transações**: Permite o cadastro de receitas e despesas, com descrição e valor.
- **Relatório de Transações**: Exibe um histórico das transações realizadas.

## Estrutura do Projeto

- `app.py`: Script principal que contém a lógica backend, desenvolvido com o framework Flask.
- Diretório `static/`: Arquivos de frontend, como scripts e estilos CSS.
  - `scripts/main.js`: Funções JavaScript para interações na interface.
  - `styles/styles.css` e `styles/styles_componentes.css`: Arquivos de estilo para personalizar a interface.
- Diretório `templates/`: Templates HTML que estruturam as páginas do aplicativo.
  - `index.html`: Página inicial que exibe o saldo.
  - `add_transaction.html`: Formulário para adicionar uma nova transação.
  - `report.html`: Página que mostra o relatório de transações.

## Pré-requisitos

- Python 3.x
- Flask

## Instalação

1. Clone este repositório:
-Execute o comando abaixo para clonar o repositório em sua máquina:
git clone https://github.com/RayanneMatos/meu_projeto_financeiro.git
- Após clonar, navegue até a pasta do projeto:
cd meu_projeto_financeiro

3. Instalar as dependências:

**Python 3**
1. Verifique se o Python 3 já está instalado
No terminal ou linha de comando, execute:
python3 --version
Se o Python 3 não estiver instalado ou se você estiver usando uma versão desatualizada, siga as etapas abaixo.

2. Instale o Python 3
-Windows:
Baixe o instalador do Python no site oficial.
Execute o instalador e marque a opção Add Python to PATH antes de continuar com a instalação.
-Linux (via terminal):
Atualize seus pacotes e instale o Python:
sudo apt update
sudo apt install python3
-Mac:
Utilize o Homebrew:
brew install python3

3. Verifique o gerenciador de pacotes pip
Certifique-se de que o pip (gerenciador de pacotes do Python) está instalado:
pip3 --version

Se o pip não estiver instalado, execute:
python3 -m ensurepip --upgrade

**Flask**
1. Instale o Flask
- Crie e ative um ambiente virtual (opcional, mas recomendado)
No diretório do projeto, crie um ambiente virtual para evitar conflitos de dependências:
python3 -m venv venv
Ative o ambiente virtual:
- Windows:
venv\Scripts\activate
- Linux/Mac:
source venv/bin/activate

Com o ambiente virtual ativado (ou diretamente, se não for usar um), instale o Flask usando o pip:
pip install flask

Confirme que o Flask foi instalado corretamente:
flask --version
