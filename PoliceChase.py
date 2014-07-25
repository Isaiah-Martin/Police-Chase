from flask import Flask, request
app = Flask(__name__)




def surrender():
	return "You got on your knees and let the cops take You"

def Avatar_Image(skin,gender):
	skin = int(skin)
	if gender == 'girl':
		if skin <= 15:
			return "<img src= 'http://volkundvaterland.files.wordpress.com/2013/07/white-nordic-woman.jpg'>"
		elif skin <= 25:
			return "<img src= 'http://ak5.picdn.net/shutterstock/videos/1023682/preview/stock-footage-pretty-young-chinese-woman-eating-noodles-from-a-bowl-with-chopsticks.jpg'>"
		elif skin <= 50:
			return "<img src='http://www.volveralamor.mx/images/gallery/MariaM.jpg'>"
		elif skin <= 75:
			return "<img src='http://s2.hubimg.com/u/7942445_f260.jpg'>"
		else:
			return "<img src= 'http://thyblackman.com/wp-content/uploads/2011/08/darkskin.jpg' width='407' height='331'>"
	else:
		if skin <= 15:
			return "<img src= 'http://1.bp.blogspot.com/_N2EyyrA_LPs/S9LpXXVf82I/AAAAAAAAIc0/mg_jA4o1r9k/s400/whiteboy.jpg'> "
		elif skin <= 20:
			return "<img src= 'http://i00.i.aliimg.com/wsphoto/v0/891218646/Present-Hair-Net-font-b-2013-b-font-new-arrival-wigs-Male-wig-stubbiness-oblique-bangs.jpg'> "
		elif skin <= 50:
			return "<img src= 'http://bloximages.chicago2.vip.townnews.com/nogalesinternational.com/content/tncms/assets/v3/editorial/a/f4/af432074-6989-11e3-a2e6-0019bb2963f4/52b45f560c5ce.preview-300.jpg'> "
		elif skin <= 75:
			return "<img src= 'http://uppitynegronetwork.files.wordpress.com/2008/05/boris-kodjoe.jpg'> "
		else:
			return "<img src= 'http://www2.pictures.stylebistro.com/gi/Lance+Gross+Classic+Sunglasses+Aviator+Sunglasses+_iO9EAGsmjAl.jpg'> "


@app.route("/")
def form_info():
    html_code= '<form background="" name= "name" action="/submit" method="POST">'
    html_code = html_code + 'Nickname:<input type="text" name = "user" placeholder = "Enter Nickname"><br><br>'
    html_code= html_code + 'Birthday<input type="text" name = "bday" placeholder = "Enter Birthday"><br><br><br>Motto<br>'
    html_code= html_code+ '<textarea name = "motto" row= "20" cols="40" placeholder = "What Code Do You Live By?" value = "motto"> </textarea><br><br>'
    html_code= html_code +  'Gender: <input type="radio" name="gender" value="boy"> Boy'
    html_code = html_code+ '<input type="radio" name="gender" value="girl"> Girl <br><br>'
    html_code= html_code+ 'Location: <input type="text" name = "loc" placeholder = "Enter Game Setting"><br><br>'
    html_code= html_code+ '<form oninput="x.value=skin_tone.valueAsNumber">'
    html_code=html_code+ 'Skin Tone (on a scale of 100 from lightest to darkest) <br> 0 <input type="range" id="tone" name="skin" oninput="thisRate.value = tone.value" value="50"> 100<output name="x" for="tone"></output><br><br>'
    submit = "<input type='submit' action = '/submit' value='Submit' method='POST'></form>" + '</form>'
    return  html_code + submit



