from mysite.titanic.models.dataset import Dataset
from mysite.titanic.models.service import Service

class Plot(object):

    dataset = Dataset()
    service = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)

    def print_survived_dead(self):
        this = self.entity
        print(f'The data type of Train is {type(this)}.')
        print(f'Columns of Train is {this.columns}.')
        print(f'The top 5 superior data are {this.head}.')
        print(f'The top 5 inferior data are {this.tail}.')

    
