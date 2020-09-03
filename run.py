import papermill as pm


pm.execute_notebook(
    'main.ipynb',
    'output.ipynb',
    parameters=dict(name='ODDS', x=0.1, y=10)
)
