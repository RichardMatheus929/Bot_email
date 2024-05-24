
from Email import Email
from Extract import Extract


def listar_arquivos(diretorio):
    import os
    arquivos = os.listdir(diretorio)
    return arquivos
    

def realizar_processo(caminho):

    e = Extract(caminho)
    email = Email()
        
    # email_secretaria = "thiagoedu19@gmail.com"
    email_secretaria = "richardmatheus29112005@gmail.com"
    assunto = "Teste com conteudo padrao"
    conteudo = e.get_conteudo_padrao()
    caminho = caminho

    email.criar_email(email_secretaria,assunto,conteudo,caminho)
    # email.enviar_email()
    print(e.get_Nprocesso())
    
    


# Rodando tudo
all_files = listar_arquivos("C:/Programação/Bot thiago/arquivos")
contador = 1
for i in all_files:
    realizar_processo(f"C:/Programação/Bot thiago/arquivos/{i}")
    if contador == 2:
        break
    else:
        contador += 1
    from time import sleep;sleep(10)
    