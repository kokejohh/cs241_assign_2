import re

class Calculator:
    def __init__(self):
        self.__inputStr = ''
        self.__arithExpr = ''
        self.__tokens = []

    def start(self):
        while True:
            choice = ''
            while choice not in ['c', 'q']:
                self.displayMenu()
                choice = input('Please Enter Your Choice: ')
            if choice == 'q': break
            self.__inputStr = input('\nEnter an arithmetic expression: ')
            self.calculateExpression()
        self.showEndProgram()

    def displayMenu(self):
        print('c: Calculate Arithmetic Expression')
        print('q: Quit')

    def calculateExpression(self):
        self.__arithExpr = self.__inputStr.replace('^', '**')
        self.__tokens = self.ExprToTokenList(self.__arithExpr)
        if (self.__tokens.__len__() == 0):
            ans = eval(self.__arithExpr)
            expo = '{:e}'.format(ans)
            print(f'Result: = {ans} = {expo}\n')
        else:
            ans = eval(self.ExprToLambdaExpr(self.__arithExpr))
            expo = '{:e}'.format(ans)
            print(f'Arithmetic Expression to Evaluate: {self.__arithExpr} = {ans} = {expo}\n')

    def showEndProgram(self): print('\n<End of Program>')

    def ExprToTokenList(self, expr): return re.findall(r"[a-zA-Z]", expr)

    def ExprToLambdaExpr(self, expr):
        str = '('
        for token in self.__tokens:
            str += 'lambda ' + token + ': '
        str += expr + ')'
        nums = {}
        for token in self.__tokens:
            if (token not in nums): nums[token] = input(f'\nEnter a value of variable {token}:')
            self.__arithExpr = self.__arithExpr.replace(token, nums[token], 1)
            str += '(' + nums[token] + ')'
        return str

cal = Calculator()
cal.start()
