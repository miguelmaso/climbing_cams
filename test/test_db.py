import climbing_cams as cams


def test_select():
    rack = cams.db.select(brand='BD', name='UL')
    assert len(rack) == 7


def test_select_range():
    rack = cams.db.select(brand='BD', name='UL', range=[30, 120])
    assert len(rack) == 4
