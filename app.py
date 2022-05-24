from flask import Flask, jsonify, render_template, request, redirect
import requests, json

app = Flask(__name__)
key = ""

with open('API_KEY.json', 'r') as file_to_read:
    json_data = json.load(file_to_read)
    key = json_data["API_KEY"]  

@app.route("/")
def index():
    #return index
    return render_template("index.html")

@app.route("/weather")
def weather():
    # get city value then consult weather app, get results and present them to index
    city = request.args.get("city")
    if city:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}")
        return data.content
              
@app.route("/current")
def current():
    #get latitude and longitude, then make reques to api and return data, else return false
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    if lat and lon:
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={key}")
        return data.content
    return False        
    
if __name__ == '__main__':
    app.run(debug = True)

