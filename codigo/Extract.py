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
        <p>Segue Ordem de Compra, referente ao {self.get_Nprocesso()}, {self.get_despesa()}, {self.get_pregao()} do município de Touros/RN.</p>

        <p>Observações importantes:</p>

        <p>A Nota Fiscal deve ser faturada conforme a Ordem de Compra.
        Caso a empresa não disponha da totalidade dos itens para entrega imediata, a Nota Fiscal poderá ser faturada com os itens disponíveis, sendo necessário a edição da Ordem de Compra por parte do setor de compras da prefeitura. Ou seja, os itens não atendidos nesta Nota, podem ser enviados em outra Nota Fiscal, sendo emitida outra Ordem de Compra para a referida Nota.</p>

        <p>Informo que a entrega deverá ser feita das 7h às 13h, de segunda à sexta, no seguinte endereço:
        CENTRAL DE ABASTECIMENTO FARMACÊUTICO E ALMOXARIFADO Av. 27 de Março, S/N, Centro - Touros/RN por trás do Hospital Municipal Ministro Paulo de Almeida Machado</p>

        <p>Em relação à validade, observar a cláusula do Termo de Referência:
        "4. CRITÉRIOS DE ACEITAÇÃO DO OBJETO 4.1. A entrega dos produtos deverá ser realizada de segunda à sexta no horário dás 7h as 13h, na Central de Abastecimento Farmacêutico; 4.2. No caso de produtos perecíveis, o prazo de validade na data da entrega não poderá ser inferior a 12 (doze) meses do prazo total recomendado pelo fabricante"</p>

        <p>Solicito que ao emitir a nota fiscal, envie para os seguintes e-mails:
        pmt.financeiro.rn@gmail.com touroscontroladoria@gmail.com caftouros@gmail.com</p>

        <p>Estou à disposição para quaisquer dúvidas neste e-mail ou contato telefônico citado abaixo. Favor acusar recebimento.</p>

        <p>Atenciosamente,</p>"""
        return stringa