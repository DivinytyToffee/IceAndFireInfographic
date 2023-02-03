import os
import re
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


def parse_url_elem(url: str, position: int = -1):
    return url.split('/')[position]


def barplot(x_data, y_data, title="", x_label="", y_label=""):
    _, ax = plt.subplots()

    for x, y in zip(x_data, y_data):
        ax.bar(x, y[0], color='b', align='center', width=0.4, label=f'{x} characters')
        ax.bar(x, y[1], color='r', align='center', width=0.4, label=f'{x} died characters')

    ind = np.arange(len(x_data))

    plt.xticks(ind, x_data)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()


def died_counter(collection, char, attr):
    collection[getattr(char, attr)] += 1
    if char.died:
        collection[f'{getattr(char, attr)}_died'] += 1


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
        died_counter(collection, char, 'gender')


def pov_characters(collection, char):
    """
    Function checks if the character was person of view in book chapters.

    :param collection:
    :param char:
    :return:
    """
    if char.povBooks:
        died_counter(collection, char, 'gender')


def prepare_bar_plot_data(collection, key_set):
    data = []
    fields = []
    for key in key_set:
        if key == '' or key is None:
            collection['Unknown'] = collection.pop(key)
            key = 'Unknown'
        fields.append(key)
        data.append([collection[key], collection[f'{key}_died']])

    return fields, data


def make_bar_plot(collection, key_set, title, x_label, y_label, file_name):
    fields, data = prepare_bar_plot_data(collection, key_set)
    barplot(fields, data, title=title, x_label=x_label, y_label=y_label)

    cur_dir = os.getcwd()
    images = Path(os.path.join(cur_dir, 'images'))
    images.mkdir(parents=True, exist_ok=True)
    plt.savefig(os.path.join(images, f'{file_name}.png'))