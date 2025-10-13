
# Gerenciador de Senhas em Linha de Comando (CLI)

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)

Um gerenciador de senhas simples e seguro, desenvolvido em Python, que permite gerar, salvar e gerenciar suas credenciais diretamente do terminal. Este projeto foi criado como uma ferramenta de uso pessoal e como uma peça de portfólio para demonstrar habilidades em Python, manipulação de arquivos e criptografia.

---

### ✨ Funcionalidades Principais

* **🔑 Criptografia Forte:** Utiliza a biblioteca `cryptography` (padrão da indústria) com o algoritmo Fernet para garantir que suas senhas sejam armazenadas de forma segura.
* **✍️ Adicionar Senhas:** Salve novas credenciais (site e senha) de forma intuitiva.
* **👀 Visualizar Senhas:** Exibe todas as suas senhas salvas de forma organizada em uma tabela no terminal, descriptografando-as apenas no momento da visualização.
* **🗑️ Remover Senhas:** Apague credenciais antigas de forma segura.
* **🎲 Gerador de Senhas:** Crie senhas fortes e aleatórias com comprimento personalizável, incluindo letras, números e símbolos.

---

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Bibliotecas Principais:**
    * `cryptography`: Para a criptografia simétrica das senhas.
    * `tabulate`: Para a exibição dos dados em uma tabela formatada no terminal.

---

### 🚀 Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/AlexMachineCode/python-password-manager.git](https://github.com/AlexMachineCode/python-password-manager.git)
    ```

2.  **Navegue até o diretório:**
    ```bash
    cd python-password-manager
    ```

3.  **Instale as dependências:**
    (Certifique-se de ter um arquivo `requirements.txt` com as bibliotecas `cryptography` e `tabulate`)
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o programa:**
    ```bash
    python3 passManager.py
    ```
    *A primeira execução irá gerar automaticamente um arquivo `chave.key` para a criptografia.*

---

### ⚠️ Aviso de Segurança

* Este projeto armazena a chave de criptografia (`chave.key`) e o arquivo de senhas (`senhas.txt`) localmente. **NÃO COMPARTILHE** o arquivo `chave.key` com ninguém.
* É crucial adicionar os arquivos `chave.key` и `senhas.txt` ao seu `.gitignore` para evitar que eles sejam enviados acidentalmente para o repositório.

---
