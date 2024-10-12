import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from .rack import Rack
from .units import Measurements


def rack_barchart(rack, ax=None, ylabel='[{number}]', numbers_inside=False):
    if not isinstance(rack, Rack):
        raise Exception(f'{rack_barchart} must be called with a {Rack} instance but it was called with {type(rack)}')
    if ax is None:
        ax = plt.gca()
    labels = [ylabel.format(brand=cam.brand, name=cam.name, number=cam.number) for cam in rack]
    minimums = [cam.min for cam in rack]
    maximums = [cam.max for cam in rack]
    ranges = [maximum - minimum for maximum, minimum in zip(maximums, minimums)]
    colors = [cam.color for cam in rack]
    bars = ax.barh(labels, width=ranges, left=minimums, height=.8, color=colors, alpha=0.7)

    for patch in reversed(bars):
        bb = patch.get_bbox()
        color = patch.get_facecolor()
        p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),
                                abs(bb.width), abs(bb.height),
                                boxstyle="round,pad=0,rounding_size=0.5",
                                ec="none", fc=color,
                                mutation_aspect=0.2
                                )
        patch.remove()
        ax.add_patch(p_bbox)

    if numbers_inside:
        numbers = [cam.number for cam in rack]
        ax.bar_label(bars, numbers, label_type='center', fontsize=5, weight='bold', color='white')
    return plt.gcf(), ax


def racks_barchart(racks, smart_ylabels=True, numbers_inside=True):
    if not isinstance(racks[0], Rack):
        raise Exception(f'{racks_barchart} must be called with a list of {Rack} but it was called with a list of {type(racks[0])}')
    sizes = [len(rack) for rack in racks]
    fig, axes = plt.subplots(nrows=len(racks), sharex=True,
                             gridspec_kw={'height_ratios': sizes, 'hspace': 0})
    axes = [axes] if len(racks) == 1 else axes

    for rack, ax in zip(racks, axes):
        rack_barchart(rack, ax, numbers_inside=numbers_inside)
        sep = '\n'
        ax.set_ylabel(f'{rack.name(sep)}')
        ax.spines.right.set_visible(False)
        ax.spines.left.set_visible(False)
        ax.spines.top.set_visible(False)
        ax.tick_params(length=0)
        ax.xaxis.grid()
        ax.set_axisbelow(True)
        if smart_ylabels:
            ax.set_yticklabels([])
            ax.set_ylabel(f'{rack.name(sep)}', rotation=0, horizontalalignment='right', verticalalignment='center')
    fig.tight_layout()
    return fig, axes


def scatter_average(racks, xvalue, yvalue, ax=None):
    if not ax:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()
    for rack in racks:
        ax.plot([getattr(rack, xvalue)], [getattr(rack, yvalue)],
                label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
        ax.legend()
    ax.set_xlabel(f'{xvalue.replace("_", " ").capitalize()} [{Measurements.get_label(xvalue)}]')
    ax.set_ylabel(f'{yvalue.replace("_", " ").capitalize()} [{Measurements.get_label(yvalue)}]')
    fig.tight_layout()
    return fig, ax


def scatter_individual(racks, xvalue, yvalue, ax=None):
    if not ax:
        fig, ax = plt.subplots()
    else:
        fig = ax.get_figure()
    for rack in racks:
        x = [getattr(i, xvalue) for i in rack]
        y = [getattr(i, yvalue) for i in rack]
        ax.plot(x, y, label=rack.name(), marker='o', markersize=10, linewidth=0, alpha=.7)
        ax.legend()
    ax.set_xlabel(f'{xvalue.replace("_", " ").capitalize()} [{Measurements.get_label(xvalue)}]')
    ax.set_ylabel(f'{yvalue.replace("_", " ").capitalize()} [{Measurements.get_label(yvalue)}]')
    fig.tight_layout()
    return fig, ax
