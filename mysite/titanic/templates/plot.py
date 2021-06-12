from mysite.titanic.models.dataset import Dataset
from mysite.titanic.models.service import Service

class Plot(object):

    dataset = Dataset()
    service = Service()

    def __init__(self, fname):
        self.entity = self.service.new_model(fname)