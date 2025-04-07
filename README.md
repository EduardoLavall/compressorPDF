# compressorPDF📩
 Converte html para pdf e comprime o arquivo
 - recebe uma url e valida ela
 - define o nome do arquivo resultante
 - faz o download do arquivo bruto
 - comprime o arquivo utilizando GhostScript

## requisitos do sistema
- Sistema operacional Linux ou Windows
- Git
- Docker 

## como usar o compressorPDF
1. Clone o repositório do projeto para o diretório desejado
```bash
git clone https://github.com/EduardoLavall/compressorPDF pasta_desejada
```

2. Instale e execute o sistema com o comando:
```bash
docker compose up
```

3. Envie uma solicitação HTTP usando o método POST para o endereço do servidor
- O endereço deve seguir o seguinte formato 
```bash
http://endereço:porta/compressor_pdf
```

- A solicitação deve conter um JSON com o seguinte formato:
```json
{
    "url_html" : "https:/url-do-html/",
    "nome_arquivo": "nome_do_arquivo_desejado"
}
```
 onde "url_html" deve ser o endereço da página html que será convertida para pdf
 e "nome_arquivo" refere-se ao nome do arquivo resultante

4. A solicitação vai retornar uma URL de download do arquivo resultante









