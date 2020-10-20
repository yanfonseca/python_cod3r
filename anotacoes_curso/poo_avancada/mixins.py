class HtmlToStringMixin:
    def __str__(self):
        # conversao para html
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''


class PessoaHtml(HtmlToStringMixin, Pessoa):  # A ordem das classes informadas importa!
    pass


class AnimalHtml(HtmlToStringMixin, Animal):  # A ordem das classes informadas importa!
    pass


if __name__ == '__main__':
    primeiraPessoa = Pessoa('Maria Eduarda')
    print(primeiraPessoa)

    segundaPessoa = PessoaHtml('Roberto Carlos')
    print(segundaPessoa)

    toto = AnimalHtml('Totó')
    print(toto)

    gato = AnimalHtml('Gato', False)
    print(gato)
