
from api import API_consumer
from api import API_Pokemon, API_Ice_and_Fire
from api import API_Rick_Morty, API_Star_Wars


class ETL:
    def consume(self, id, consumer=API_Pokemon()):
        if issubclass(type(consumer), API_consumer):
            print(consumer.extract(id))
        else:
            print('Falhou')
    def consume2(self, id, rick=API_Rick_Morty()):
        if issubclass(type(rick), API_consumer):
            print(rick.extract(id))
        else:
            print('Falhou')
    def consume3(self, id, star=API_Star_Wars()):
        if issubclass(type(star), API_consumer):
            print(star.extract(id))
        else:
            print('Falhou')
    def consume4(self, id, ice=API_Ice_and_Fire()):
        if issubclass(type(ice), API_consumer):
            print(ice.extract(id))
        else:
            print('Falhou')

etl = ETL()
print('\n\nConsumo da API Pokemon')
print(40 * '*')
etl.consume(1, API_Pokemon())
etl.consume(2)

print('\n\nConsumo da API Rick and Morty')
print(40 * '*')
etl.consume2(1, API_Rick_Morty())
etl.consume2(2, API_Rick_Morty())

print('\n\nConsumo da API Star Wars')
print(40 * '*')
etl.consume3(1, API_Star_Wars())
etl.consume3(2, )

print('\n\nConsumo da API Crônicas do Gelo e do Fogo')
print(40 * '*')

etl.consume4(583, API_Ice_and_Fire())
etl.consume4(2, API_Ice_and_Fire())
