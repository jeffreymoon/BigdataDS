
"""
Lab2-2. Wolfram-Beta OO
support cos, sin, exp
float type degree & factor

Object Oriented
using classes
    WolframBeta
    Terms (has terms_dict)
"""
import traceback
import math

class Terms:
    def __init__(self, equation=None):
        """
        :param equation: str, 문자열로 표현된 함수
                        None 인 경우 terms_dict 를 생성만 함
        """
        # make Terms.terms : dict {key = degree, val = factor}
        # store the equation if not None
        self.terms_dict = dict()
        if equation:
            self.parse_equation(equation)
        self.equation = equation
        pass

    def __str__(self):
        """
        :return: str equation
        """
        # this function support interface
        # str(Terms) -> string (equation)
        return self.print_equation()

    def __eq__(self, other):
        """
        :param other: Terms
        :return: True when equal, ow False
        """
        # don't modify this function
        if type(other) != Terms:
            return False

        t1 = self.terms_dict
        t2 = other.terms_dict
        eps = 1e-6

        keys = set(t1.keys()).union(t2.keys())
        for k in keys:
            if not math.isclose(t1.get(k, 0), t2.get(k, 0),
                                rel_tol=eps, abs_tol=eps):
                return False
        return True

    def get_terms_dict(self):
        return self.terms_dict

    @staticmethod
    def print_term(degree, factor):
        """
        :param degree: float, 항의 차수
        :param factor: float, 항의 계수
        :return: str
        """
        # use wolfram_beta's print_term
        if type(degree) is str:
            deg = degree
            x = ''
            caret = ''
        else :
            x = '' if (degree == 0) else 'x'
            caret = '' if (degree == 0 or degree == 1) else '^'
            deg = '' if (degree == 0 or degree == 1) else str(degree)
        
        if degree is not 0:
            fac = '' if factor is 1 else ('-' if factor is (-1) else str(factor))
        else:
            fac = str(factor)

        return fac + x + caret + deg

    def print_equation(self):
        """
        :param self: self.terms_dict: dict {key=degree, value=factor}
        :return: str equation
        """
        # use wolfram_beta's print_equation
        equa = []
        for key, value in self.terms_dict.items():
            temp = self.print_term(key, value)
            equa.append(str(temp))
        result = ' + '.join(equa)
        return result        

    @staticmethod
    def parse_term(term_str):
        """
        :param term_str: str (a single term <- a part of equation)
        :return: 2-tuple (degree: float/str, factor: float)
        """
        # use wolfram_beta's parse_term
        # now, degree is float
        #             or (cos(x), sin(x), exp(x)
        #      factor is float
        if 'sin(x)' in term_str:
            ts = term_str.split('sin(x)')
            degree = 'sin(x)'
        elif 'cos(x)' in term_str:
            ts = term_str.split('cos(x)')
            degree = 'cos(x)'
        elif 'exp(x)' in term_str:
            ts = term_str.split('exp(x)')
            degree = 'exp(x)'
        elif 'x^' in term_str:
            ts = term_str.split('x^')
            try:
                degree = int(ts[1])
            except:
                degree = float(ts[1])
        elif 'x' in term_str:
            ts = term_str.split('x')
            degree = 1
        else:
            ts = [term_str]
            degree = 0

        if ts[0] is '':
            factor = 1
        elif ts[0] is '-':
            factor = -1
        else :
            try:
                factor = int(ts[0])
            except:
                factor = float(ts[0])
        
        return degree, factor

    def parse_equation(self, equation):
        """
        :param equation: str
        :return: None (modify self.terms_dict)
        """
        # update self.terms_dict
        # terms in equation is separated by ' + '
        # use dict.get(key, default)
        eq_dict = dict()

        eq_list = [self.parse_term(eq) for eq in equation.split(' + ')]
        for key, value in eq_list:
            if key in eq_dict:
                eq_dict[key] += value
            else :
                eq_dict[key] = value

        self.terms_dict = eq_dict

    def d_dx_as_terms(self):
        """
        :return: Terms : that result of differential
        """
        # make Terms that result of differential
        dterms = Terms()

        # process each term (degree, factor) in terms
        # use dict.get(key, default)
        
        for degree in self.terms_dict:
            if type(degree) is str:
                if degree == 'sin(x)':
                    key = 'cos(x)'
                    dterms.terms_dict[key] = self.terms_dict.get(degree, 0)
                elif degree == 'cos(x)':
                    key = 'sin(x)'
                    dterms.terms_dict[key] = self.terms_dict.get(degree, 0) * (-1)
                elif degree == 'exp(x)':
                    key = 'exp(x)'
                    dterms.terms_dict[key] = self.terms_dict.get(degree, 0)
                else:
                    pass
            else:
                if degree is 0:
                    continue
                key = degree - 1
                dterms.terms_dict[key] = self.terms_dict.get(degree, 0) * degree

        if (len(dterms.terms_dict)) is 0:
            dterms.terms_dict = {0:0}
            
        return dterms

    def integral_as_terms(self, constant):
        """
        :param constant: float
        :return: Terms : that result of integral
        """
        # make Terms that result of integral
        iterms = Terms()

        # process each term (degree, factor) in terms
        # use dict.get(key, default)

        # don't forget the constant
        for degree in self.terms_dict:
            if type(degree) is str:
                if degree == 'sin(x)':
                    key = 'cos(x)'
                    iterms.terms_dict[key] = self.terms_dict.get(degree, 0) * (-1)
                elif degree == 'cos(x)':
                    key = 'sin(x)'
                    iterms.terms_dict[key] = self.terms_dict.get(degree, 0)
                elif degree == 'exp(x)':
                    key = 'exp(x)'
                    iterms.terms_dict[key] = self.terms_dict.get(degree, 0)
                else:
                    pass
            else:
                key = degree + 1
                factor = self.terms_dict.get(degree, 0)
                if key % 1 == 0 and factor % 1 == 0:
                    iterms.terms_dict[key] = factor // key
                else:
                    iterms.terms_dict[key] = float(factor) / key

        iterms.terms_dict[0] = constant

        return iterms

    def compute_as_terms(self, x):
        """
        :param x: float
        :return: float
        """
        result = 0.0
        # compute the result using Terms
        for degree in self.terms_dict:
            factor = self.terms_dict.get(degree, 0)
            if type(degree) is str:
                if degree == 'sin(x)':
                    result += factor * math.sin(x)
                elif degree == 'cos(x)':
                    result += factor * math.cos(x)
                elif degree == 'exp(x)':
                    result += factor * math.exp(x)
                else:
                    pass
            else:
                # factor = self.terms_dict.get(degree, 0)
                result += factor * (x**degree)
        
        return int(result) if result % 1 == 0 else result


