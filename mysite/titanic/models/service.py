from mysite.titanic.models.dataset import Dataset
import pandas as pd
import numpy as np

class Service(object):

    dataset = Dataset()

    def new_model(self, payload) -> object:
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis = 1) # axis 0 가로, 1 세로

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop([i], axis = 1)
            this.test = this.test.drop([i], axis=1)
            # 학습, 테스트 세트는 항상 동일하게 편집한다.
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked', 'S'}) # S는 사우스햄튼
        this.test = this.test.fillna({'Embarked', 'S'})  # S는 사우스햄튼
        this.train['Embarked'] = this.train['Embarked'].map({'S': 1, 'C': 2, 'Q':3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this

    @staticmethod
    def title_norminal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(
                ['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mme', 'Rare')
            title_mapping = {'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
            dataset['Title'] = dataset['Title'].fillna(0)
            dataset['Title'] = dataset['Title'].map(title_mapping)
        return this

    @staticmethod
    def gender_norminal(this) -> object:
        combine = [this.train, this.test]
        gender_mapping = {'male': 0, 'female': 1}
        for i in combine:
            i['Gender'] = i['Sex'].map(gender_mapping)
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        for data in train, test:
            data['Age'] = data['Age'].fillna(-0.5)
        bins = [-1, 0, 5, 12, 18, 24, 35, 68, np.inf]
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
        age_title_mapping = {'Unknown': 0, 'Baby': 1, 'Child': 2, 'Teenager': 3, 'Student': 4,
                             'Young Adult': 5, 'Adult': 6, 'Senior': 7}
        for data in train, test:
            data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels)
            data['AgeGroup'] = data['AgeGroup'].map(age_title_mapping)
        return this

    @staticmethod
    def fare_ordinal(this) -> object:

        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4, labels={1,2,3,4}) # 최고와 최저를 통해 4등분하라
        this.test['FareBand'] = pd.qcut(this.test['Fare'], 4, labels={1,2,3,4})

        







