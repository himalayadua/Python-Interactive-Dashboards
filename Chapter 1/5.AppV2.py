from dash import Dash, html, dcc, Input, Output

app = Dash()


# removes id='input_text',
# using variables instead
input_text = dcc.Input(value='change this text', type='text'),
output_text = html.Div()

# add these variables in the html
app.layout = html.Div([input_text, output_text])


#Decorator
@app.callback(
    Output(component_id=output_text, component_property='children'),
    Input(component_id=input_text, component_property='value')
)
def update_output_div(input_text):
    return f'Text: {input_text}'


if __name__ == '__main__':
    app.run_server(debug=True)