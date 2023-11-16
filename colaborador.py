

class Colaborador():
    def __init__(self, id, departamento, setor, nome, sobrenome):
        self.__id = id
        self.__departamento = departamento
        self.__setor = setor
        self.__nome = nome
        self.__sobrenome = sobrenome
        
    def dados_colaborador(self):
        dados_colaborador = {'id':self.__id, 'departamento':self.__departamento, 'setor': self.__setor, 'nome': self.__nome, 'sobrenome':self.__sobrenome}
        return dados_colaborador
    