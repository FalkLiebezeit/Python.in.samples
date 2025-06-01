from bokeh.plotting import figure, show
from bokeh.io import output_notebook

output_notebook()  # Anzeige im Jupyter Notebook

p = figure(title="Bokeh Beispiel", x_axis_label="X-Werte", y_axis_label="Y-Werte")
p.line([1, 2, 3, 4, 5], [10, 20, 15, 30, 25], line_width=2)

show(p)