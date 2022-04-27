from urllib import response
from flask import Flask, redirect, render_template, request, session
import pymongo
import requests
import json
import base64

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client.get_database('total_records')
records = db.register

scrapper = "http://10.201.77.70:2593/fetchprod?name="
comparator = "http://10.201.77.70:2593/fetchcomparison?url="
analyzer = "http://10.201.77.70:2593/fetchreviews?name="
global reviews_list

@app.route('/sign_out')
def sign_out(user=""):
    session["email"]=""
    session.pop("email", None)
    return render_template('pages-login.html', user=user)

@app.route('/')
def home_page(user=""):
    return redirect('/categories/Mobile')
    # return render_template('index.html', user=user)

@app.route('/categories/<string:user>', methods = ['get'])
def categories(user):
    global reviews_list
    response = requests.get(url = scrapper+user)
    review_response = requests.get(url = analyzer+user)
    review_data = review_response.json()
    data = response.json()
    products_list = data['result']
    products_list = products_list[0:9]
    reviews_list = review_data['result']
    return render_template('sample.html', user=products_list, name = user)


@app.route('/search', methods = ['post'])
def search(user=""):
    user = request.form.get('query')
    response = requests.get(url = scrapper+user)
    review_response = requests.get(url = analyzer+user)
    review_data = review_response.json()
    data = response.json()
    products_list = data['result']
    products_list = products_list[0:9]
    global reviews_list
    reviews_list = review_data['result']

    return render_template('sample.html', user=products_list, name = user)
#     

@app.route('/comparison', methods = ['post'])
def compare():
    # print(type(request.form.get('url')))

    pc_url = request.form.get('url')
    index = int(request.form.get('index'))

    global reviews_list
    
    if(pc_url == ""):
        products_list = [
            {
      "shopping_results": [
        {
          "link": "noresults.html", 
          "price": "No Results for comparison", 
          "title": "No Results for comparison"
        }
      ]
    }
        ]
        if(index > len(reviews_list)-1):
            polarity = reviews_list[0]['polarity']
            polarity = round(polarity, 2)
            return render_template('comparison.html', user = products_list, reviews = reviews_list[0], polarity = polarity*100, revpolarity = 100*(1 - polarity))
    
        polarity = reviews_list[index]['polarity']
        polarity = round(polarity, 2)
        
        return render_template('comparison.html', user = products_list, reviews = reviews_list[index], polarity = polarity*100, revpolarity = 100*(1 - polarity))
    
    response = requests.get(url = comparator+pc_url)
    data = response.json()
    products_list = data['result']
    
    if(index > len(reviews_list)-1):
        polarity = reviews_list[0]['polarity']
        polarity = round(polarity, 2)
        return render_template('comparison.html', user = products_list, reviews = reviews_list[0], polarity = polarity*100, revpolarity = 100*(1 - polarity))
    
    polarity = reviews_list[index]['polarity']
    polarity = round(polarity, 2)
    return render_template('comparison.html', user = products_list, reviews = reviews_list[index], polarity = polarity*100, revpolarity = 100*(1 - polarity))

@app.route('/pages_faq')
def pages_faq():
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('pages-faq.html', user=user)

@app.route('/users_profile')
def users_profile():
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('users-profile.html', user=user)

@app.route('/pages_contact')
def pages_contact():
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('pages-contact.html', user=user)

@app.route('/', methods=['post','get'])
def pages_login():
    message=''
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
        return render_template('index.html', user=user)

@app.route('/pages_error_404')
def pages_error_404():
   return render_template('pages-error-404.html')

@app.route('/pages_blank')
def pages_blank():
   return render_template('pages-blank.html')

@app.route('/components')
def components():
    message=''
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('components.html', user=user)
   
@app.route('/group_view')
def group_view():
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('group-view.html', user=user)

@app.route('/bluetooth_devices')
def bluetooth_devices():
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('bluetooth-devices.html', user=user)

@app.route('/scheduled_jobs')
def scheduled_jobs():
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('scheduled-jobs.html', user=user)

@app.route('/logs')
def logs():
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('logs.html', user=user)

@app.route('/commands')
def commands():
    print(session)
    if "email" in session and session["email"]!="":
        user_found = records.find_one({"email": session["email"]})
        user = {'name': user_found["name"], 'email': user_found["email"], 'password': user_found["password"], 'fullname': user_found["fullname"], 'country': user_found["country"], 'address':user_found["address"], 'phone':user_found["phone"] }
        print(user)
    return render_template('commands.html', user=user)

@app.route('/tables_general')
def tables_general():
   return render_template('tables-general.html')

@app.route('/tables_data')
def tables_data():
   return render_template('tables-data.htmll')

@app.route('/charts_chartjs')
def charts_chartjs():
   return render_template('charts-chartjs.html')

@app.route('/charts_apexcharts')
def charts_apexcharts():
   return render_template('charts-apexcharts.html')

@app.route('/charts_echarts')
def charts_echarts():
   return render_template('charts-echarts.html')

@app.route('/icons_bootstrap')
def icons_bootstrap():
   return render_template('icons-bootstrap.html')

@app.route('/icons_remix')
def icons_remix():
   return render_template('icons-remix.html')

@app.route('/icons_boxicons')
def icons_boxicons():
   return render_template('icons-boxicons.html')

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 5000, debug = True)