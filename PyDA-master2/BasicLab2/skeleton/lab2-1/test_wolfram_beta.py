import pytest
from wolfram_beta import (print_term, print_equation, parse_term,
                         parse_equation, d_dx_as_terms, d_dx,
                         integral_as_terms, integral, compute_as_terms,
                         compute, solve_query)

def test_solve_query():
    assert solve_query("D,0x^2 + -x + 5") == "0x + -1"
    assert solve_query("I,2x + -1,5") == "1x^2 + -1x + 5"
    assert solve_query("C,2x + -1,5") == "9"

def test_compute():
    assert compute("2x + -1", 5) == "9"
    assert compute("1x^2 + -3x + 5", 3) == "5"

def test_compute_as_terms():
    assert compute_as_terms({1:2, 0:-1}, 5) == 9
    assert compute_as_terms({0: 5, 1: -3, 2: 1}, 3) == 5

def test_integral():
    assert integral("2x + -1", 5) == "1x^2 + -1x + 5" 

def test_integral_as_terms():
    assert integral_as_terms({1:0, 0:-1}, 5) == {2:0, 1:-1, 0:5}
    assert integral_as_terms({0:-1, 1:0}, 5) == {2:0, 1:-1, 0:5}
    assert integral_as_terms({0:-1, 1:0}, 5) == {1:-1, 2:0, 0:5}
    assert integral_as_terms({}, 5) == {0:5}
    assert integral_as_terms({}, 0) == {0:0}

def test_d_dx():
    assert d_dx("0x^2 + -x + 5") == "0x + -1"

def test_d_dx_as_terms():
    assert d_dx_as_terms({2:0, 1:-1, 0:5}) == {1:0, 0:-1}
    assert d_dx_as_terms({1:-1, 2:0, 0:5}) == {0:-1, 1:0}
    assert d_dx_as_terms({0:0}) == {0:0}
    assert d_dx_as_terms({0:5}) == {0:0}

def test_parse_equation():
    assert parse_equation("-x + 5 + 0x^2") == {2:0, 1:-1, 0:5}
    assert parse_equation("0x^2 + -x + 5") == {2:0, 1:-1, 0:5}
    assert parse_equation("5 + -x + 0x^2") == {2:0, 1:-1, 0:5}

def test_parse_term():
    assert parse_term('0x^2') == (2,0)
    assert parse_term('-x') == (1,-1)
    assert parse_term('5') == (0,5)

def test_print_equation():
    assert print_equation({2:0, 1:-1, 0:5}) == "0x^2 + -1x + 5"

def test_print_term():
    assert print_term(2, 0) == '0x^2'
    assert print_term(1, -1) == '-1x'
    assert print_term(0, 5) == '5'
