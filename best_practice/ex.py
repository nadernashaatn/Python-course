from loguru import logger
import snoop


@logger.catch  # Add this to track errors
@snoop
def bad():
    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'})]
    for i in range(1, len(DATA)):
        if DATA[i][-1]['species'][0] == 'v':
            print(DATA[i][-1]['species'])

# @logger.catch # Add this to track errors


@snoop
def good():
    DATA = [('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, {'species': 'virginica'}),
            (5.1, 3.5, 1.4, 0.2, {'species': 'setosa'}),
            (5.7, 2.8, 4.1, 1.3, {'species': 'versicolor'}),
            (6.3, 2.9, 5.6, 1.8, {'species': 'virginica'}),
            (6.4, 3.2, 4.5, 1.5, {'species': 'versicolor'}),
            (4.7, 3.2, 1.3, 0.2, {'species': 'setosa'}),
            (7.0, 3.2, 4.7, 1.4, {'species': 'versicolor'}),
            (7.6, 3.0, 6.6, 2.1, {'species': 'virginica'}),
            (4.6, 3.1, 1.5, 0.2, {'species': 'setosa'})]
    header, *data = DATA
    for *measurements, species in data:
        species = species['species']
        if species.startswith('v'):
            print(species)


good()
bad()
