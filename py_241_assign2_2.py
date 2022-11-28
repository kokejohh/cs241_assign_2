import re
from decimal import Decimal

class Calculator:
    def __init__(self):
        self.__inputStr = ''
        self.__arithExpr = ''
        self.__tokens = []

    def start(self):
        while True:
            choice = ''
            while choice not in ['c', 'q']: choice = self.displayMenu()
            if choice == 'q': break
            self.__inputStr = input('\nEnter an arithmetic expression: ')
            self.calculateExpression()
        self.showEndProgram()

    def displayMenu(self):
        print('c: Calculate Arithmetic Expression')
        print('q: Quit')
        return input('Please Enter Your Choice: ')

    def calculateExpression(self):
        self.__arithExpr = self.__inputStr.replace('^', '**')
        self.__tokens = self.exprToTokenList(self.__arithExpr)
        if (self.__tokens.__len__() == 0):
            ans = eval(self.__arithExpr)
            print(f'Result: = {ans} = ', end='')
        else:
            lamb_expr, self.__arithExpr = self.exprToLambdaExpr(self.__arithExpr)
            ans = eval(lamb_expr)
            self.__arithExpr = self.__arithExpr.replace('**', '^')
            print(f'Arithmetic Expression to Evaluate: {self.__arithExpr} = {ans} = ', end='')
        expo_notation = self.format_e(ans)
        print(f'{expo_notation}\n')

    def showEndProgram(self): print('\n<End of Program>')

    def exprToTokenList(self, expr): return re.findall(r"[a-zA-Z]", expr)

    def exprToLambdaExpr(self, expr):
        tokens = self.exprToTokenList(expr)
        lamb_expr = '('
        for token in tokens: lamb_expr += f'lambda {token}: ' 
        lamb_expr += f'{expr})'
  
        nums = {}
        arith_expr = self.__arithExpr
        for token in tokens:
            if (token not in nums): nums[token] = input(f'\nEnter a value of variable {token}:')
            arith_expr = arith_expr.replace(token, nums[token], 1)
            lamb_expr += f'({nums[token]})'
        return lamb_expr, arith_expr
    
    def format_e(self, val):
        tup = Decimal(str(val)).as_tuple()
        ans = ''.join(f'{digit}.' if (i == 0) else f'{digit}' for i, digit in enumerate(tup.digits))
        sign = '-' if tup.sign else ''
        num = ans.rstrip('0').rstrip('.')
        expo = tup.digits.__len__() - 1 + tup.exponent
        return f'{sign}{num}e{expo}'

cal = Calculator()
cal.start()
