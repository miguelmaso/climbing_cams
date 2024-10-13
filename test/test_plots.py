import climbing_cams as cams
from matplotlib import figure, axes
import pytest


def test_rack_bar_chart_fail():
    with pytest.raises(Exception) as e_info:
        cams.plots.rack_bar_chart(1)
    assert str(e_info.value) == f'{cams.plots.rack_bar_chart} must be called with a {cams.rack.Rack} ' + \
                                f'instance but it was called with {int}'


def test_racks_bar_chart_fail():
    with pytest.raises(Exception) as e_info:
        cams.plots.racks_bar_chart([1])
    assert str(e_info.value) == f'{cams.plots.racks_bar_chart} must be called with a list of {cams.rack.Rack} ' + \
                                f'but it was called with a list of {int}'


def test_rack_bar_chart():
    rack = cams.db.select(name="C4")
    fig, ax = cams.plots.rack_bar_chart(rack)
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)


def test_racks_bar_chart():
    racks = [cams.db.select(**spec) for spec in [{'name': 'C4'}, {'name': 'UL'}]]
    assert len(racks) == 2
    fig, ax = cams.plots.racks_bar_chart(racks)
    assert isinstance(fig, figure.Figure)
    assert len(ax) == 2


def test_scatter_individual():
    racks = [cams.db.select(**spec) for spec in [{'name': 'C4'}, {'name': 'UL'}]]
    fig, ax = cams.plots.scatter_individual(racks, 'avg', 'weight')
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)
    assert len(ax.lines) == 2
    line_c4 = ax.lines[0]
    assert len(line_c4.get_data()[0]) == 10
    line_ul = ax.lines[1]
    assert len(line_ul.get_data()[0]) == 7


def test_scatter_average():
    racks = [cams.db.select(**spec) for spec in [{'name': 'C4'}, {'name': 'UL'}]]
    assert len(racks) == 2
    fig, ax = cams.plots.scatter_average(racks, 'avg', 'weight')
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)
    assert len(ax.lines) == 2
    line_c4 = ax.lines[0]
    assert len(line_c4.get_data()[0]) == 1
    line_ul = ax.lines[1]
    assert len(line_ul.get_data()[0]) == 1
