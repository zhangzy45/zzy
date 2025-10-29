import pandas as pd

# 设置输出对齐，防止中文不对齐
pd.set_option('display.unicode.east_asian_width', True)

# 获取数据集，并将字符编码指定为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

# 输出数据集的前5行
print(penguin_df.head())

# 删除缺失值所在的行
penguin_df.dropna(inplace=True)

# 将企鹅的种类定义为目标输出变量
output = penguin_df['企鹅的种类']

# 将去除年份列不作为特征列
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]

# 对特征列进行独热编码
features = pd.get_dummies(features)

# 将目标输出变量转换为离散数值
output_codes, output_uniques = pd.factorize(output)

print('下面是去重后，目标输出变量的数据：')
print(output_uniques)
print('下面是独热编码后，特征列的数据：')
print(features.head())

# 第8章/generate_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# 读取数据集，并将字符编码指定为gbk，防止中文报错
penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

# 删除缺失值所在的行
penguin_df.dropna(inplace=True)

# 将企鹅的种类定义为目标输出变量
output = penguin_df['企鹅的种类']

# 将去除年份列不作为特征列
# 使用企鹅栖息的岛屿、喙的长度、翅膀的长度、身体质量、性别作为特征列
features = penguin_df[['企鹅栖息的岛屿', '喙的长度', '喙的深度', '翅膀的长度', '身体质量', '性别']]

# 对特征列进行独热编码
features = pd.get_dummies(features)

# 将目标输出变量转换为离散数值
output_codes, output_uniques = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(features, output_codes, train_size=0.8)

# 构建一个随机森林分类器
rfc = RandomForestClassifier()

# 使用训练集数据x_train和y_train来拟合(训练)模型
rfc.fit(x_train, y_train)

y_pred = rfc.predict(x_test)

score = accuracy_score(y_test, y_pred)
print(f'该模型的准确率是: {score}')
