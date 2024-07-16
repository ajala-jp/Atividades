class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    
    def Alterar_editora(self, novaeditora):
        self.editora= novaeditora
        print(f"Editora atualizada: {self.editora}")

    def Listar_qtde_paginas(self):
        print(f"Quantidade de páginas: {self.paginas}")


livro1 = Livro("Orfanato da senhorita Peregrine", "Ramsoon Riggs", "Sei la a editora", 300)


livro1.Alterar_editora("Sei la 2")

livro1.Listar_qtde_paginas()