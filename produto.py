'''
    Módulo produto
    Classe Produto
'''


class Produto():

    def _init_(self, id, codigo, descricao, valor):
        self.id = id
        self.codigo=codigo
        self.descricao=descricao
        self.valor=valor 

    def str(self):
        string="Id={3} Codigo={2} Descricao={1} Valor={0}".format(self.valor, self.descricao, self.codigo, self.id)      
        return string

