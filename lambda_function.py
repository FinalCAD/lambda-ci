from flask_api import FlaskAPI, status

def lambda_handler(event, context):
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name'])  
    return { 
        'message' : message
    }

app = FlaskAPI(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "", status.HTTP_200_OK
app.run()
