import plotly.graph_objects as go
from .basic_chart import BasicChart


class BarChart(BasicChart):

    def __init__(self, data, **parameters):
        super().__init__()
        self.femme = list()
        self.homme = list()
        self.sexe = None
        self.years = None
        self.column = parameters["column"]
        self.chosedYear = parameters["chosedYear"]
        self.set_data(data)

    def render_chart(self):
        if len(self.chosedYear) != 0:
            return self.chartSelectedYear()            
        return self.chartAll()

    def chartAll(self):
        self.sexe = self.data[self.column].unique()
        self.years = self.data["an"].unique()
        for i in self.sexe:
            for j in self.years:
                tempdata = self.data[self.data['an'] == j]
                self.femme.append(tempdata.loc[tempdata[self.column] == "femme", 'sexe'].sum()/2)
                self.homme.append(tempdata.loc[tempdata[self.column] == "homme", 'sexe'].sum())
                self.homme[len(self.homme) - 1] -= self.femme[len(self.femme) - 1]

        fig = go.Figure(data=[
            go.Bar(name='homme', x=self.years, y=self.homme),
            go.Bar(name='femme', x=self.years, y=self.femme)
        ])
        fig.update_layout(barmode='group', title_text='Répartition femme/homme de chaque année')
        return fig

    def chartSelectedYear(self):
        self.sexe = self.data[self.column].unique()
        for i in self.sexe:
            for j in self.chosedYear:
                tempdata = self.data[self.data['an'] == j]
                self.femme.append(tempdata.loc[tempdata[self.column] == "femme", 'sexe'].sum()/2)
                self.homme.append(tempdata.loc[tempdata[self.column] == "homme", 'sexe'].sum())
                self.homme[len(self.homme) - 1] -= self.femme[len(self.femme) - 1]

        fig = go.Figure(data=[
            go.Bar(name='Garçon', x=self.chosedYear, y=self.homme),
            go.Bar(name='femme', x=self.chosedYear, y=self.femme)
        ])
        fig.update_layout(barmode='group', title_text='Répartition femme/homme de chaque formation')
        return fig
