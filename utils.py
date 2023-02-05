import os
import re
from collections import defaultdict
from pathlib import Path
from typing import List, Tuple

import numpy as np
from matplotlib import pyplot as plt


def parse_url_elem(url: str, position: int = -1):
    return url.split('/')[position]


def bar_plot(x_data: List[str],
             y_data: List[List[int]],
             title: str = "",
             x_label: str = "",
             y_label: str = "",
             image_size:
             Tuple[int, int] = (1600, 100),
             ):

    px = 1 / plt.rcParams['figure.dpi']  # pixel in inches
    _, ax = plt.subplots(figsize=(image_size[0] * px, image_size[1] * px))

    for x, y in zip(x_data, y_data):
        ax.bar(x, y[0], color='b', align='center', width=0.4)
        ax.bar(x, y[1], color='r', align='center', width=0.4)

    ind = np.arange(len(x_data))

    plt.xticks(ind, x_data, rotation=90, fontsize=5)

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend(['All characters', 'Deid characters'])


def all_and_died_counter(collection: defaultdict, char, key: str):
    collection[key] += 1
    if char.died:
        collection[f'{key}_died'] += 1


def is_born_after_year_ac(collection: defaultdict, char, year: int = 170):
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
        all_and_died_counter(collection, char, char.gender)


def pov_characters(collection: defaultdict, char):
    """
    Function checks if the character was person of view in book chapters.

    :param collection:
    :param char:
    :return:
    """
    if char.povBooks:
        all_and_died_counter(collection, char, char.gender)


def prepare_bar_plot_data(collection: defaultdict, key_set: set, skip_unknown: bool = False):
    """
    Converting data for use in a bar plot.

    :param collection:
    :param key_set:
    :param skip_unknown:
    :return:
    """
    data = []
    fields = []
    for key in key_set:
        if key == '' or key is None:
            if skip_unknown:
                continue
            collection['Unknown'] = collection.pop(key)
            key = 'Unknown'
        fields.append(key)
        data.append([collection[key], collection[f'{key}_died']])

    return fields, data


def make_bar_plot(collection: defaultdict,
                  key_set: set,
                  title: str,
                  x_label: str,
                  y_label: str,
                  file_name: str,
                  skip_unknown: bool = False,
                  image_size: Tuple[int, int] = (1600, 100),
                  ):
    
    fields, data = prepare_bar_plot_data(collection, key_set, skip_unknown)
    print('+++++ Data prepared for drawing +++++')
    bar_plot(fields, data, title=title, x_label=x_label, y_label=y_label, image_size=image_size)

    cur_dir = os.getcwd()
    images = Path(os.path.join(cur_dir, 'images'))
    images.mkdir(parents=True, exist_ok=True)
    plt.savefig(os.path.join(images, f'{file_name}.png'), dpi=200)
    print('+++++ Polt is drew +++++')
