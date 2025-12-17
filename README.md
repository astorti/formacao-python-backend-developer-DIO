<hr>

<img src="./assets/formacao-python-backend-developer.png"/>

### FORMAÇÃO PYTHON BACKEND DEVELOPER

Repositório para implementação e estudo dos códigos desenvolvidos durante o curso **Formação Python Backend Developer**, oferecido pela plataforma de ensino [**Digital Innovation One - DIO**](https://www.dio.me)

### Links

- [Documentação Python](https://www.python.org/doc/)
- [PYPI](https://pypi.org/)
- [pipenv](https://pipenv.pypa.io/en/latest/)
- [Poetry](https://python-poetry.org/)
- [pipx](https://pipx.pypa.io/stable/)
- [PEP 8](https://peps.python.org/pep-0008/)

### Conceitos Desenvolvidos

- **Gerenciamento de Pacotes**
    - **conceitos**: 
        - pacotes: módulos que podem ser instalados e utilizados nos programas Python
        - PYPI (Python Package Index): local onde os pacotes são armazenados
    - **ambiente virtual**
        - comandos:
            - criar ambiente virtual:
                - `python3 -m venv .env`
            - ativar ambiente viertual: 
                - `source .env/bin/activate`
                - OBS: No lugar do **.env** também pode informar um nome para o ambiente virtual.
            - sair do ambiente virtual: `deactivate`
    - **gerenciadores de pacotes**
        - **pip**
            - comandos básicos pip:
                - `pip install nome_do_pacote`
                - `pip install --update nome_do_pacote`
                - `pip uninstall nome_do_pacote`
                - `pip list`
        - **pipenv**: combina gestão de dependências com criação de ambiente virtual
            - instalação
                - instalação recomendada para Ubuntu 24.04
                    - `sudo apt install pipenv`
                - instalação do pipenv em ambiente global
                    - `pip install pipenv`
            - comandos básicos pipenv:
                - `pipenv install nome_do_pacote`
                - `pipenv uninstall nome_do_pacote`
                - `pipenv lock`: gera o arquivo de dependência .lock
                - `pipenv graph`: lista as dependências instaladas
                - `pipenv clean`: remove dependências não referenciadas no arquivo lock
        - **Poetry**
            - instalação
                - instalação recomendada para Ubuntu 24.04
                    - `sudo apt install pipx`
                    - `pipx ensurepath`: garante que o sistema encontre os executáveis do pipx e dos pacotes instalados com ele 
                    - `pipx install poetry`
                - instalação do pipenv em ambiente global
                    - `pip install poetry`
            - comandos básicos Poetry:
                - `poetry new nome_do_projeto`
                - `poetry add nome_da_dependência`
                - `poetry remove nome_da_dependência`

- **Boas Práticas**
    - PEP 8
        - identação de 4 espaços
        - limitar linhas em 79 caracteres
        - nome de variaveis e funções em snake_case
        - nome de classesem CamelCase
    - ferramentas
        - **Flake8**: Linter (analisador estático)
            - `flake8 nome_do_arquivo.py`
        - **Black**: formatador de código
            - `black nome_do_arquivo.py`
        - **Isort**: organizador de imports
            - `isort nome_do_arquivo.py`
    - extensões VSCode
        - Black Formatter (Microsoft)
        - isort (Microsoft)

- **Banco de Dados Relacionais**

    - Fundamentos
        - tabelas
        - chaves primárias
        - chaves estrangeiras
        - SQL (**S**tructured **Q**uery **L**anguage)
    - Conexão Banco de Dados
        - Python DB API
            - SQLite
                ```
                import sqlite3
                conexao = sqlite3.connect('nome_banco_de_dados.bd)
                ```
            - metodos
                - execute()
                - commit()
                - executemany()
                - fetchone()
                - fetchall()
                - rollback()
            - row_factory
            - classe Row
            - tratamento de exceções

- **Aplicações Rest**
    - Desenvolvimento Web
        - estrutura básica da web
        - arquitetura cliente-servidor
        - tecnologias frontend
        - tecnologias backend
    - API
        - RESTful
            - APIs que seguem os princípios REST (Representational State Transfer)
            - utlizam padrão HTTP (GET, POST, UPDATE, DELETE)
            - utilizadas em interações web
        - SOAP (Simple Object Access Protocol)
            - utiliza XML para troca de informações
        - GraphQL
            - permite que seja especificado quais dados serão solicitados
            - reduz solicitações e tamanho dos dados transferidos
            - flexível e fortemente tipada

- **Desafios de Códigos**

    - **Desafio 01: Extração de Domínios de Email** Os domínios de email são essenciais para categorizar e identificar a origem dos contatos, facilitando a segmentação e análise dos dados. Sabendo disso, sua função será receber uma string contendo múltiplos emails separados por ponto e vírgula e retornar uma lista contendo apenas os domínios de cada um desses emails. **Entrada:** A entrada deve receber uma string contendo emails separados por ponto e vírgula: "email;email;email;...". Cada email é uma string. **Saída:** Deverá retornar uma lista de strings com os domínios dos emails.

    - **Desafio 02: Transformação de Datas** Você está desenvolvendo um sistema que integra com uma API de dados transacionais, onde as datas são fornecidas no formato "DD-MM-YYYY". Sua tarefa é processar essa lista de datas e transformá-las para o formato internacional "YYYY/MM/DD". **Entrada:** A entrada deve receber uma string contendo datas separadas por ponto e vírgula: "DD-MM-YYYY;DD-MM-YYYY;...". Cada data é uma string. **Saída:** Deverá retornar uma lista de strings contendo as datas no formato "YYYY/MM/DD".

    - **Desafio 03: Conversão de Dados de Temperatura** Você está desenvolvendo um sistema de monitoramento de temperaturas para uma estação meteorológica. O seu script deve processar os dados brutos de temperaturas e converter esses dados de Celsius para Fahrenheit. Para converter uma temperatura de Celsius para Fahrenheit, utiliza-se a fórmula matemática: `Fahrenheit = (Celsius × 9/5) + 32`. **Entrada:** A entrada deve receber uma string com valores numéricos separados por “,” (vírgula) representando as temperaturas em graus Celsius. **Saída:** Deverá retornar uma lista de valores numéricos representando as temperaturas convertidas para Fahrenheit.

    - **Desafio 04:  Filtragem de Produtos em Estoque** Imagine que você está trabalhando em um sistema de gerenciamento de estoque que recebe dados de produtos de uma API externa. Cada produto é representado por uma string que contém seu nome, preço e a quantidade disponível em estoque. Por exemplo, a string `Laptop:1200:10;Mouse:20:0;Keyboard:50:5` indica que há 10 unidades do laptop disponíveis, 0 unidades do mouse e 5 unidades do teclado. Seu objetivo é implementar uma função em Python que filtre apenas os produtos que têm quantidade maior que zero. A função deve então retornar uma lista de strings, onde cada string representa um produto disponível, no formato original `NOME:PRECO:QUANTIDADE` **Entrada:** A entrada deve receber uma lista de strings contendo o nome do produto, preço e a quantidade disponível em estoque, separados por “:” respectivamente. **Saída:** Deverá retornar uma lista de strings, onde cada string contém as informações dos produtos que têm quantidade maior que 0.

    - **Desafio 05: Filtragem de Transações Acima de um Valor Específico** Você está consumindo dados de uma API de uma instituição financeira que fornece uma lista de transações. Seu desafio é filtrar todas as transações que possuem um valor acima de um determinado limite. **Entrada:** A entrada deve receber dois valores: **1)** Um número decimal representando o valor limite. **2)** Uma string contendo transações no seguinte formato: `ID:VALOR;ID:VALOR;...` **Saída:** Deverá retornar uma lista de strings, onde cada string contém as informações das transações cujo valor é maior que o valor limite especificado.

    - **Desafio 06: Filtragem de Clientes de uma Cidade** Uma empresa de marketing deseja segmentar seus clientes para uma nova campanha promocional. A empresa fornece uma lista de clientes, cada um com seu nome e cidade. Sua tarefa é filtrar os clientes que moram em uma cidade específica. **Entrada:** A entrada consiste em duas partes: **1)** Uma string representando a cidade de interesse para a campanha. **2)** Uma string contendo o nome do cliente (string) e a cidade do cliente (string), no seguinte formato: `CLIENTE:CIDADE;CLIENTE:CIDADE;...` **Saída:** O programa deverá retornar uma lista de tuplas contendo os clientes que moram na cidade especificada.
