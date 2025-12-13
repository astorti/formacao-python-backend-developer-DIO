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