
import plotly.express as px
from .basic_chart import BasicChart
import pandas as pd


class ScatterChart(BasicChart):

    def __init__(self, data, **parameters):
        super().__init__()
        self.abscisse = parameters["abscisse"]
        self.ordonne = parameters["ordonne"]
        self.set_data(data)

    def render_chart(self):
        tempdata = self.data[self.data[self.abscisse] < 100]
        df = pd.DataFrame({self.abscisse: tempdata[self.abscisse].unique(),
                   self.ordonne: tempdata.groupby(self.abscisse)[self.ordonne].mean()})

        print(df,type(df))
        print(df.keys())
        fig = px.scatter(x=df[self.abscisse], y=df[self.ordonne],title="Moyenne de la gravité des accidents en fonction de l'age")
        return fig