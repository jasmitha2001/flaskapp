name=''
from .data.about import bot
from .code import *
def get_intent(data):
    global name 
    m=data['message'].lower()
    if data['key']=="name":
        name=m
        return "next"
    if data['key']=="city":
        return "weatherresult"
    if data['key']=="country":
        return "coronaresult"
    if data['key']=="expression":
        return "evaluateresult"

    if any(x in m for x in ["weather","weatherdetails"]):
        return "weather"
    elif any(x in m for x in ["corona","Corona","covid","covid19","covid 19"]):
        return "corona"
    elif any(x in m for x in ["calculate","Calculate","Evaluate","eval","Eval","evaluate","evaluation","Evaluation","expression","Expression","Calculation","calculation"]):
        return "evaluate"
    elif any(x in m for x in ["end","close","bye","Bye"]):
        return "end"
    elif any(x in m for x in ["hy","hi","Hi","Hy","Hello","hello"]):
        return "next"
    else:
        return "echo"

def handle(data):
    global name 
    from flask import render_template
    intent=get_intent(data)
    if intent == 'next':
        return render_template('messages/greet.html',name=name,
        question={'key':'request','text':'What would you like to do?'})
    elif intent == 'weather':
        return render_template('messages/weatherintro.html',name=name,
        question={'key':'city'})
    elif intent == 'weatherresult':
        return render_template('messages/cityweatherintro.html',data=bot,wdata=weather_report(data['message']),name=name,
        question={'key':'response'})
    elif intent == 'corona':
        return render_template('messages/coronaintro.html',name=name,
        question={'key':'country'})
    elif intent == 'coronaresult':
        return render_template('messages/countrycoronaintro.html',data=bot,wdata=corona_updates(data['message']),name=name,
        question={'key':'response'})
    elif intent == 'evaluate':
        return render_template('messages/evaluateintro.html',name=name,
        question={'key':'expression'})   
    elif intent == 'evaluateresult':
        return render_template('messages/exprevaluateintro.html',data=bot,wdata=evaluate_expression(data['message']),name=name,
        question={'key':'response'}) 
    elif intent == "end":
        return render_template('messages/endintro.html',name=name,
        question={'key':'Restart'}) 
    else:
        return render_template('messages/echo.html',data=data)