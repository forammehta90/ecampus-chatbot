from calculator import calculator
import nlp

class controller(object):
    def __init__(self):
        self.calculation = calculator()
        self.nlp = nlp.Nlp()
    
    def find_solution(self,command):
        response = ""
        if command.startswith('do'):
            response = self.calculation.calculate(command)
        else:
            response = self.nlp.analyzer(command)
        
        return response