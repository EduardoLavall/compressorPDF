#!/bin/bash

# Verifica se o sistema operacional é Linux
if [[ "$(uname)" == "Linux" ]]; then
    echo "Executando comandos específicos para Linux..."
    # Coloque aqui os comandos específicos para Linux
fi

# Verifica se o sistema operacional é Windows
if [[ "$(uname -s)" == "Windows_NT" ]]; then
    echo "Executando comandos específicos para Windows..."
    # Coloque aqui os comandos específicos para Windows
fi

# Verifica se o sistema operacional é macOS
if [[ "$(uname)" == "Darwin" ]]; then
    echo "Executando comandos específicos para macOS..."
    # Coloque aqui os comandos específicos para macOS
fi

# Executa o comando principal do contêiner
exec "$@"