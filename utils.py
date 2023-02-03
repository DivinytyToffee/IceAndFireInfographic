import re

import numpy as np
from matplotlib import pyplot as plt


def parse_url_elem(url: str, position: int = -1):
    return url.split('/')[position]


def barplot(x_data, y_data, title=""):
    _, ax = plt.subplots()
    ax.bar(x_data[0], y_data[0][0], color='#539caf', align='center', width=0.4, label=f'{x_data[0]} characters')
    ax.bar(x_data[1], y_data[0][1], color='#530caf', align='center', width=0.4, label=f'{x_data[1]} characters')
    ax.bar(x_data[0], y_data[1][0], color='#000', align='center', width=0.3, label=f'{x_data[0]} died characters')
    ax.bar(x_data[1], y_data[1][1], color='#050', align='center', width=0.3, label=f'{x_data[1]} died characters')

    ind = np.arange(2)

    plt.xticks(ind, x_data)

    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    ax.set_title(title)
    ax.legend()


def gender_died_counter(collection, char):
    collection[char.gender] += 1
    if char.died:
        collection[f'{char.gender}_died'] += 1


def prepare_bar_plot_data(collection):
    return (collection.get('Female'), collection.get('Male')), \
           (collection.get('Female_died'), collection.get('Male_died'))


def is_born_after_year_ac(collection, char, year=170):
    """
    Function checks date of born characters.

    :param collection:
    :param char:
    :param year:
    :return:
    """
    if 'AC' not in char.born:
        return

    born_year = min(int(s) for s in re.findall(r'\d+', char.born))
    if born_year > year:
        gender_died_counter(collection, char)


def pov_characters(collection, char):
    """
    Function checks if the character was person of view in book chapters.

    :param collection:
    :param char:
    :return:
    """
    if char.povBooks:
        gender_died_counter(collection, char)
