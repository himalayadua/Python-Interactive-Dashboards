from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

happiness = pd.read_csv('world_happiness.csv')

#create line graph variable
line_fig = px.line(happiness[happiness['country']=='United States'],
                                 x='year', y='happiness_score',
                                 title='Happiness Scpre')

app = Dash()

app.layout = html.Div([

    html.H1('My Dashboard'),
    html.P(['This dashboard shows the happiness score.',
            html.Br(),
            html.A('World Happiness Report Data Source',
                   href='http://worldhappiness.report',
                   target='_blank')]),

        
        dcc.Dropdown(id='country-dropdown', options=happiness['region'].unique(), value='United States'),
        
        # use the new variable
        dcc.Graph(id='happiness-graph', figure={})
        # figure is an empty map as this will get updated by the callback function below
 ])

#Decorator
@app.callback(
    Output(component_id='happiness-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value')
)
def update_graph(selected_country):
    filtered_happiness = happiness[happiness['country']==selected_country]
    line_fig= px.line(filtered_happiness,
                      x='year',
                      y='happiness_score',
                      title=f'Happiness Score in {selected_country}')
    
    return line_fig


if __name__ == '__main__':
    app.run_server(debug=True)