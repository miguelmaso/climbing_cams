import climbing_cams as cams
from matplotlib import figure, axes


def test_rack_barh():
    rack = cams.db.select(name="C4")
    fig, ax = rack.barh()
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)


def test_racks_barh():
    racks = cams.db.select_many([{'name': 'C4'}, {'name': 'UL'}])
    assert len(racks) == 2
    fig, ax = racks.barh()
    assert isinstance(fig, figure.Figure)
    assert len(ax) == 2


def test_racks_scatter_individual():
    racks = cams.db.select_many([{'name': 'C4'}, {'name': 'UL'}])
    fig, ax = racks.scatter('avg', 'weight', individual=True)
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)
    assert len(ax.lines) == 2
    line_c4 = ax.lines[0]
    assert len(line_c4.get_data()[0]) == 10
    line_ul = ax.lines[1]
    assert len(line_ul.get_data()[0]) == 7


def test_racks_scatter_average():
    racks = cams.db.select_many([{'name': 'C4'}, {'name': 'UL'}])
    assert len(racks) == 2
    fig, ax = racks.scatter('avg', 'weight')
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)
    assert len(ax.lines) == 2
    line_c4 = ax.lines[0]
    assert len(line_c4.get_data()[0]) == 1
    line_ul = ax.lines[1]
    assert len(line_ul.get_data()[0]) == 1


def test_rack_weight_range():
    rack = cams.db.select(name="C4")
    fig, ax = rack.weight_range()
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)


def test_racks_weight_range():
    racks = cams.db.select_many([{'name': 'C4'}, {'name': 'UL'}])
    fig, ax = racks.weight_range()
    assert isinstance(fig, figure.Figure)
    assert isinstance(ax, axes.Axes)
    assert len(ax.collections) == 2
