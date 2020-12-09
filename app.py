from flask import Flask, render_template, request, session,jsonify, redirect
import datetime
app = Flask(__name__)
app.secret_key = 'jeongseojeongseo' # secret key는 랜덤 문자열로 설정
from pymongo import MongoClient     # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  
db = client.dbtest                  # 임시로 dbtest에 저장      

## home화면 보여주기
@app.route('/')
def home():
    return render_template('home.html')

# 회원가입 구현
@app.route('/signin', methods=['GET','POST'])
def signin():
    # get method일 때 템플릿만 보여주기
    if request.method == 'GET':
        return render_template('signin.html')
    # post method일 때 사용자의 입력값을 받아서 db에 저장
    else:
        userid = request.form.get('userid')
        password = request.form.get('password')
        password_check = request.form.get('password_check')

    # 예외상황일 때 경고창 띄워주기    
    if not userid and password and password_check:
        return jsonify({'msg': "입력이 완료되지 않았습니다."})
    elif password != password_check:
        return jsonify({'msg': "비밀번호를 확인해주세요"})
    else:
        #정상적으로 입력 받았을 때 db에 입력
        data = {
            'userid':userid,
            'password':password
        }
        db.user.insert_one(data)
        return redirect('/login')
    # 정상적으로 회원가입이 완료되고난 후 home 화면으로 이동(추후에 메인페이지나 로그인 페이지로 변경 가능)
    return redirect('/login')

# 로그인 구현
@app.route('/login', methods=['GET','POST'])
def login():
    # get method일 때 템플릿 띄워주기
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 사용자가 입력한 아이디와 패스워드 가져오기
        userid = request.form['userid']
        password = request.form['password']
        # user db에 있는지 확인
        account_user = db.user.find_one({'userid':userid})
        if account_user:
            if password == account_user['password']:
                # 세션을 생성해 주고 홈 화면으로 이동(추후 메인페이지로 변경 가능)
                session['username'] = userid
                return redirect('/')
        return render_template('error.html')

# 로그아웃
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# 카드 생성
@app.route('/main', methods=['GET','POST', 'DELETE'])
def main():
    # 카드 listing
    if request.method == 'GET':
        cards = list(db.main.find({},{'_id':0}).sort('created_datetime', -1))
        return render_template("main.html", cards=cards)

    # 카드 create
    elif request.method == 'POST':
        card_id_receive = request.form['card_id_give']
        booktitle_receive = request.form['booktitle_give']
        title_receive = request.form['title_give']
        context_receive = request.form['context_give']
        priority_receive = request.form['priority_give']
        flag = request.form['private_flag']

        writer = session['username']
        completed = False
        if flag == 'private':
            private = True
        else:
            private = False
        created_datetime = datetime.datetime.now()
        display_datetime = datetime.datetime.now().strftime('%Y-%m-%d')

        data = {
            'writer' : writer,
            'card_id' : card_id_receive,
            'title' : title_receive,
            'context' : context_receive,
            'priority' : int(priority_receive),
            'booktitle' : booktitle_receive,
            'completed' : completed,
            'private' : private,
            'created_datetime' : created_datetime,
            'display_datetime' : display_datetime
        }
        db.main.insert_one(data)
        return redirect('/main')
    # 카드 delete
    else:
        card_id_receive = request.form['card_id_give']
        db.main.delete_one({ "card_id": card_id_receive })
        return render_template('main.html')
    
# 카드 수정
@app.route('/main/<userId>', methods=['GET','POST'])
def update(userId):
    if request.method == 'GET':
        target_card = db.main.find_one({'card_id':userId},{'_id':0})
        print(userId)
        return render_template('main.html', target_card = target_card)
    else:
        return render_template('main.html')
        
@app.route('/main/book', methods=['GET'])
def sorting_book():
    if request.method == 'GET':
        cards = list(db.main.find({},{'_id':0}).sort('booktitle'))
        return render_template("main.html", cards=cards)
    else:
        return render_template("main.html")

@app.route('/main/priority', methods=['GET'])
def sorting_priority():
    if request.method == 'GET':
        cards = list(db.main.find({},{'_id':0}).sort('priority', -1))
        print(cards)
        return render_template("main.html", cards=cards)
    else:
        return render_template("main.html", cards=cards)

@app.route('/main/private', methods=['GET'])
def sorting_private():
    if request.method == 'GET':
        cards = list(db.main.find({'private':True},{'_id':0}))
        return render_template("main.html", cards=cards)
    else:
        return render_template("main.html", cards=cards)
        

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)