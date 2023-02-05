from collections import defaultdict

from collecting import CollectionsLoader
from utils import all_and_died_counter, is_born_after_year_ac, pov_characters, \
    make_bar_plot

if __name__ == '__main__':
    cl = CollectionsLoader()
    cl.run(True)

    characters = cl.collections.get('characters')
    houses = cl.collections.get('houses')

    all_chars = defaultdict(int)
    born_after_170_ac = defaultdict(int)
    pov_char = defaultdict(int)
    culture_char = defaultdict(int)
    houses_chars = defaultdict(int)

    culture_set = []
    gender_set = []
    house_set = []

    for h in houses.storage.values():
        if h.swornMembers:
            for member_id in h.swornMembers:
                member = characters.get(member_id)
                all_and_died_counter(houses_chars, member, h.name)
            house_set.append(h.name)

    print('Making plot for ratio of the dead and alive characters in each house.')
    make_bar_plot(
        houses_chars,
        set(house_set),
        title='The ratio of the dead and alive characters in each house.',
        file_name='house_dead',
        x_label='House',
        y_label='Count',
        skip_unknown=True,
        image_size=(3200, 3000)
    )

    for x in characters.storage.values():
        all_and_died_counter(culture_char, x, x.culture)
        all_and_died_counter(all_chars, x, x.gender)
        is_born_after_year_ac(born_after_170_ac, x)
        pov_characters(pov_char, x)
        culture_set.append(x.culture)
        gender_set.append(x.gender)

    print('Making plot for ratio of the dead and alive characters in each culture in a World of Ice and Fire.')
    make_bar_plot(
        culture_char,
        set(culture_set),
        title='The ratio of the dead and alive characters in each culture in a World of Ice and Fire.',
        file_name='culture_dead',
        x_label='Culture',
        y_label='Count',
        skip_unknown=True
    )

    print('Making plot for ratio of the dead and alive characters by gender')
    make_bar_plot(
        all_chars,
        set(gender_set),
        title='The ratio of the number of characters by \n'
              ' gender and the ratio of their deaths',
        file_name='deid_alive',
        x_label='Gender',
        y_label='Count',
    )

    print('Making plot for ratio of the dead and alive PoV characters by gender')
    make_bar_plot(
        pov_char,
        set(gender_set),
        title='The ratio of the number of pov characters by \n'
              ' gender and the ratio of their deaths',
        file_name='deid_alive_pov',
        x_label='Gender',
        y_label='Count',
    )

    print('Making plot for ratio of the dead and alive characters by gender born after 170 AC')
    make_bar_plot(
        born_after_170_ac,
        set(gender_set),
        title='The ratio of the number of characters by \n'
              ' gender and the ratio of their deaths',
        file_name='deid_alive_after_170',
        x_label='Gender',
        y_label='Count'
    )
