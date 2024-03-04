import matplotlib as mpl
mpl.use('WXAgg')
import matplotlib.backends.backend_wxagg as mwx
fig = mpl.figure.Figure()
canvas = mwx.FigureCanvasWxAgg(panel, -1, fig)
ax = fig.add_subplot(1, 1, 1)
ax.plot(...)
canvas.draw()