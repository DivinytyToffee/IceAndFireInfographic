import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


from collecting import Point


def barplot(x_data, y_data, error_data, x_label="", y_label="", title=""):
    _, ax = plt.subplots()
    # Draw bars, position them in the center of the tick mark on the x-axis
    ax.bar(x_data[0], y_data[0], color = '#539caf', align = 'center')
    ax.bar(x_data[1], y_data[1], color = '#000', align = 'edge')
    # Draw error bars to show standard deviation, set ls to 'none'
    # to remove line betwee1n points
    # ax.errorbar(x_data,y_data, yerr = error_data, color = '#297083', ls = 'none', lw = 2, capthick = 2)
    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)
    ax.set_title(title)


if __name__ == '__main__':
    p = Point()
    p.run(True)
    characters = p.collections.get('characters')
    genders = set()
    genders_count = {}
    female = 0
    female_died = 0
    male = 0
    male_died = 0
    for x in characters.storage.values():
        if x.gender == 'Female':
            female += 1
            if x.died:
                female_died += 1
        elif x.gender == 'Male':
            male += 1
            if x.died:
                male_died += 1

    print(f"Female - {female}({female_died} - dead), Male - {male}({male_died} - dead)")

    barplot([['Female', 'Male'], ['Died Female', 'Died Male']], [[female, male], [female_died, male_died]], 1)

    plt.show()
