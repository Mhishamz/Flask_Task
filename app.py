from flask import Flask , render_template , request, jsonify ,redirect, url_for
app = Flask(__name__)

users={1:{"id":1, 'name': 'Hossam Hesham', 'email': 'hossamhisham9004@gmail.com'},
       2:{ "id":2,'name': 'Mohamed Hesham', 'email': 'mohamedhisham14@gmail.com'},
       3:{ "id":3,'name': 'Ahmed Hesham', 'email': 'mohamedhisham14@gmail.com'},
       4:{ "id":4,'name': 'Mahmoud Hesham', 'email': 'mohamedhisham14@gmail.com'},
       5:{ "id":5,'name': 'Fares Hesham', 'email': 'Fares@gmail.com'},
       6:{ "id":6,'name': 'hema Hesham', 'email': 'mohamedhisham14@gmail.com'}

       }

@app.route('/Add_users_menu')
def Users_menu():
    return render_template('./Add_user.html')

@app.route('/Update_users_menu')
def Update_menu():
    return render_template('./Update_user.html')

@app.route('/Delete_users_menu')
def delete_menu():
    return render_template('./Delete_user.html')

@app.route('/')
def home_page():
    return render_template('./my_web_page.html', users=users)

@app.route('/users', methods=['POST'])
def create_user(): 
    print("herer")
    user_id = len(users) + 1
    users[user_id] = {
        "id": user_id,
        "name": request.form.get('name'),
        "email": request.form.get('email')
    }
    print("finished")
    print(users[user_id])
    return redirect(url_for('home_page'))

@app.route('/modify_user', methods=['POST'])
def modify_user():
    user_id = int(request.form.get('userId'))

    try:
        if user_id in users:
            users[user_id] = {
            "id": user_id,
            "name": request.form.get('name'),
            "email": request.form.get('email')
             }
    except ValueError:
        print("Invalid user ID.")

    return redirect(url_for('home_page'))

@app.route('/delete_user', methods=['POST'])
def delete_user():
    try:
        user_id = int(request.form.get('userId'))
        if user_id in users:
            del users[user_id]
            print(f"Deleted User ID: {user_id}")
        else:
            print(f"User ID {user_id} not found.")
    except ValueError:
        print("Invalid user ID.")

    # Redirect back to the select_user page
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    app.run(debug=True)