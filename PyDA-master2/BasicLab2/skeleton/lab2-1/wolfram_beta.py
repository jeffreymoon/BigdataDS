
"""
Lab2-1. Wolfram-Beta
only int range degree & factor

Not Object Oriented,
just functions (not class)
"""
import traceback
import math


def print_term(degree, factor):
    """
    :param degree: int, 항의 계수
    :param factor: int, 항의 차수
    :return: str
    """
    x = 'x'
    gguk = '^'
    if factor == 0:
        fac = '0'
    elif factor == 1:
        fac = '1'
    elif factor == -1:
        fac = '-1'
    else:
        fac = str(factor)

    if degree == 0:
        deg = ''
        x = ''
        gguk = ''
    elif degree == 1:
        deg = ''
        gguk = ''
    else:
        deg = str(degree)

    result = fac + x + gguk + deg
    return result    # when degree == 2 and factor == 7


def print_equation(terms):
    """
    :param terms: dict {key=degree, value=factor}
    :return: str
    """
    equa = []
    for key, value in terms.items():
        temp = print_term(key, value)
        # if temp == 0:
        #     continue
        equa.append(str(temp))
    result = ' + '.join(equa)
    return result # '1 + 5x^2'    # when terms == {0: 1, 2: 5}


def parse_term(term_str):
    """
    :param term_str: str
    :return: 2-tuple (degree: int, factor: int)
    """
    if "^" in term_str:
        divide = term_str.split('x^')
    elif 'x' in term_str:
        divide = term_str.split('x')
    else:
        divide = term_str
    print(divide)
    return 2, 5    # when term_str == '5x^2'


def parse_equation(equation):
    """
    :param equation: str
    :return: dict {key=degree, value=factor}
    """
    return {1: -7, 2: 3}    # when equation == '-7x + 3x^2'


def d_dx_as_terms(terms):
    """
    :param terms: dict {key=degree, value=factor}
    :return: dict {key=degree, value=factor}
             terms와 동일한 형식, 값은 terms의 미분 결과
    """
    return {0: 3, 2: 6}    # when terms == {1: 3, 3: 2}


def d_dx(equation):
    """
    :param equation: str
    :return: str (differential result)
    """
    return '2 + 6x'    # when equation == '2x + 3x^2'


def integral_as_terms(terms, constant):
    """
    :param terms: dict (key=degree, value=factor)
    :param constant: int
    :return: dict {key=degree, value=factor}
             terms와 동일한 형식, 값은 terms의 적분 결과
    """
    return {0: 6, 1: -2, 2: 5}    # when terms == {0: -2, 1: 10} and constant == 6


def integral(equation, constant):
    """
    :param equation: str
    :param constant: str
    :param constant: str (integral result)
    """
    return '5 + 3x + 5x^5'    # when equation == '3 + 25x^4' and constant == 5


def compute_as_terms(terms, x):
    """
    :param terms: dict (key=degree, value=factor)
    :param x: int
    :return: int
    """
    return 5    # when terms == {0: 5, 1: -3, 2: 1} and x = 3


def compute(equation, x):
    """
    :param equation: str
    :param x: str
    :return: str <- not int type
    """
    return '5'    # when equation == '5 + -3x + x^2' and x == 3


def solve_query(line):
    """
    :param line: str
    :return: str
    """
    try:
        # 이 안에 코드를 작성해주세요!
        # solve_query() 함수에서 실행 도중 불가피한 오류가 발생하더라도,
        # 다음 쿼리를 받아들일 수 있게 도와줍니다.
        return '2x'    # if line == 'D,x^2'
    except:
        traceback.print_exc()
        return ''


def solve(input_path, output_path):
    """
    :param input_path: str
    :param output_path: str
    :return: None (파일 입출력으로 문제 해결)
    """
    return


if __name__ == '__main__':
    ipath = 'input_sample.txt'
    opath = 'output_sample.txt'

    # solve(ipath, opath)
    # print(print_term(2, 0))
    # print(print_term(1, -1))    
    # print(print_term(0, 5))
    # dic = dict({2:0, 1:-1, 0:5})
    # print(print_equation(dic))
    parse_term("0x^2")
    parse_term("-x")
    parse_term("5")
