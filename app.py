from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/mypage/me')
def page_me():
    site = "contact"
    return render_template('first_page.html', site=site)

@app.route('/mypage/contact', methods=["GET", "POST"])
def contact_page():
    site = "me"
    if request.method == "POST": 
        print(request.form)
        return redirect('/mypage/contact')
    elif request.method == "GET": 
        return render_template('sec_page.html', site=site)
    

if __name__ == '__main__':
    app.run()
    
    