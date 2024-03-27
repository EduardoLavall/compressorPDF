from flask import Flask, request, jsonify, send_from_directory, url_for
import compressor
import os

app = Flask(__name__)

@app.route('/compressor_pdf', methods=['POST'])
def compressor_pdf():
    # Verifica se a solicitação contém JSON
    if request.is_json:
        # Obtém o nome do arquivo do corpo JSON da solicitação
        dados_json = request.json
        url_html = dados_json.get('url_html')
        nome_arquivo = dados_json.get('nome_arquivo')
        
        if url_html and nome_arquivo:
            try:
                compressor.compressorpdf(url_html, nome_arquivo)
            except:
                return "erro ao comprimir o arquivo"
            else:
                nome_arquivo = nome_arquivo+"-comprimido.pdf"
                print ("nome do arquivo: "+nome_arquivo)
                # Verifica se o arquivo existe na pasta do aplicativo
                diretorio_app = os.path.dirname(os.path.abspath(__file__))
                caminho_arquivo = os.path.join(diretorio_app, nome_arquivo)

                if os.path.exists(caminho_arquivo):
                    print ("existe")
                    # Constrói a URL de download com base na rota do aplicativo Flask e no nome do arquivo
                    url_download = url_for('download_pdf', nome_arquivo=nome_arquivo, _external=True)
                    return jsonify({'url_download': url_download})
                else:
                    return f'O arquivo "{nome_arquivo}" não existe na pasta do aplicativo', 404
        else:
            return 'Por favor, forneça o nome do arquivo no corpo da solicitação JSON', 400
    else:
        return 'O corpo da solicitação deve ser JSON', 400

@app.route('/download_pdf/<nome_arquivo>', methods=['GET'])
def download_pdf(nome_arquivo):
    # Verifica se o arquivo existe na pasta do aplicativo
    diretorio_app = os.path.dirname(os.path.abspath(__file__))
    print ("diretório app "+diretorio_app)
    caminho_arquivo = os.path.join(diretorio_app, nome_arquivo)
    print ("caminho arquivo "+caminho_arquivo)

    if os.path.exists(caminho_arquivo):
        print ("path existe")
        # Retorna o arquivo como resposta
        return send_from_directory(diretorio_app, nome_arquivo, as_attachment=True)
    else:
        return f'O arquivo "{nome_arquivo}" não existe na pasta do aplicativo', 404

if __name__ == "__main__":
    app.run(debug=True)
