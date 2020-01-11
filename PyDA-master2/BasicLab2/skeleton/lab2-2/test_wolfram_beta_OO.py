import pytest
from wolfram_beta_OO import Terms, WolframBeta

def test_solve_query():
    wb = WolframBeta('','')
    assert wb.solve_query("D,0x^2 + -x + 5") == "0x + -1"
    assert wb.solve_query("I,2x + -1,5") == "x^2 + -x + 5"
    assert wb.solve_query("C,2x + -1,5") == "9"

def test_compute():
    assert WolframBeta.compute("2x + -1", 5) == "9"
    assert WolframBeta.compute("1x^2 + -3x + 5", 3) == "5"

def test_compute_as_terms():
    terms = Terms()
    terms.terms_dict = {1:2, 0:-1}
    assert terms.compute_as_terms(5) == 9
    terms.terms_dict = {0: 5, 1: -3, 2: 1}
    assert terms.compute_as_terms(3) == 5

def test_integral():
    assert WolframBeta.integral("2x + -1", 5) == "x^2 + -x + 5" 

def test_integral_as_terms():
    terms = Terms()
    terms.terms_dict = {1:0, 0:-1}
    assert terms.integral_as_terms(5).terms_dict == {2:0, 1:-1, 0:5}
    terms.terms_dict = {0:-1, 1:0}
    assert terms.integral_as_terms(5).terms_dict == {2:0, 1:-1, 0:5}
    terms.terms_dict = {0:-1, 1:0}
    assert terms.integral_as_terms(5).terms_dict == {1:-1, 2:0, 0:5}
    terms.terms_dict = {}
    assert terms.integral_as_terms(5).terms_dict == {0:5}
    terms.terms_dict = {}
    assert terms.integral_as_terms(0).terms_dict == {0:0}

def test_d_dx():
    assert WolframBeta.d_dx("0x^2 + -x + 5") == "0x + -1"

def test_d_dx_as_terms():
    terms = Terms()
    terms.terms_dict = {2:0, 1:-1, 0:5}
    assert terms.d_dx_as_terms().terms_dict == {1:0, 0:-1}
    terms.terms_dict = {1:-1, 2:0, 0:5}
    assert terms.d_dx_as_terms().terms_dict == {0:-1, 1:0}
    terms.terms_dict = {0:0}
    assert terms.d_dx_as_terms().terms_dict == {0:0}
    terms.terms_dict = {0:5}
    assert terms.d_dx_as_terms().terms_dict == {0:0}

def test_parse_equation():
    # term1 = Terms("cos(x)")
    # assert term1.get_terms_dict() == {0:0}
    term1 = Terms("-x + 5 + 0x^2")
    assert term1.get_terms_dict() == {2:0, 1:-1, 0:5}
    term2 = Terms("0x^2 + -x + 5")
    assert term2.get_terms_dict() == {2:0, 1:-1, 0:5}
    term3 = Terms("5 + -x + 0x^2")
    assert term3.get_terms_dict() == {2:0, 1:-1, 0:5}
    term4 = Terms("0")
    assert term4.get_terms_dict() == {0:0}

def test_parse_term():
    # assert Terms.parse_term('cos(x)') == (0,0)
    assert Terms.parse_term('0x^2') == (2,0)
    assert Terms.parse_term('-x') == (1,-1)
    assert Terms.parse_term('x') == (1,1)
    assert Terms.parse_term('5') == (0,5)
    assert Terms.parse_term('0') == (0,0)

def test_print_equation():
    term1 = Terms("0x^2 + -x + 5")
    assert term1.print_equation() == "0x^2 + -x + 5"
    term2 = Terms("0")
    assert term2.print_equation() == "0"

def test_print_term():
    assert Terms.print_term(2, 0) == '0x^2'
    assert Terms.print_term(1, -1) == '-x'
    assert Terms.print_term(1, 1) == 'x'
    assert Terms.print_term(0, 5) == '5'
    assert Terms.print_term(0, 0) == '0'
    assert Terms.print_term(0, -1) == '-1'
    