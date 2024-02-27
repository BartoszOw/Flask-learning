from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/mypage/me')
def page_me():
    return render_template('first_page.html')

@app.route('/mypage/contact')
def contact_page():
    return render_template('sec_page.html')