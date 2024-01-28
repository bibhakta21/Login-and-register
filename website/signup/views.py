from django.shortcuts import render

import mysql.connector as sql

fn = ''
ln = ''
s = ''
em = ''
pwd = ''

def signaction(request):
    global fn, ln, s, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", password="12345", database='website',port='3307')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "First_Name":
                fn = value
            if key == "Last_Name":
                ln = value
            if key == "gender":
                s = value
            if key == "Email":
                em = value
            if key == "password":
                pwd = value

        c = "INSERT INTO users (First_Name, Last_Name, gender, Email, password) VALUES ('{}', '{}', '{}', '{}', '{}')".format(fn, ln, s, em, pwd)
        cursor.execute(c)
        m.commit()
        return render(request, 'signup.html')

    # Add the following return statement for GET requests
    return render(request, 'signup.html')