class WolframBeta:
    def __init__(self, input_path, output_path):
        """
        :param input_path: path of input query file
        :param output_path: path of output file storing result
                            generated by wolfram beta
        """
        self.input_path = input_path
        self.output_path = output_path

        # if you need more initializing process,
        # just write your code !

        pass

    @staticmethod
    def d_dx(equation):
        """
        :param equation: str
        :return: equation str (differential result)
        """
        # using Terms's class function
        terms = Terms(equation)
        terms.parse_equation(equation)
        dx_terms = terms.d_dx_as_terms()
        return dx_terms.print_equation()

    @staticmethod
    def integral(equation, constant):
        """
        :param equation: str
        :param constant: str
        :return: str equation (integral result)
        """
        # using Terms's class function
        terms = Terms(equation)
        terms.parse_equation(equation)
        integral_terms = terms.integral_as_terms(constant)
        return integral_terms.print_equation()

    @staticmethod
    def compute(equation, x):
        """
        :param equation: str
        :param x: str
        :return: str <- not int type
        """
        # using Terms's class function
        terms = Terms(equation)
        terms.parse_equation(equation)
        try:
            cast_x = int(x)
        except:
            cast_x = float(x)
        return str(terms.compute_as_terms(cast_x))

    def solve_query(self, line):
        """
        :param line: str (query)
        :return: str (result)
        """
        try:
            # 이 안에 코드를 작성해주세요!
            # solve_query() 함수에서 실행 도중 불가피한 오류가 발생하더라도,
            # 다음 쿼리를 받아들일 수 있게 도와줍니다.
            query = line.split(',')
            if query[0] == 'D':
                return WolframBeta.d_dx(query[1])
            elif query[0] == 'I':
                return WolframBeta.integral(query[1], query[2])
            elif query[0] == 'C':
                return WolframBeta.compute(query[1], query[2])
            else:
                pass            
            return ''
        except:
            traceback.print_exc()
            return ''

    def solve(self):
        """
        :return: None (파일 입출력으로 문제 해결)
        """
        with open(self.input_path) as f_in:
            with open(self.output_path, 'w') as f_out: 
                for line in f_in:
                    f_out.write(self.solve_query(line.strip())+'\n')
        return


if __name__ == '__main__':
    ipath = 'input_sample.txt'
    opath = 'output_sample.txt'

    wolfram_beta = WolframBeta(ipath, opath)
    wolfram_beta.solve()