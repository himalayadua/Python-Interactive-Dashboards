from dash import Dash, html
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

app = Dash()

app.layout = html.Div([

    html.H1('My Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='http://worldhappiness.report',
                   target='_blank')])
 ])

if __name__ == '__main__':
    app.run_server(debug=True)