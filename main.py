from flask import Flask, render_template, jsonify, session, redirect, app
from flask_restful import Resource, Api, reqparse
import sql
from datetime import timedelta
#import lookup

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
   #test  = lookup.lookup_database() 
   #print(test)
   
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
    app.run(host='192.168.0.19', port=8000, debug=True)
