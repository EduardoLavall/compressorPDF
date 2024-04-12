# syntax=docker/dockerfile:1

FROM python:latest 

WORKDIR /app
ENV FLASK_APP app.py

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copie o script de inicialização para o contêiner, Dê permissão de execução ao script
# COPY init_script.sh /init_script.sh
# RUN chmod +x /init_script.sh

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]