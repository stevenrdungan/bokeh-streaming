from datetime import datetime, timedelta
import pandas as pd
from bokeh.plotting import curdoc, figure
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.driving import count


source = ColumnDataSource(dict(cutoff=[],
                               d_ct=[],
                               d_avg=[],
                               d_min=[],
                               d_max=[]))

p = figure(title='Streaming Example',
           x_axis_label='timestamp',
           y_axis_label='value',
           x_axis_type='datetime')
p.toolbar.logo = None
p.toolbar_location = None
p.min_border_left = 50
p.min_border_bottom = 50

# formatting dt display is work in progress - poor docs and few examples
p.xaxis.formatter=DatetimeTickFormatter(hours='%H:%M:%S',
                                        minutes='%H:%M:%S',
                                        seconds='%H:%M:%S')

l1 = p.line(x='cutoff', y='d_ct', color='red', line_width=1, source=source)
l2 = p.line(x='cutoff', y='d_avg', color='blue', line_width=3, source=source)
l3 = p.line(x='cutoff', y='d_min', color='purple', line_width=3, source=source)
l4 = p.line(x='cutoff', y='d_max', color='green', line_width=3, source=source)

legend = Legend(items=[
    ('count', [l1]),
    ('avg', [l2]),
    ('min', [l3]),
    ('max', [l4])
    ], location=(5, -10))
p.add_layout(legend, 'right')


def _get_data(dt):
    cutoff = dt - timedelta(seconds=10)
    data = pd.read_csv("output.txt", header=None, names=['timestamp', 'value'])
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    new_data = data[data['timestamp'] >= cutoff]
    d_ct = len(new_data)
    d_avg = new_data['value'].mean()
    d_min = new_data['value'].min()
    d_max = new_data['value'].max()
    return cutoff, d_ct, d_avg, d_min, d_max


@count() # decorator required to perform callback function on interval
def update(t):
    cutoff, d_ct, d_avg, d_min, d_max = _get_data(datetime.utcnow())
    new_data = dict(cutoff=[cutoff],
                    d_ct=[d_ct],
                    d_avg=[d_avg],
                    d_min=[d_min],
                    d_max=[d_max]) # this data is appended to our source data
    source.stream(new_data=new_data, rollover=20) # keep up to last 20 results


curdoc().add_root(p)
curdoc().add_periodic_callback(update, 1000) # update data every second
