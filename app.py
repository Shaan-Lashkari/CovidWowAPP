from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")

def visitors():

	
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	
	visitors_count = visitors_count + 1

	
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()


	return render_template('index.html',cnt=visitors_count)

@app.route("/",methods=['POST'])


def covid_stats():
	
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	
	country = request.form['con_name']
	link = 'https://covidstats-sdbd.onrender.com/?country='+ country
	print(link)
	return render_template('index.html',image=link,count=visitors_count)


if __name__ == "__main__":

	app.run()	