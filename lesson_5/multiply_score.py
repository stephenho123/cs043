import wsgiref.simple_server
import urllib.parse
import sqlite3
import http.cookies
import random

connection = sqlite3.connect('users.db')
stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='users'"
cursor = connection.cursor()
result = cursor.execute(stmt)
r = result.fetchall()
if (r == []):
    exp = 'CREATE TABLE users (username,password)'
    connection.execute(exp)

def RANDOMWITHNODUPLICATE(randomrandomrandom):
    eeeeeeeeeeeeeeeeeeeeeee = random.randint(0,100)
    while eeeeeeeeeeeeeeeeeeeeeee in randomrandomrandom:
        eeeeeeeeeeeeeeeeeeeeeee = random.randint(0,100)


    return eeeeeeeeeeeeeeeeeeeeeee

def application(environ, start_response):
    headers = [('Content-Type', 'text/html; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    un = params['username'][0] if 'username' in params else None
    pw = params['password'][0] if 'password' in params else None

    if path == '/register' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ?', [un]).fetchall()
        if user:
            start_response('200 OK', headers)
            return ['Sorry, username {} is taken'.format(un).encode()]
        else:
            connection.execute('INSERT INTO users VALUES (?, ?)', [un,pw])
            connection.commit()
            start_response('200 OK', headers)
            return ["USER CREATED".encode()]
            #[INSERT CODE HERE. Use SQL commands to insert the new username and password into the table that has been created. Print a message saying the username was created successfully]

    elif path == '/login' and un and pw:
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()
        if user:
            headers.append(('Set-Cookie', 'session={}:{}'.format(un, pw)))
            start_response('200 OK', headers)
            return ['User {} successfully logged in. <a href="/account">Account</a>'.format(un).encode()]
        else:
            start_response('200 OK', headers)
            return ['Incorrect username or password'.encode()]

    elif path == '/logout':
        headers.append(('Set-Cookie', 'session=0; expires=Thu, 01 Jan 1970 00:00:00 GMT'))
        start_response('200 OK', headers)
        return ['Logged out. <a href="/">Login</a>'.encode()]

    elif path == '/account':
        start_response('200 OK', headers)
        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])

        if 'HTTP_COOKIE' not in environ or 'session' not in cookies:
            return ['Not logged in <a href="/">Login</a>'.encode()]

        [un, pw] = cookies['session'].value.split(':')
        user = cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', [un, pw]).fetchall()

        #This is where the game begins. This section of is code only executed if the login form works, and if the user is successfully logged in
        if user:
            correct = 0
            wrong = 0
            #score = 5:3
            #cookies = http.cookies.SimpleCookie()
            #print('HTTP_COOKIE' in environ)
            #print(cookies)
            if 'HTTP_COOKIE' in environ and 'score' in cookies:
                correct = int(cookies['score'].value.split(':')[0])
                wrong = int(cookies['score'].value.split(':')[1])
                #[INSERT CODE FOR COOKIES HERE]

            page = '<!DOCTYPE html><html><head><title>Multiply with Score</title></head><body>'
            if 'factor1' in params and 'factor2' in params and 'answer' in params:
                if int(params['factor1'][0]) * int(params['factor2'][0]) == int(params['answer'][0]):
                    page += '<p style = "background-color: lightgreen" > CORRECT: ' + params['factor1'][0] + "x" + params['factor2'][0] + "=" + params['answer'][0] +'</p>'
                    correct += 1
                else:
                    page += '<p style = "background-color: red" > INCORRECT: ' + params['factor1'][0] + "x" + params['factor2'][0] + "=" + params['answer'][0] + '</p>'
                    wrong += 1
                #[INSERT CODE HERE. If the answer is right, show the “correct” message. If it’s wrong, show the “wrong” message.]

            elif 'reset' in params:
                correct = 0
                wrong = 0

            headers.append(('Set-Cookie', 'score={}:{}'.format(correct, wrong)))

            f1 = random.randrange(10) + 1
            f2 = random.randrange(10) + 1

            page = page + '<h1>What is {} x {}</h1>'.format(f1, f2)
            answer = []
            a = f1*(f2)
            answer.append(a)
            b = RANDOMWITHNODUPLICATE(answer)
            answer.append(b)
            c = RANDOMWITHNODUPLICATE(answer)
            answer.append(c)
            d = RANDOMWITHNODUPLICATE(answer)
            answer.append(d)
            #print(answer)
            #[INSERT CODE HERE. Create a list that stores f1*f2 (the right answer) and 3 other random answers]
            random.shuffle(answer)

            hyperlink = '<a href="/account?username={}&amp;password={}&amp;factor1={}&amp;factor2={}&amp;answer={}">{}: {}</a><br>'
            letter = "ABCD"
            #[INSERT CODE HERE. Create the 4 answer hyperlinks here using string formatting.]
            for index in range(len(answer)):
                page += hyperlink.format(un,pw,f1,f2,answer[index],letter[index],answer[index])
                #print("%s %s %s %s %s %s %s" %(un,pw,f1,f2,a,letter[index],answer[index]))

            page += '''<h2>Score</h2>
            Correct: {}<br>
            Wrong: {}<br>
            <a href="/account?reset=true">Reset</a>
            </body></html>'''.format(correct, wrong)

            return [page.encode()]
        else:
            return ['Not logged in. <a href="/">Login</a>'.encode()]

    elif path == '/':
        start_response('200 OK', headers)
        #[INSERT CODE HERE. Create the two forms, one to login, the other to register a new account]

        page = '''<!DOCTYPE html>
        <html>
        <head></head>
        <body>
        <form action = "/login">
            Username <input type="text" name="username"><br>
            Password <input type="password" name="password"><br>
            <input type="submit" value = 'login'>
        </form action = "/register">
        <form action = "/register">
            Username <input type="text" name="username"><br>
            Password <input type="password" name="password"><br>
            <input type="submit" value = 'register'>
        </form>
        </body></html>'''
        return [page.encode()]

    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()