class Extract:

    def __init__(self,caminho_pdf):

        self.caminho_pdf = caminho_pdf
        
    def linhas_do_pdf(self):
        import fitz

        doc = fitz.open(self.caminho_pdf)
        text = ""

        for page in doc:
            page_text = page.get_text()
            text += page_text

        lines = text.splitlines()
        return lines
    
    def get_valor(self):
        for i in self.linhas_do_pdf():
            if "valor" in i.lower():
                valor = i
                return valor
        return "Nenhum valor encontrado"
    
    def get_Nprocesso(self):
        for i in self.linhas_do_pdf():
            if "processo" in i.lower():
                valor = i
                return valor
        return "Nenhum processo encontrado"
    
    def get_pregao(self):
        for i in self.linhas_do_pdf():
            if "modalidade" in i.lower():
                valor = i
                return valor.replace('Modalidade: ','')
        return "Nenhuma modalidade encontrado"
    
    def get_despesa(self):
        for i in self.linhas_do_pdf():
            if "despesa" in i.lower():
                valor = i
                return valor
        return "Nenhuma despesa encontrado"
    def get_conteudo_padrao(self):
        stringa = f"""
        """
        return stringa
