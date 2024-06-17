from dash import Dash, html, dcc, Input, Output

app = Dash()

app.layout = html.Div([
    dcc.Input(id='input_text', value='change this text', type='text'),
    html.Div(children='', id='output_text')
])

#Decorator
@app.callback(
    Output(component_id='output_text', component_property='children'),
    Input(component_id='input_text', component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'
