import pytest

from code_one.game_treefive import (
    multiple_of, robot, multiple_of_5, multiple_of_3, three_five
)

@pytest.mark.parametrize('base, number, expected', [
    (3, 6, True), (2, 6, True), (4, 6, False), (5, 5, True), (5, 10, True), (5, 9, False)
])
def test_multiple_of(base, number, expected):
    assert multiple_of(base, number) == expected


@pytest.mark.parametrize('number, expected', [
    (3, True), (4, False), (17, False), (90, True), (99, True), (36, True)
])
def test_multiple_of_3(number, expected):
    assert multiple_of_3(number) == expected


@pytest.mark.parametrize('number, expected', [
    (5, True), (4, False), (15, True), (20, True), (22, False), (75, True)
])
def test_multiple_of_5(number, expected):
    assert multiple_of_5(number) == expected


@pytest.mark.parametrize('number, expected', [
    (1, '1'), (2, '2'), (3, 'Three'), (5, 'Five'), (7, '7'), (9, 'Three'), (12, 'Three'),
    (15, 'ThreeFive'), (27, 'Three'), (30, 'ThreeFive'), (90, 'ThreeFive'), (94, '94')
])
def test_robot(number, expected):
    assert robot(number) == expected


@pytest.mark.parametrize('total_three, total_five, total_threefive', [
    (27, 14, 6)
])
def test_three_five(capfd, total_three, total_five, total_threefive):
    three_five()
    out, err = capfd.readouterr()
    output = out.split('\n')
    assert output.count('Three') == total_three
    assert output.count('Five') == total_five
    assert output.count('ThreeFive') == total_threefive

