import pandas as pd

class users:
    def __init__(self):
        self.name = ''
    def getData(self, filename):
        """

        :param filename:
        :return:
        """
        df = pd.read_csv(filename)

        for index in range(len(df['Patient Email Address'])):
            if df['Patient Email Address'][index] == '-':
                df = df.drop(index)

        for index in range(len(df['Patient Name'])):
            name = df['Patient Name'][index]
            name = name.split(', ')
            df['Patient Name'][index] = name[1]

        self.data = pd.DataFrame()
        self.data['name'] = df['Patient Name']
        self.data['email'] = df['Patient Email Address']

        return self.data
