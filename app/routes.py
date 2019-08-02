# from app import app
# from flask import render_template, request
# from app.models import model, formopener
from app import app
from flask import render_template, request
from app.models import model, formopener
from flask import render_template
from flask import request
from app import food_calories

@app.route('/')
@app.route('/index')
def index():
    return render_template ("index.html")

@app.route('/cal_intake', methods=['GET','POST'])
def cal_intake():
    #if it's a GET request, send them back to fill out form
    #if it's a POST request, do the following:
    #save all user data from the form (line 24 in other file)
    #take each useful piece of info from form, save to variables (convert data types)
    #do calculation
    #send to results page with info
    if request.method=='GET':
        return render_template("index.html")
    else:
        userdata = request.form
        print (userdata)
        weight=userdata["weight"]
        height=userdata["height"]
        age=userdata["age"]
        female_intake = (10.0 * float(weight) * 0.4536) + (6.25 * float(height) * 2.54) - (5.0 * float(age)) - (161.0)
        male_intake= (10.0 * float(weight) * 0.4536) + (6.25 * float(height) * 2.54) - (5.0 * float(age)) + (5.0)
        gender=userdata["gender"]
        if gender== "female":
            intake = round(female_intake)
        else:
            intake = round(male_intake)
        return render_template("cal_intake.html", weight=weight, height=height, age=age, gender=gender, calories = intake)
        
@app.route('/results', methods=['GET','POST'])
def results():
    userdata = request.form
    input_food = userdata["calsEaten"]
    food_cals = food_calories.food.get(input_food)
    cal_intake = int(userdata["cal_intake"])
    remaining_cals = cal_intake - food_cals
    if request.method=="POST":
        return render_template("results.html", remaining_cals=remaining_cals, food=input_food, cals=food_cals)
    else:
        for food in food: 
            print(remaining_cals)
            

@app.route('/about')
def about():
    return render_template("about.html")
            
    
    
    
    
    
    # if request.method=='GET':
    #     female_intake= (10 * weight * .4536) + (6.25 * height * 2.54) - (5 * age) - 161
    #     male_intake= (10 * weight * .4536) + (6.25 * height * 2.54) - (5 * age) + 5 
    #     return render_template("cal_intake.html", female_intake=female_intake, male_intake=male_intake)
    
