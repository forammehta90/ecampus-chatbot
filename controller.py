from calculator import calculator

class controller(object):
    def __init__(self):
        self.calculation = calculator()
    
    def find_solution(self,command):
        response = ""
        if command.startswith('do'):
            response = self.calculation.calculate(command)
        else:
            response = 'I do not understand'
        
        return response