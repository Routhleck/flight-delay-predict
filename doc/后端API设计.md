# API

## 用户登录相关

### 注册

```python
def signup
# 传入参数：用户名userId, 密码password
# 操作：数据库写入user表
```

### 登录

```python
def login
# 传入参数：用户名userId, 密码password
# 操作：判断user表中是否有用户名userId，没有返回-1，
#      有则继续匹配数据库中密码是否等于传入密码，若有则返回是否为管理员isAdmin，没有返回-1
```

## 管理员管理相关

### 添加用户

```python
def addUser
# 传入参数：用户名userId, 密码password
# 操作：数据库写入user表
```

### 删除用户

```python
def removeUser
# 传入参数: 用户名
# 操作： 数据库删除用户名的行，成功返回true，失败返回false
```

