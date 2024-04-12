import requests
import subprocess
import validators
#import ghostscript


#compressorPDF
def validar_url():
    #valida a url digitada
    while True:
        url=input("Digite a url de download do arquivo html: ")
        if validators.url(url):
            break
        print("URL inválida.")
    return url

def validar_url_request(url):
    #valida a url digitada
    while True:
        if validators.url(url):
            return url
        else:
            return False
    

def baixar_arquivo(url, arquivoBruto):
    #envia a url como parâmetro para a API e baixa o arquivo PDF bruto
    api = "https://htmltopdf.hcc.app.br/?url="
    print("Baixando o pdf...")
    response = requests.get(api + url)
    if response.status_code == 200:
        with open(arquivoBruto+'.pdf', 'wb') as f:
            f.write(response.content)
        print("Arquivo baixado com sucesso!")
    else:
        print("Falha ao baixar o arquivo:", response.status_code)
        return False

#def convert_to_pdf(arquivoBruto, output_file):
#    args = [
#        "-dBATCH",
#        "-dNOPAUSE",
#        "-sDEVICE=pdfwrite",
#        "-dCompatibilityLevel=1.4",
#        "-sNAME=setting"
#        f"-sOutputFile={output_file}",
#        arquivoBruto
#    ]
#    ghostscript.Ghostscript(*args)

def compress_pdf(input_file, output_file, quality='screen'):
    args = [
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        "-dPDFSETTINGS=/" + quality,
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        "-sOutputFile={output_file}",
        input_file
    ]
    ghostscript.Ghostscript(*args)

def comprimir_arquivo_pdf(arquivoBruto):
    #comprime o arquivo utilizando ghostscript
    
    diretorioGS = r'C:\Program Files\gs\gs10.03.0\bin\gswin64'
    arquivoComprimido = arquivoBruto+"-comprimido.pdf"
    command = '{} -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -sNAME=setting -sOutputFile={} {}'.format(diretorioGS, arquivoComprimido, arquivoBruto+'.pdf')
    print (command)
    print("Comprimindo o arquivo PDF")
    try:
        subprocess.run(command, shell=False, check=True)
        print("Arquivo PDF comprimido gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao comprimir o arquivo PDF:", e)
        
def comprimir_arquivo_pdf2(arquivoBruto):
    #comprime o arquivo utilizando ghostscript
    
    diretorioGS = r'.\gs\gs10.03.0\bin\gswin64'
    arquivoComprimido = arquivoBruto+"-comprimido.pdf"
    command = '{} -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -sNAME=setting -sOutputFile={} {}'.format(diretorioGS, arquivoComprimido, arquivoBruto+'.pdf')
    print (command)
    print("Comprimindo o arquivo PDF")
    try:
        subprocess.run(command, shell=False, check=True)
        print("Arquivo PDF comprimido gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print("Ocorreu um erro ao comprimir o arquivo PDF:", e)

#url = r'https://hcc-prd.s3.amazonaws.com/IDF/158582/Orçamento/Proposta/Proposta_IDF_158582_V1.1.html'
def main():
    url = validar_url()
    arquivoBruto = input('digite o nome do arquivo desejado (exemplo "documento"): ')
    baixar_arquivo(url, arquivoBruto)
    comprimir_arquivo_pdf2(arquivoBruto)
    print ('Fim')
    exit()
    
def compressorpdf(url, nomeArquivo):
    #recebe a url e o nome do arquivo
    if not validar_url_request(url):
        print("url inválida")
        return False
    else:
        baixar_arquivo(url, nomeArquivo)
        comprimir_arquivo_pdf2(nomeArquivo)
        return nomeArquivo
    
if __name__ == "__main__":
    main()
    








