from flask import Flask, render_template, request, jsonify, send_from_directory
import sqlite3
import pandas as pd
import json

app = Flask(__name__)

# SQLite DB 파일 경로
DB_PATH = 'database.db'

def get_db_connection():
    """SQLite3 DB 연결하는 함수"""
    conn = sqlite3.connect(DB_PATH)
    return conn

@app.route('/')
def home():
    # # DB에서 DataFrame으로 읽어와 웹페이지에 테이블 렌더링
    # conn = get_db_connection()
    # df = pd.read_sql_query('SELECT * FROM issue', conn)
    # conn.close()

    # # 전체 셀 공백 제거
    # df = df.apply(lambda x: x.str.strip(), axis = 1)
    # # project 칼럼 추가
    # for idx in range(0, len(df)):
    #     df['project'][idx] = df['key'][idx].split('-')[0]

    # # 해외법인 잔여이슈 현황
    # dataList = []
    # temp = pd.pivot_table(df, index='region', values='key', aggfunc='count')
    # for i in range(0,len(temp)):
    #     dataList.append(int(temp['key'][i]))

    # # 유형별 이슈 현황
    # df.groupby(['region', 'project'])[['key']].count()
    # # 우선순위별 이슈 현황
    # df.groupby('priority')[['key']].count()
    # # 법인별 우선순위 현황
    # df.groupby(['region', 'priority'])[['key']].count()


    # return render_template('home.html', dataList=json.dumps(dataList))
    return render_template('home.html')

@app.route('/data/seoul.geojson')
def serve_geojson():
    return send_from_directory('data', 'seoul.geojson')

@app.route('/issues')
def show_issues():
    """DB에서 DataFrame으로 읽어와 웹페이지에 테이블 렌더링"""
    conn = get_db_connection()
    df = pd.read_sql_query('SELECT * FROM issue', conn)
    conn.close()

    # DataFrame을 리스트 형태로 변환
    issues = df.to_dict(orient='records')

    # HTML 템플릿에 데이터 넘기기
    return render_template('issues.html', issues=issues)

@app.route('/map')
def view_map():

    # HTML 템플릿에 데이터 넘기기
    return render_template('map.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)