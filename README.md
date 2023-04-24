# 23sp_ST

## 安装
依赖见requirements.txt，可通过pip install或pipreqs配置

## 测试
在server目录下flask run

## demo说明
- data.db为sqlite数据库文件
- 传递了一个集群的三个集体指标（Health_active_shards，Health_status，Health_number_of_nodes）
- 每个均为“date-value”的list
app.py中：
![image](https://user-images.githubusercontent.com/73417610/233922504-42a6680c-25ff-47da-990f-d67e3a0c86ab.png)
使用时将上图index.html改为对应html文件
在html中使用：
![image](https://user-images.githubusercontent.com/73417610/233923253-fe750d66-44be-46f0-a498-0a9ac16a44e9.png)
row[0]为date，row[1]为value
