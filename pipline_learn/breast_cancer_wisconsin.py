import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

def getData():
    df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/'
                     'breast-cancer-wisconsin/wdbc.data', header=None)
                                     # Breast Cancer Wisconsin dataset

    X, y = df.values[:, 2:], df.values[:, 1]
                                    # y为字符型标签
                                    # 使用LabelEncoder类将其转换为0开始的数值型
    # Encode labels with value between 0 and n_classes-1.
    encoder = LabelEncoder()
    y = encoder.fit_transform(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=0)
    return X_train, X_test, y_train, y_test


def Examples_SklearnOrg_Pipline(X_train, X_test, y_train, y_test):
    from sklearn import svm
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import f_regression
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    # SelectKBest 移除得分前 k 名以外的所有特征(取top k)
    anova_filter = SelectKBest(f_regression, k=5)
    # clf = svm.LinearSVR(kernel='linear')
    clf = svm.LinearSVC()
    anova_svm = Pipeline([('sc', StandardScaler()),
                        ('pca', PCA(n_components=2)),('anova', anova_filter), ('svc', clf)])
    # You can set the parameters using the names issued
    # For instance, fit using a k of all in the SelectKBest
    # Because the PCA,we only have 2 features
    # and a parameter 'C' of the svm
    anova_svm.set_params(anova__k="all", svc__C=.1).fit(X_train, y_train)

    # prediction_trian = anova_svm.predict(X_train)
    # prediction_test = anova_svm.predict( X_test)
    score_train = anova_svm.score(X_train, y_train)
    score_test = anova_svm.score(X_test, y_test)

    # print("prediction_train :", prediction_trian)
    # print("prediction_test :", prediction_test)
    print("score_train :", score_train)
    print("score_test :", score_test)
    # getting the selected features chosen by anova_filter
    Pri_nameed_steps00 = anova_svm.named_steps['anova'].get_support()
    print(Pri_nameed_steps00)

    # Another way to get selected features chosen by anova_filter
    Pri_nameed_steps01 = anova_svm.named_steps.anova.get_support()
    print(Pri_nameed_steps01)

X_train, X_test, y_train, y_test = getData()
Examples_SklearnOrg_Pipline(X_train, X_test, y_train, y_test)
print('over')
