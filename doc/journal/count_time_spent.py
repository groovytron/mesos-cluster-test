import sys
import re
import numpy as np
import matplotlib.pyplot as plt


def create_dict(filename):
    with open(filename) as f:
        time_regex = re.compile(r"\| \d+$")
        activity_regex = re.compile(
            r"^(?:Documentation|Test|Développement|Environnement de développement|Environnement de test|Étude de faisabilité)"
        )
        row_time = None
        doc_dic = dict()

        for i in range(2):
            f.readline()
        for line in f:
            row_time = time_regex.findall(line)
            row_activity = activity_regex.findall(line)
            if row_time != None and len(row_activity):
                row_activity = row_activity[0]
                row_time = int(row_time[0][2:])
                if doc_dic.get(row_activity, None) != None:
                    doc_dic[row_activity] += row_time
                else:
                    doc_dic[row_activity] = row_time
            else:
                raise NameError(
                    'Missing time or activity in the following line: ', line)
        return doc_dic


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("falsy call")
    else:
        activity_histo = create_dict(sys.argv[1])
        print(activity_histo)
        total_minutes = sum(activity_histo.values())
        minutes = total_minutes % 60
        hours = int(total_minutes / 60)
        print("Time spent:", hours, "hours and", minutes, "minutes")

        n_groups = len(activity_histo.keys())

        means_times = [t / 60 for t in activity_histo.values()]

        fig, ax = plt.subplots()

        index = np.arange(n_groups)
        bar_width = 0.35

        opacity = 0.4
        error_config = {'ecolor': '0.3'}

        rects = plt.bar(
            index,
            means_times,
            bar_width,
            alpha=opacity,
            color='b',
            error_kw=error_config,
            label="Julien M'Poy")

        plt.xlabel("Type d'activité")
        plt.ylabel('Temps passé (en heures)')
        plt.title("Vue d'ensemble du temps consacré au projet")
        plt.xticks(index + bar_width / 2, tuple(activity_histo.keys()))
        plt.legend()
        figure = plt.gcf()
        figure.set_size_inches(17.5, 10.5)
        figure.savefig('time_histogram.png', dpi=100)