@app.route('/submit', methods=['POST'])
def Submit():
	Username = request.form['user']
	Birthday = request.form['bday']
	Location = request.form['loc']
	Motto = request.form['motto']
	Gender = request.form['gender']
	Skin = request.form['skin']


	E = "<body background= 'http://newevolutiondesigns.com/images/freebies/urban-landscape-wallpaper-19.jpg'><body style= color:yellow link='white' vlink='yellow'>"
	A = "Okay <i>%s</i>, before we start, this is your avatar.<br><br>" % (Username)
	I = "" + (Avatar_Image(Skin,Gender)) + "<br><br>"
	U = "<b>Your Nickname is </b><i>%s</i><br><br>" %  (Username)
	B = "<b>The day of your birthday is </b><i>%s</i><br><br>" % (Birthday)
	Q = "<b>The code you live by is </b><i>%s</i><br><br>" % (Motto)
	G = "<b>Your gender is </b><i>%s</i><br><br>" % (Gender)
	T = "<b> Your Skin Tone (on a scale of 100 from lightest to darkest) is </b><i>%s</i><br><br>" % (Skin)
	S = "<b>And the Setting of the Scene is</b> = <i>%s</i><br><br>" % (Location)
	C = "<br><br>Good?<br><br> Click 'Begin Play to begin play or back to make some changes to your avatar'<br><br> <a href='/Choice'>Option 1: Begin Play</a><br><br> <a href='/'>Option 2: Back</a></body>"

	master_var =E + A + I + U + B + Q + G + T + S + C
	return master_var

@app.route("/Choice")
def Statements():
    	I = '<body background= "http://2.bp.blogspot.com/_aaVprncJvaA/TB_9gTv7jKI/AAAAAAAAA9g/CCOtUKx8GCE/s400/screen-capture-38.png"><body style= color:yellow link="yellow" vlink="yellow"><img src="http://tucsoncitizen.com/morgue/files/2006/07/l18414-2.jpg">'
    	T ='<br><br>Hey!<br><br>You were caught commiting a terrible crime<br><br> Your hands are up.<br><br>' 
    	K ='The cop said put your hands up.<br><br> What are you gonna do?<br><br> I dare you to reply "No"! and ran away. <br><br>But you do not have the guts to do that<br><br>'
    	F = 'You have a bright future ahead of you.<br><br>But it is dimming now as time goes by and you must decide <br><br>to endure years locked up in prison or take the small chance you have of a future<br><br>' 
    	A = '<a href= "/S">Option 1: Surrender</a><br><br><a href= "/1">Option 2: Shoot a cop</a><br><br><a href="/2">Option 3: Hijack a car</a><br><br><a href="/3">Option 4: Hijack an aircraft</a>' 
    	master_var = I+T+F+K+A
    	return master_var

@app.route("/S")
def surrender():
	B = '<body background="http://dellinolaw.com/wp-content/uploads/2013/10/arrested.png"><body style= color:brown link="brown" vlink="brown"><br><br>'
	O = "<br><br>You got on your knees,<br><br><br> Put your hands up and let the cops take you to prison.<br><br><br> Your future lies in the prison cells now.<br><br><br> Make the most of it.<br><br>"
	L = '<a href= "/Choice">Option 1: Back</a><br><br><a href= "/">Option 2: Start Over</a>'
	master_var = B+O+L
	return master_var

@app.route("/1")
def shoot():
	
	return '<body background="http://2.bp.blogspot.com/_aaVprncJvaA/TB_9gTv7jKI/AAAAAAAAA9g/CCOtUKx8GCE/s400/screen-capture-38.png""><body style= color:yellow link="yellow" vlink="yellow"><br><br>' + "You shot cop 1 in the face.<br><br>You ran away to escape.<br><br>You ran away to a biulding<br><br>and blended in as a hidden genius in the Hidden Genius Project.<br><br><a href='/'>Start Over<br><br>" 


@app.route("/2")	
def drive():
	return '<body background="http://2.bp.blogspot.com/_aaVprncJvaA/TB_9gTv7jKI/AAAAAAAAA9g/CCOtUKx8GCE/s400/screen-capture-38.png""><body style= color:yellow link="yellow" vlink="yellow"><br><br>'+ 'You took an SUV,<br><br> and drove off to Oakland.<br><br>And blened in as a <br><br>hidden genius in the Hidden Genius Project.<br><br><a href="/">Start Over<br><br> '

@app.route("/3")	
def aircraft():
	return '<body background="http://2.bp.blogspot.com/_aaVprncJvaA/TB_9gTv7jKI/AAAAAAAAA9g/CCOtUKx8GCE/s400/screen-capture-38.png""><body style= color:yellow link="yellow" vlink="yellow"><br><br>'+ 'You took an aircraft, <br><br>and flied to Oakland.<br><br>And Blended in as a <br><br>hidden genius in the Hidden Genius Project.' + "<br><br><a href='/'>Start Over<br><br>" 

if __name__ == "__main__":
	app.debug = True
	app.run('0.0.0.0')



