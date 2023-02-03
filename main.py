from collections import defaultdict

from collecting import Point
from utils import gender_died_counter, is_born_after_year_ac, pov_characters, \
    make_gender_died_ratio_plot

if __name__ == '__main__':
    p = Point()
    p.run(True)

    characters = p.collections.get('characters')

    all_chars = defaultdict(int)
    born_after_170_ac = defaultdict(int)
    pov_char = defaultdict(int)

    for x in characters.storage.values():
        gender_died_counter(all_chars, x)
        is_born_after_year_ac(born_after_170_ac, x)
        pov_characters(pov_char, x)

    make_gender_died_ratio_plot(all_chars, title='The ratio of the number of characters by \n'
                                                 ' gender and the ratio of their deaths', file_name='deid_alive')
    make_gender_died_ratio_plot(pov_char, title='The ratio of the number of pov characters by \n'
                                                ' gender and the ratio of their deaths', file_name='deid_alive_pov')
    make_gender_died_ratio_plot(born_after_170_ac, title='The ratio of the number of characters by \n'
                                                         ' gender and the ratio of their deaths',
                                file_name='deid_alive_after_170')
