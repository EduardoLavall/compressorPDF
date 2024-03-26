@echo off

:: Cria o ambiente virtual
virtualenv -p python venv

:: Ativa o ambiente virtual
call venv\Scripts\activate

:: Instala as dependências
pip install -r requirements.txt

:: Instala o pre-commit
pre-commit install

echo Setup concluído.