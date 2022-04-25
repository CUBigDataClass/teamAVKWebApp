from urllib import response
from flask import Flask, redirect, render_template, request, session
import pymongo
import requests
import json

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client.get_database('total_records')
records = db.register

scrapper = "http://127.0.0.1:5001/fetchprod?name="
comparator = "http://127.0.0.1:5001/fetchcomparison?url="
# analyzer = ""
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
    response = requests.get(url = scrapper+user)
    data = response.json()
    products_list = data['result']
    products_list = products_list[0:9]
    return render_template('sample.html', user=products_list, name = user)


@app.route('/search', methods = ['post'])
def search(user=""):
    user = request.form.get('query')
    response = requests.get(url = scrapper+user)
    data = response.json()
    products_list = data['result']
    products_list = products_list[0:9]
    global reviews_list
    reviews_list = [
    {
      "shopping_results": [
        {
          "link": "https://stockx.com/air-jordan-1-retro-high-og-seafoam-ps%3Fcountry%3DUS%26currencyCode%3DUSD%26size%3D12C%26srsltid%3DAWLEVJzkme5036bgKY-I9Tszk7eGrdtI_EcMRp4PrJ536zICLpIH08E3fs4&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykIJA&usg=AOvVaw3z0n728kCMKu-6gVo5VT5e", 
          "price": "$111.00", 
          "title": "StockXOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.goat.com/sneakers/air-jordan-1-retro-high-og-ps-seafoam-cu0449-002&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykIKA&usg=AOvVaw36NXnrKBXX7SqUjC_HzMxw", 
          "price": "$116.00", 
          "title": "GOATOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.flightclub.com/air-jordan-1-retro-high-og-ps-seafoam-cu0449-002&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykILQ&usg=AOvVaw3zoP2NVVzoUvQSIOuFRw-v", 
          "price": "$116.00", 
          "title": "Flight ClubOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.kickscrew.com/products/air-jordan-1-retro-high-og-ps-seafoam-cu0449-002%3Fvariant%3D40913738498243%26currency%3DUSD%26utm_medium%3Dproduct_sync%26utm_source%3Dgoogle%26utm_content%3Dsag_organic%26utm_campaign%3Dsag_organic%26srsltid%3DAWLEVJz6tFu00CRw3bAw3-yOIanhk4qk_aoWwU1RuCf6eyDzm8M8itb8nLw&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykIMQ&usg=AOvVaw1bSc7LcmVcHg1TIigW_qso", 
          "price": "$190.00", 
          "title": "kickscrew.comOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.farfetch.com/shopping/kids/jordan-kids-air-jordan-1-retro-high-og-sneakers-item-17234149.aspx%3Ffsb%3D1%26size%3D20%26storeid%3D11218&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykINQ&usg=AOvVaw0DzWpVKj8LoI-LmndoJUsW", 
          "price": "$147.00", 
          "title": "farfetch.comOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.farfetch.com/shopping/kids/jordan-kids-air-jordan-1-retro-high-og-sneakers-item-17234149.aspx%3Ffsb%3D1%26size%3D20%26storeid%3D11218&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykINQ&usg=AOvVaw0DzWpVKj8LoI-LmndoJUsW", 
          "price": "$147.00", 
          "title": "farfetch.comOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.farfetch.com/shopping/kids/jordan-kids-air-jordan-1-retro-high-og-sneakers-item-17234149.aspx%3Ffsb%3D1%26size%3D20%26storeid%3D11218&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykINQ&usg=AOvVaw0DzWpVKj8LoI-LmndoJUsW", 
          "price": "$147.00", 
          "title": "farfetch.comOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.farfetch.com/shopping/kids/jordan-kids-air-jordan-1-retro-high-og-sneakers-item-17234149.aspx%3Ffsb%3D1%26size%3D20%26storeid%3D11218&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykINQ&usg=AOvVaw0DzWpVKj8LoI-LmndoJUsW", 
          "price": "$147.00", 
          "title": "farfetch.comOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }, 
    {
      "shopping_results": [
        {
          "link": "https://www.farfetch.com/shopping/kids/jordan-kids-air-jordan-1-retro-high-og-sneakers-item-17234149.aspx%3Ffsb%3D1%26size%3D20%26storeid%3D11218&sa=U&ved=0ahUKEwjdka356av3AhVIbs0KHWh3DyYQ2ykINQ&usg=AOvVaw0DzWpVKj8LoI-LmndoJUsW", 
          "price": "$147.00", 
          "title": "farfetch.comOpens in a new window",
          "positive" : 10,
          "neutral": 15,
          "negative": 5
        }
      ]
    }
  ]

    return render_template('sample.html', user=products_list, name = user)
#     

@app.route('/comparison', methods = ['post'])
def compare():
    # print(type(request.form.get('url')))
    global reviews_list
    print(len(reviews_list))
    pc_url = request.form.get('url')
    print(pc_url)
    index = int(request.form.get('index'))
    print(index)
    if(pc_url == ""):
        return render_template('noresults.html')
    response = requests.get(url = comparator+pc_url)
    data = response.json()
    products_list = data['result']

    return render_template('comparison.html', user = products_list, reviews = reviews_list[index])

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
   app.run(debug = True)