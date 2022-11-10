import plotly.graph_objects as go
import plotly.io as pio

pio.templates["custom"] = pio.templates["plotly_white"]

pio.templates['custom']['layout']['paper_bgcolor'] = 'rgba(0,0,0,0)'
pio.templates['custom']['layout']['plot_bgcolor'] = 'rgba(0,0,0,0)'
pio.templates['custom']['layout']['coloraxis']['showscale'] = False
pio.templates['custom']['layout']['title']['x'] = 0.5
pio.templates['custom']['layout']['title']['font']['size'] = 18
pio.templates['custom']['layout']['title']['font']['family'] = "'Open Sans', sans-serif"
pio.templates['custom']['layout']['title']['font']['color'] = 'rgb(100, 100, 100)'
pio.templates['custom']['layout']['font']['size'] = 14
pio.templates['custom']['layout']['font']['family'] = "'Open Sans', sans-serif"
pio.templates['custom']['layout']['font']['color'] = 'rgb(100, 100, 100)'
# pio.templates['custom']['layout']['bargap'] = 0
pio.templates['custom']['layout']['margin'] = {'b': 10, 'l': 0, 'r': 0}
pio.templates['custom']['layout']['xaxis']['visible'] = False

if __name__ == "__main__":
    print(pio.templates['custom'])
