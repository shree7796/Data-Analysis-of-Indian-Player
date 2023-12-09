import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from dash import dash_table
from utils import *


app = dash.Dash(__name__)

# Sample image URLs and names
image_data = [
    {'url': 'https://static.indiatvnews.com/ins-web/images/kohli-profile-1540274232.jpg', 'name': 'Virat Kohli', 'link': '/virat'},
    {'url': 'https://static.javatpoint.com/biography/images/rohit-sharma.png', 'name': 'Rohit Sharma', 'link': '/rohit'},
    {'url': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/322600/322697.png', 'name': 'Shubman Gill', 'link': '/gill'},
    {'url': 'https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/323000/323035.png', 'name': 'Shreyas iyer', 'link': '/shreyas'},
    {'url': 'https://img1.hscicdn.com/image/upload/f_auto/lsci/db/PICTURES/CMS/304200/304207.png', 'name': 'Kl Rahul', 'link': '/kl_rahul'},
    {'url': 'https://images.cricket.com/players/11803_headshot_safari.png', 'name': 'SKY', 'link': '/sky'},
    {'url': 'https://resources.pulse.icc-cricket.com/players/210/2740.png', 'name': 'Hardik', 'link': '/hardik'},
    {'url': 'https://images.cricket.com/players/3850_headshot_safari.png', 'name': 'Jadeja', 'link': '/jadeja'},
    {'url': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrxlP0B_hx2R6SshUPLwR74POgeewCXpeekZHUG_Sd4Q&s', 'name': 'Shami', 'link': '/shami'},
    {'url': 'https://img1.hscicdn.com/image/upload/f_auto/lsci/db/PICTURES/CMS/356800/356849.1.png', 'name': 'Jasprit', 'link': '/jasprit'},
    {'url': 'https://m.cricbuzz.com/a/img/v1/192x192/i1/c352490/kuldeep-yadav.jpg', 'name': 'Kuldeep', 'link': '/kuldeep'},
    # Add more image data as needed
]


# Function to create a clickable image box
def create_image_box(image_info):
    return dcc.Link(
        [
            html.Div([
                html.Img(src=image_info['url'], alt=image_info['name']),
                html.Div(image_info['name'],  style={'width': '100px', 'height': '100px'})
            ], style={'border': '1px solid #ccc', 'padding': '10px'}),
        ],
        href=image_info['link']
    )


# Create a list of clickable image boxes
image_boxes = [create_image_box(image) for image in image_data]
# App layout of the home page
home_layout = html.Div([
    html.H1('Indian Cricket Team Analysis',style={"background-color": "skyblue"}),
    html.P("Welcome to the home page of Indian Cricket Team. All of the information about Indian players and their performances can be found here.", style={"font-style": "oblique"}),

    html.Div([
        html.Div([
            html.A(
                [
                    html.Img(src=image_info['url'], alt=image_info['name']),
                    html.Div(image_info['name'], style={'textAlign': 'center'})
                ],
                href=image_info['link'],
            )
        ], style={'display': 'inline-block', 'margin': '10px'})
        for image_info in image_data
    ]),

])


# App layout of Virat Page
virat_layout = html.Div([
    html.Img(src='https://rapidkings.com/wp-content/uploads/2023/05/17kohli1-1024x928.jpg', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Virat Kohli', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=virat_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(virat_dataframe(), x='Ground', y=['Runs', '4s', '6s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(virat_dataframe(), x='Ground', y=['Runs', '4s', '6s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),

])

# App layout of Rohit Page
rohit_layout = html.Div([
    html.Img(src='https://static.javatpoint.com/biography/images/rohit-sharma.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Rohit Sharma', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=rohit_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(rohit_dataframe(), x='Years', y=['Runs', '4s', '6s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(rohit_dataframe(), x='Years', y=['Runs', '4s', '6s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),

])

# App layout of KL Rahul Page
kl_layout = html.Div([
    html.Img(src='https://img1.hscicdn.com/image/upload/f_auto/lsci/db/PICTURES/CMS/304200/304207.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='KL Rahul', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=kl_rahul_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(kl_rahul_dataframe(), x='Year', y=['Runs', '100s', '50s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(kl_rahul_dataframe(), x='Year', y=['Runs', '100s', '50s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),

])

# App layout of Gill Page
gill_layout = html.Div([
    html.Img(src='https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/322600/322697.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='KL Rahul', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=shubhman_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(shubhman_dataframe(), x='Year', y=['Runs', '100s', '50s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(shubhman_dataframe(), x='Year', y=['Runs', '100s', '50s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),

])

# App layout of Shreyas Page
shreyas_layout = html.Div([
    html.Img(src='https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_320,q_50/lsci/db/PICTURES/CMS/323000/323035.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Shreyas Iyar', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=shreyas_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(shreyas_data_dataframe(), x='Year', y=['Runs', '100s', '50s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(shreyas_data_dataframe(), x='Year', y=['Runs', '100s', '50s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])

# App layout of SKY Page
sky_layout = html.Div([
    html.Img(src='https://images.cricket.com/players/11803_headshot_safari.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Suryakumar Yadav', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=sky_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(sky_data_dataframe(), x='Year', y=['Runs', '100s', '50s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(sky_data_dataframe(), x='Year', y=['Runs', '100s', '50s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])


# App layout of Hardik Page
hardik_layout = html.Div([
    html.Img(src='https://resources.pulse.icc-cricket.com/players/210/2740.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Hardik Pandya', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=hardik_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(hardik_data_dataframe(), x='Year', y=['Runs', '100s', '50s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(hardik_data_dataframe(), x='Year', y=['Runs', '100s', '50s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])


# App layout of Jadeja Page
jadeja_layout = html.Div([
    html.Img(src='https://images.cricket.com/players/3850_headshot_safari.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Ravindra Jadeja', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=jadeja_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(jadeja_data_dataframe(), x='Year', y=['Runs', '100s', '50s'], barmode='group')),
    #
    # Line Chart
    dcc.Graph(figure=px.line(jadeja_data_dataframe(), x='Year', y=['Runs', '100s', '50s'])),
    #
    # # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])


# App layout of Shami Page
shami_layout = html.Div([
    html.Img(src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrxlP0B_hx2R6SshUPLwR74POgeewCXpeekZHUG_Sd4Q&s', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Md Shami', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=shami_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(shami_data_dataframe(), x='Year', y=['Runs', 'shami_wickets', 'shami_4wickets'], barmode='group')),

    # # Line Chart
    # dcc.Graph(figure=px.line(shami_data_dataframe, x='Year', y=['Runs', 'shami_wickets', 'shami_4wickets'])),
    #
    # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])


# App layout of Jasprit Page
jasprit_layout = html.Div([
    html.Img(src='https://img1.hscicdn.com/image/upload/f_auto/lsci/db/PICTURES/CMS/356800/356849.1.png', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Jasprit Bumrah', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=jasprit_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(jasprit_data_dataframe(), x='Year', y=['Runs', 'jasprit_wickets', 'jasprit_4wickets'], barmode='group')),

    # # Line Chart
    # dcc.Graph(figure=px.line(shami_data_dataframe, x='Year', y=['Runs', 'shami_wickets', 'shami_4wickets'])),
    #
    # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])

# App layout of Kuldeep Page
kuldeep_layout = html.Div([
    html.Img(src='https://m.cricbuzz.com/a/img/v1/192x192/i1/c352490/kuldeep-yadav.jpg', style={'width': '100px', 'height': '100px'}),
    html.Div(children='Kuldeep Yadav', style={'fontSize': 24, 'color': 'blue', 'fontFamily': 'Arial'}),

    # DataTable
    dash_table.DataTable(data=kuldeep_data_dataframe().to_dict('records'), page_size=30),

    # Bar Chart
    dcc.Graph(figure=px.bar(kuldeep_data_dataframe(), x='Year', y=['Runs', 'kuldeep_wickets', 'kuldeep_4wickets'], barmode='group')),

    # # Line Chart
    # dcc.Graph(figure=px.line(shami_data_dataframe, x='Year', y=['Runs', 'shami_wickets', 'shami_4wickets'])),
    #
    # Scatter Plot
    # dcc.Graph(figure=px.scatter(df, x='Start Date', y=['Runs', '4s', '6s'])),
])


# Define the main layout with dcc.Location and a callback to update the page content
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Callback to update the page content based on the URL
@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/virat':
        return virat_layout
    elif pathname == '/rohit':
        return rohit_layout
    elif pathname == '/kl_rahul':
        return kl_layout
    elif pathname == '/gill':
        return gill_layout
    elif pathname == '/shreyas':
        return shreyas_layout
    elif pathname == '/sky':
        return sky_layout
    elif pathname == '/hardik':
        return hardik_layout
    elif pathname == '/jadeja':
        return jadeja_layout
    elif pathname == '/shami':
        return shami_layout
    elif pathname == '/jasprit':
        return jasprit_layout
    elif pathname == '/kuldeep':
        return kuldeep_layout
    else:
        return home_layout


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
