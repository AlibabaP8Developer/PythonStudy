import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_train = pd.read_csv("./Train_data.csv")
df_test = pd.read_csv("./Predict_data.csv")
df_all = pd.concat([df_train, df_test])
print("train size:", len(df_train))
print("test size:", len(df_test))
print(df_all.info())

# 异常检测
def review_outlier(x, lower, upper):
    '''
    根据3-西格玛方法检测出特征中的异常值
    '''
    if x < lower or x > upper:
        return True
    return False


df_outlier_train = df_train.copy()
k = 3.0

for fea in df_outlier_train.columns:
    lower = df_outlier_train[fea].mean() - k * df_outlier_train[fea].std()
    upper = df_outlier_train[fea].mean() + k * df_outlier_train[fea].std()

    outlier = df_outlier_train[fea] \
        .apply(review_outlier, args=(lower, upper))
    print("{} 异常值数量：{}".format(fea, outlier.sum()))

sns.countplot(x='Label', data=df_train)

# 对数据中的好坏客户的年龄分布进行统计
bad = df_train[df_train['Label'] == 1].index
good = df_train[df_train['Label'] == 0].index
fig, ax = plt.subplots(2, 1, figsize=[6, 6])
fig.subplots_adjust(hspace=0.5)
sns.distplot(df_train.loc[bad, 'Age'], ax=ax[0])
ax[0].set_title("bad customer")
sns.distplot(df_train.loc[good, 'Age'], ax=ax[1])
ax[1].set_title("good customer")
print("坏客户年龄统计\n", df_train.loc[bad, 'Age'].describe())
print("好客户年龄统计\n", df_train.loc[good, 'Age'].describe())

# 变量显著性检验
from scipy.stats import levene, ttest_ind

bad = df_train[df_train['Label'] == 1].index
good = df_train[df_train['Label'] == 0].index
fea_pvalue = {}
for fea in df_train.columns[2:]:

    p_values = {}
    _, pvalue_l = levene(train_x.loc[bad, fea], train_x.loc[good, fea])

    # 当p>0.05时不能拒绝原假设，即认为方差对齐
    if pvalue_l > 0.05:
        _, p_values = ttest_ind(train_x.loc[bad, fea], train_x.loc[good, fea], equal_var=True)
        fea_pvalue[fea] = p_values

    else:
        _, p_values = ttest_ind(train_x.loc[bad, fea], train_x.loc[good, fea], equal_var=False)
        fea_pvalue[fea] = p_values

fea_pvalue = pd.DataFrame(fea_pvalue, index=[0]).T.rename(columns={0: 'p-value'})

df_train = df_train.drop(columns=['Unnamed: 0'])
df_test = df_test.drop(columns=['Unnamed: 0'])
from sklearn.model_selection import train_test_split
