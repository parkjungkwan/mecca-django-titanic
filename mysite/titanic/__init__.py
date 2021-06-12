from mysite.titanic.views.controller import Controller
from mysite.titanic.templates.plot import Plot

if __name__ == '__main__':
    api = Controller()
    while 1:
        menu = input('0-종료 1-데이터 시각화 2-데이터 모델링 3-머신러닝 4-배포')
        if menu == '0':
            break
        elif menu =='1':
            plot = Plot('train.csv')
            '''
            Train의 데이터 타입은 is <class 'pandas.core.frame.DataFrame'>.
            Train의 컬럼은 'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
                            'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'이다.
            '''
            plot.draw_survived_dead()
            plot.draw_pclass()
            plot.draw_sex()
            plot.draw_embarked()

        elif menu == '2':
            df = api.modeling('train.csv','test.csv')  # 전처리

        elif menu == '3':
            df = api.learning('train.csv','test.csv') # 머신러닝, 사이킷런

        elif menu == '4':
            df = api.submit('train.csv','test.csv')

        else:
            continue
