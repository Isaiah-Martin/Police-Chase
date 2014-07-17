from flask import Flask, request
app = Flask(__name__)


def shoot(target):
	return "You shot %s in the face. You ran away to escape." % (target)
print shoot("Cop 1")


def move(Vehicle):
	return "You took %s "% (Vehicle)
print move ("A honda and went to your Grannys House!!!!")


def surrender():
	return "You got on your knees and let the cops take You"
print surrender()

def Avatar():
	if int(skin_tone) <= 25:
		return "<img src='' alt='%s' style='height:32px;width:32px'>" % (Username)
	elif int(skin_tone <= 50):
		return "<img src='' alt='%s' style='height:32px;width:32px'>" % (Username)
	elif int(skin_tone <= 75):
		return "<img src='' alt='%s' style='height:32px;width:32px'>" % (Username)
	else:
		return "<img src='' alt='%s' style='height:32px;width:32px'>" % (Username)

@app.route("/")
def form_info():
    html_code= '<form oninput="x.value=skin_tone.valueAsNumber" name= "name" action="/submit" method="POST">'
		html_code= html_code + 'Location To Rob: <input type="text" name = "bday" placeholder = "Enter Location To Rob"><br>Motto<br>'
	html_code = html_code + '<textarea name=“motto" row= "20" cols="40" placeholder = "What Code Do You Live By?" value = "motto"></textarea><br><br>'
	html_code = html_code+  'Skin_Tone<br>0<input type="range" id="skin_tone" name="skin_tone" oninput="thisRate.value = skin_tone.value" value="50">100<br>Skin Tone = <output name="x" for="skin_tone”>50</output><br><br>'
	
	return html_code



@app.route('/submit', methods=['POST'])
def Submit():
	Username = request.form['user']
	Birthday = request.form['bday']
	Motto = request.form['motto']
	Gender = request.form['gender']
	Skin_Tone = request.form['skin_tone']

	U = "Okay %s, this is your avatar.<br><br>%s<br><br><b>Username</b> = <i>%s</i><br>" %  (Username, Avatar(Skin_Tone), Username) 
	'<b>Username</b> = <i>%s</i><br><br>' %  Username, Username 
	B = "<b>Birthday</b> = <i>%s</i><br><br>" % Birthday
	Q = "<b>The code you live by</b> = <i>%s</i><br><br>" % Motto
	G = "<b>Gender</b> = <i>%s</i><br><br>" % Gender
	Skin_Tone = "<b>Skin Tone</b> = <i>%s</i><br><br>" % Skin_Tone
	Name = "<br><br><a href='/Choice'>Begin Play</a>"

	master_var = U + B + Q + G + Name
	return master_var

@app.route("/Choice")
def Statements(num):
	Username = request.form['user']
    	Birthday = request.form['bday']
    	Quote = request.form['quote']
    	Gender = request.form['gender']

    	return '<b>%s</b>!<br>You were caught commiting a terrible crime. Your hands are up. Today is your Birthday: %s and The cop said put your hands up %s. You replied <b>"%s"<b>! and ran away. <br><br><a href= "/1">Shoot a cop</a><br><br><a href="/2">Drive</a>' % (Username,Birthday,Quote,Gender)

@app.route("/1")
def shoot(target):
	target = "cop 1"
	return "You shot %s in the face. You ran away to escape." % (target)
@app.route("/2")	

def move(Vehicle):
	Vehicle = "honda"
	return "You took %s "% (Vehicle)

if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')



