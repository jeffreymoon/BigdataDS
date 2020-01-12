import pytest
from wolfram_beta_OO import Terms, WolframBeta

def test_solve_query():
    wb = WolframBeta('','')
    assert wb.solve_query("D,0x^2 + -x + 5") == "0x + -1"
    assert wb.solve_query("I,2x + -1,5") == "x^2 + -x + 5"
    assert wb.solve_query("C,2x + -1,5") == "9"
    assert wb.solve_query("I,0,331") == "0x + 331"
    assert wb.solve_query("D,5x^5 + -6.5x^5") == "-7.5x^4"
    assert wb.solve_query("C,cos(x),20") == "0.40808206181339196"
    assert wb.solve_query("C,sin(x),20") == "0.9129452507276277"
    assert wb.solve_query("C,exp(x),20") == "485165195.4097903"
    assert wb.solve_query("C,0x,-1.5") == "0"
    assert wb.solve_query("I,0.5x,0.5") == "0.25x^2 + 0.5"
    assert wb.solve_query("I,-30x^4.5 + -3.5 + 2,-612") == "-5.454545454545454x^5.5 + -1.5x + -612"
    assert wb.solve_query("D2,x^3") == "6x"
    assert wb.solve_query("I,6x,0") == "3x^2 + 0"
    assert wb.solve_query("I,3x^2,0") == "x^3 + 0"
    # assert wb.solve_query("I2,6x,0") == "x^3 + 0 + 0"

def test_compute():
    assert WolframBeta.compute("2x + -1", 5) == "9"
    assert WolframBeta.compute("1x^2 + -3x + 5", 3) == "5"

def test_compute_as_terms():
    terms = Terms()
    terms.terms_dict = {1:2, 0:-1}
    assert terms.compute_as_terms(5) == 9
    terms.terms_dict = {0: 5, 1: -3, 2: 1}
    assert terms.compute_as_terms(3) == 5
    terms.terms_dict = {'sin(x)': 5, 'cos(x)': -3, 'exp(x)': 1}
    assert terms.compute_as_terms(0) == -2
    terms.terms_dict = {'sin(x)': 5, 'cos(x)': -3, 'exp(x)': 1}
    assert terms.compute_as_terms(1) == 5.3047298348941085

def test_integral():
    assert WolframBeta.integral("2x + -1", 5) == "x^2 + -x + 5"
    assert WolframBeta.integral("2x", 0) == "x^2 + 0"
    assert WolframBeta.integral("3x^2 + 0", 0) == "x^3 + 0 + 0"
    assert (WolframBeta.integral("-54cos(x) + -24sin(x) + -exp(x)", -2)
             == "-54sin(x) + 24cos(x) + -exp(x) + -2")

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
    terms.terms_dict = {'sin(x)':5}
    assert terms.integral_as_terms(1).terms_dict == {'cos(x)':-5, 0:1}
    terms.terms_dict = {'cos(x)':1}
    assert terms.integral_as_terms(2).terms_dict == {'sin(x)':1, 0:2}
    terms.terms_dict = {'exp(x)':0}
    assert terms.integral_as_terms(3).terms_dict == {'exp(x)':0, 0:3}

def test_d_dx():
    assert WolframBeta.d_dx("0x^2 + -x + 5") == "0x + -1"
    assert (WolframBeta.d_dx("-54cos(x) + -24sin(x) + -exp(x)")
             == "54sin(x) + -24cos(x) + -exp(x)")

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
    terms.terms_dict = {'sin(x)':5}
    assert terms.d_dx_as_terms().terms_dict == {'cos(x)':5}
    terms.terms_dict = {'cos(x)':-1}
    assert terms.d_dx_as_terms().terms_dict == {'sin(x)':1}
    terms.terms_dict = {'exp(x)':0}
    assert terms.d_dx_as_terms().terms_dict == {'exp(x)':0}

def test_parse_equation():
    term1 = Terms("cos(x)")
    assert term1.get_terms_dict() == {'cos(x)':1}
    term1 = Terms("-sin(x)")
    assert term1.get_terms_dict() == {'sin(x)':-1}
    term1 = Terms("0exp(x)")
    assert term1.get_terms_dict() == {'exp(x)':0}
    term1 = Terms("-x + 5 + 0x^2")
    assert term1.get_terms_dict() == {2:0, 1:-1, 0:5}
    term2 = Terms("0x^2 + -x + 5")
    assert term2.get_terms_dict() == {2:0, 1:-1, 0:5}
    term3 = Terms("5 + -x + 0x^2")
    assert term3.get_terms_dict() == {2:0, 1:-1, 0:5}
    term4 = Terms("0")
    assert term4.get_terms_dict() == {0:0}

def test_parse_term():
    assert Terms.parse_term('cos(x)') == ('cos(x)',1)
    assert Terms.parse_term('-cos(x)') == ('cos(x)',-1)
    assert Terms.parse_term('4cos(x)') == ('cos(x)',4)
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
    term3 = Terms("-sin(x) + 0exp(x) + cos(x)")
    assert term3.print_equation() == "-sin(x) + 0exp(x) + cos(x)"

def test_print_term():
    assert Terms.print_term(2, 0) == '0x^2'
    assert Terms.print_term(1, -1) == '-x'
    assert Terms.print_term(1, 1) == 'x'
    assert Terms.print_term(0, 5) == '5'
    assert Terms.print_term(0, 0) == '0'
    assert Terms.print_term(0, -1) == '-1'
    assert Terms.print_term('cos(x)', 0) == '0cos(x)'
    assert Terms.print_term('sin(x)', 1) == 'sin(x)'
    assert Terms.print_term('exp(x)', -1) == '-exp(x)'
    