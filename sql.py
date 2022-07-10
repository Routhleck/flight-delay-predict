from flask import Flask, request, render_template

app = Flask(__name__)

def querySomething(engine, table, condition, conditionColumn, resultColumn):
    with engine.connect() as con:
        sql = 'select ' + str(resultColumn) + ' from ' + str(table) + ' where ' + str(conditionColumn) + ' = ' + str(condition)
        rs = con.execute(sql)
        return rs

def queryAllthing(engine, table, resultColumn):
    with engine.connect() as con:
        sql = 'select ' + str(resultColumn) + ' from ' + str(table)
        rs = con.execute(sql)
        return rs


