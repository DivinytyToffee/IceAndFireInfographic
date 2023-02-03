from collections import defaultdict

from collecting import Point
from utils import died_counter, is_born_after_year_ac, pov_characters, \
    make_bar_plot

if __name__ == '__main__':
    p = Point()
    p.run(True)

    characters = p.collections.get('characters')

    all_chars = defaultdict(int)
    born_after_170_ac = defaultdict(int)
    pov_char = defaultdict(int)
    culture_char = defaultdict(int)

    culture_set = []
    gender_set = []

    for x in characters.storage.values():
        died_counter(culture_char, x, 'culture')
        died_counter(all_chars, x, 'gender')
        is_born_after_year_ac(born_after_170_ac, x)
        pov_characters(pov_char, x)
        culture_set.append(x.culture)
        gender_set.append(x.gender)

    make_bar_plot(culture_char, set(culture_set), 'culture_dead', 'culture_dead_1_1')

    make_bar_plot(all_chars, set(gender_set), title='The ratio of the number of characters by \n'
                                                    ' gender and the ratio of their deaths', file_name='deid_alive')
    make_bar_plot(pov_char, set(gender_set), title='The ratio of the number of pov characters by \n'
                                                   ' gender and the ratio of their deaths', file_name='deid_alive_pov')
    make_bar_plot(born_after_170_ac, set(gender_set), title='The ratio of the number of characters by \n'
                                                            ' gender and the ratio of their deaths',
                  file_name='deid_alive_after_170')
