""" 
Entidades:
    - Portafolio
    - Obras de arte
        - tipo
        - fecha de creacion
        - valor
    - Fotografias obras o videos (Multimedia)
    - Autores de las obras
    - Exposiciones
        - Fecha
        - Lugar (galería?)
        - descripcion    
"""
from datetime import datetime


class Author:
    counter = 0

    def __init__(self, name, age, phone, email):
        Author.counter += 1
        self._id = Author.counter
        self._name = name
        self._age = age
        self._phone = phone
        self._email = email


class Artwork:
    counter = 0

    def __init__(self, type, creationDate, price):
        Artwork.counter += 1
        self._id = Artwork.counter
        self._type = type
        self._creationDate = creationDate
        self._price = price

    def show(self):
        print(f'Tipo {self._type}')
        print(f'Creación {self._creationDate}')
        print(f'Precio Q{self._price}')


class AuthorWork:

    def __init__(self, idAuthor, idWork):
        self._idAuthor = idAuthor
        self._idWork = idWork


class Multimedia:
    def __init__(self, type, uri, idWork):
        self._type = type
        self._uri = uri
        self._idWork = idWork


class Portfolio:
    counter = 0

    def __init__(self, description, idExpo):
        Portfolio.counter += 1
        self._id = Portfolio.counter
        self._description = description
        self._idExpo = idExpo


class PortfolioWork:
    def __init__(self, idPortfolio, idWork):
        self._idPortfolio = idPortfolio
        self._idWork = idWork


class Expo:
    counter = 0

    def __init__(self, address, description, dates=[]):
        Expo.counter += 1
        self._id = Expo.counter
        self._address = address
        self._description = description
        self._dates = dates

    def addDates(self, date):
        self._dates.append(date)

    def show(self, authors, artworks, authorworks, multimedias, portfolios, portfoliosworks):
        portfoliosExpo = [
            portfolio for portfolio in portfolios if portfolio._idExpo == self._id]

        for p in portfoliosExpo:
            print('*'*50)
            print(f'Expo: {p._description}\n')
            worksId = [
                pw._idWork for pw in portfoliosworks if p._id == pw._idPortfolio]
            works = [work for work in artworks if work._id in worksId]
            for w in works:
                w.show()
                print('_'* 10)
            print('*'*50)


if __name__ == '__main__':
    # Creando autores
    author1 = Author('Pedro Pablo', 50, '+50235234234', 'pp@mail.com')
    author2 = Author('Alonso Alemán', 60, '+50235234234', 'aa@mail.com')
    authors = [author1, author2]
    # Creando obras
    artkwork1 = Artwork('pintura', datetime.strptime(
        '00-03-03', '%y-%m-%d'), 50000)
    artkwork2 = Artwork('escultura', datetime.strptime(
        '19-03-03', '%y-%m-%d'), 25000)

    artworks = [artkwork1, artkwork2]
    # Relacionando obras con autores
    authorWork1 = AuthorWork(idAuthor=1, idWork=1)
    authorWork2 = AuthorWork(idAuthor=2, idWork=1)
    authorWork3 = AuthorWork(idAuthor=2, idWork=2)

    authorworks = [authorWork1, authorWork2, authorWork3]

    # Multimedia de las obras
    mult1 = Multimedia(type='foto', uri='www.fotos.google/14241', idWork=1)
    mult2 = Multimedia(type='video', uri='www.youtube.com/13424241', idWork=2)

    multimedias = [mult1, mult2]
    # Creando expo
    expo = Expo(address='Interplaza, Quetzaltenango', description='Presentación obras de artistas quetzaltecos', dates=[datetime.strptime(
        '22-12-03', '%y-%m-%d')])

    # Creando un portafolio
    portfolio1 = Portfolio('Obras quetzaltecas', 1)
    portfolios = [portfolio1]
    # Relacionando obras con porfatolio
    portfolioWork1 = PortfolioWork(idPortfolio=1, idWork=1)
    portfolioWork2 = PortfolioWork(idPortfolio=1, idWork=2)
    portfoliosworks = [portfolioWork1, portfolioWork2]

    expo.show(authors, artworks, authorworks,
              multimedias, portfolios, portfoliosworks)
