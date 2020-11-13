from flask import Flask, render_template, jsonify, session, redirect, app
from flask_restful import Resource, Api, reqparse
import sql
from datetime import timedelta
import lookup

app = Flask(__name__)
api = Api(app)
app.secret_key = "super secret key"


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)


@app.route('/')
def login_page():
    session.clear()
    return render_template('login.html', image_file="images/bg.jpg")


@app.route('/main')
def main_page():
    if 'user' in session:
        return render_template('peoplecounter.html',)
    else:
        return redirect('/login')

@app.route('/stats')
def stats():
    try:
        test = lookup.lookup_database() 
        temp = test[-1]
        

        current_people = int(temp[2]) - int(temp[3])
        today_total_people = temp[2]
		
        total = 1 # 데이터 베이스 상에서 예를 들어서 11월 누적 방문객 수를 알고 싶다면 11월의 enter 칼럼의 값을 다 가져와서 다 더해준다.
       
        limit = 50
        
        density = round(current_people / limit * 100)
        if density < 0: 
            density = 0

        if current_people < 0:
            current_people = 0
		
    except:
        print("People Counter Off")
        current_people = 0
        today_total_people = 0
        density = 0
        total = 0

    return render_template('div1.html', current_people=current_people, today_total_people=today_total_people, density=density, total=total)

@app.route('/section')
def section():
    return render_template('div2.html')

class LoginUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str, required=True, help='id input str')
        parser.add_argument('pw', type=str, required=True, help='pw input str')
        args = parser.parse_args()

        print(args['id'], args['pw'])
        data = {'id': args['id'], 'pw': args['pw']}
        rs = sql.login(data)

        print(rs)
        if rs['result'] == 'success':
            session['user'] = rs['idx']
        print(session)
        return jsonify(rs)


class GetData(Resource):
    def get(self):
        rs = sql.get_data()
        return jsonify(rs)


api.add_resource(LoginUser, '/user')
api.add_resource(GetData, '/get_data')

if __name__ == "__main__":
    app.run(host='localhost', port=8000, debug=True)
