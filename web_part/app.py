from flask import Flask,render_template,jsonify,url_for,request,flash,redirect

import datetime
import my_calc as mc



app =Flask(__name__)

samples=["1 1 * 2 ? 1 + (3 ?* 2 ?/ 1 + 3 )?* 2 ? 1 + 3 ? * 7 ? + 8 7 9 ?",
"1+2+3?5-4-3?-4-6?-2",
"1+2?+3?*(5?-4?-(3?-4)-6)?+1"]


@app.route('/')
def index():
    return render_template("index.html",samples=samples)
    # return render_template("index.html")

@app.route('/begin_select', methods=["GET","POST"])
def mapping_select():
    try:
        data = request.form['select_map']
        print(data)
        res=mc.main_yeilder(data)
        res=res.split("\n")
        print(res)
        
        y_data=[round(float(x.split('=')[-1].strip()),2) for x in res if '=' in x]
        x_data=list(range(len(y_data)))
        # x_data=[x for x in x_data]
        return render_template("index.html",samples=samples,data=data,res=res,x_data=x_data,y_data=y_data)
        # return redirect(url_for('leverage',job=job))
    except Exception as e:
        print(e)
        return(e)

if __name__ == "__main__":
    # website_url = 'DataIntegration.ETL.DIP:5000'
    # app.config['SERVER_NAME'] = website_url
    app.run()
