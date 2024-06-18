from dash import Dash, html, dcc
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
                   target='_blank')]),
        
        # add radio items
        # dcc.RadioItems(options, value)
        # options = list of unique values
        # happiness['region'].unique()
        dcc.RadioItems(options=happiness['region'].unique(), value='North America'),
        dcc.Checklist(options=happiness['region'].unique(), value='North America'),
        dcc.Dropdown(options=happiness['region'].unique(), value='North America'),
        dcc.Graph(figure=px.line(happiness[happiness['country']=='United States'],
                                 x='year', y='happiness_score',
                                 title='Happiness Scpre'))
        
           
 ])

if __name__ == '__main__':
    app.run_server(debug=True)