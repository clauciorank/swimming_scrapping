from os.path import split

import pandas as pd


class TreatText:
    def __init__(self, file):
        self.text = open(file, 'r').read()
        self.text = self.text.replace('C;M;P', 'C M P')
        self.text = self.text.replace('C;M. P', 'C M P')
        self.text = self.text.split('\n')

    def treat_text(self):
        text = self.remove_empty_lines(self.text)
        text = self.remove_trash_lines(text)

        races_and_categories = self.return_races_and_categories(text)

        races = self.extract_races(text, races_and_categories['race'])

        treat_races = [self.treat_race(x) for x in races]

        df = pd.concat(treat_races)

        return df

    @staticmethod
    def treat_race(race):
        lines = []
        faixa = ''
        for i in race:
            if i[0:5] == 'FAIXA':
                faixa = i
            if 'PROVA' not in i[0:10] and i[0:5] != 'FAIXA':
                sp = i.split(';')
                if len(sp[0]) <= 3:
                    sp.pop(0)
                if sp[0].isdigit() and int(sp[0]) > 100:
                    sp[1] = sp[0] + ' ' + sp[1]
                    sp.pop(0)

                if len(sp) > 5:
                    sp = sp[:5]

                while len(sp) < 5:
                    sp.append('')

                sp.append(faixa)
                sp.append(race[0])
                lines.append(sp)

        return pd.DataFrame(lines)

    @staticmethod
    def extract_races(text, races_index):
        races = []

        for i in range(len(races_index)-1):
            r = text[races_index[i]:races_index[i+1]]
            races.append(r)

        return races

    def return_races_and_categories(self, text):
        race = []
        categories = []
        for n, i in enumerate(text):
            if 'PROVA' in self.split_line(i)[0]:
                race.append(n)
            if 'FAIXA' in self.split_line(i)[0]:
                categories.append(n)

        race.append(len(text))
        categories.append(len(text))

        return {
            'race': race,
            'categories': categories
        }

    @staticmethod
    def split_line(line):
        return line.split(',')

    @staticmethod
    def remove_trash_lines(text):
        text = [line for line in text if not line[0:3] == 'COL']

        return text

    @staticmethod
    def remove_empty_lines(text):
        text = [line for line in text if line.strip()]

        return text
