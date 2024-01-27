from project import interval, create_tab, create_scale, NOTES, FRETSTOT

def test_interval():
    assert interval('C', 'E') == 4
    assert interval('G#', 'D#') == 7
    assert interval('A', 'G') == 10

def test_create_scale():
    scale = create_scale('C', [2, 2, 1, 2, 2, 2, 1], NOTES, FRETSTOT)
    assert scale == ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']  # Check this against the expected result


def test_create_tab():
    tab_output = create_tab(['E', 'A', 'D', 'G', 'B', 'E'], FRETSTOT, ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'A', 'B', 'C', 'D'], NOTES)
    assert tab_output == [
        'E| 1 - 3 - 5 - 7',
        'B|',
        'G| - 2 - 4',
        'D| - 2 3 - 5 - 7 - 9',
        'A| - 2',
        'E| 1 - 3 - 5 - 7'
        ]