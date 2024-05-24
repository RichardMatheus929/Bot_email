class Email:

    def __init__(self):
        import win32com.client as win32
        self.outlook = win32.Dispatch('outlook.application')
        self.email = self.outlook.CreateItem(0)

    def criar_email(self,para_quem,assunto,conteudo,file_path):
        self.email.To = para_quem
        self.email.Subject = assunto
        self.email.HTMLBody = conteudo
        self.email.Attachments.Add(file_path)
    
    def enviar_email(self):
        self.email.Send()
        



