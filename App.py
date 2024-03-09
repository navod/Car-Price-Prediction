from flask import Flask, render_template, request
import joblib 
import pandas as pd 


 
# Create DataFrame


 


#dn['Price']=xgb_model.predict(testDfNew)




import os

current_dir = os.path.dirname(__file__)
template_folder = os.path.join(current_dir, 'templates')

Dmodel=joblib.load("modal.sav")

app = Flask(__name__, template_folder=template_folder)

@app.route("/", methods=["GET", "POST"])
def gender_form():
    if request.method == "POST":
        dt = {'Brand':[],'Model':[],'Year':[],'Millege':[],'Fuel Type':[],'Speed':[],'Litre':[],'Transmission':[],
        'Exterior_Color':[],'Interior_Color':[],'Accident':[],'Clean':[],'Cylinder':[],'Turbo':[],
        'EngineType':[],'HP':[],'V':[],'PDI':[],'TFSI':[],'GDI':[]
        ,'SOHC':[],'DOHC':[],'Straight':[],'AT':[],'Automatic':[],'Auto_Shift':[]
        ,'Dual_Shift_Mode':[],'CVT':[],'Overdrive':[],'MT':[]}

        dn = {'Price':[]}
        #dt['Brand'] = int(request.form["Brand"])
        brand = int(request.form["Brand"])
        model = int(request.form["Model"])
        Year = int(request.form["Year"])
        Millege = int(request.form["Millege"])
        Fuel = int(request.form["Fuel"])
        Litre = int(request.form["Litre"])
        Transmission = int(request.form["Transmission"])
        Speed = float(request.form["Speed"])
        Exterior_Color = int(request.form["Exterior Color"])
        Interior_Color = int(request.form["Interior Color"])
        Accident = int(request.form["Accident"])
        Clean = int(request.form["Clean Title"])
        Cylinder = int(request.form["Cylinder"])
        Turbo = int(request.form["Turbo"])
        EngineType = int(request.form["EngineType"])
        HP = int(request.form["HP"])
        V = int(request.form["V"])
        PDI = bool(request.form["PDI"])
        TFSI = bool(request.form["TFSI"])
        GDI = bool(request.form["GDI"])
        SOHC = bool(request.form["SOHC"])
        DOHC = bool(request.form["DOHC"])
        Straight = int(request.form["Straight"])
        AT = int(request.form["AT"])
        Automatic = int(request.form["Automatic"])
        Auto_Shift = int(request.form["Auto_Shift"])
        Dual_Shift_Mode = int(request.form["Dual_Shift_Mode"])
        CVT = int(request.form["CVT"])
        Overdrive = int(request.form["Overdrive"])
        MT = int(request.form["M/T"])
        # Process the selected gender here (e.g., store in database, display message)



        dt['Brand']=[brand]
        dt['Model']=[model] 
        dt['Year']=[Year] 
        dt['Millege']=[Millege] 
        dt['Fuel Type']=[Fuel] 
        dt['Speed']=[Litre] 
        dt['Litre']=[Transmission] 
        dt['Transmission']=[Speed] 
        dt['Exterior_Color']=[Exterior_Color] 
        dt['Interior_Color']=[Interior_Color] 
        dt['Accident']=[Accident] 
        dt['Clean']=[Clean] 
        dt['Cylinder']=[Cylinder] 
        dt['Turbo']=[Turbo] 
        dt['EngineType']=[EngineType] 
        dt['HP']=[HP]
        dt['V']=[V] 
        dt['PDI']=[PDI] 
        dt['TFSI']=[TFSI]
        dt['GDI']=[GDI] 
        dt['SOHC']=[SOHC] 
        dt['DOHC']=[DOHC] 
        dt['Straight']=[Straight] 
        dt['AT']=[AT] 
        dt['Automatic']=[Automatic] 
        dt['Auto_Shift']=[Auto_Shift] 
        dt['Dual_Shift_Mode']=[Dual_Shift_Mode] 
        dt['CVT']=[CVT] 
        dt['Overdrive']=[Overdrive] 
        dt['MT']=[MT] 
        #print(dt)
        dt = pd.DataFrame(dt)
        dn = pd.DataFrame(dn)

        #dn.to_csv('outNew.csv', index=False)
        #dt.to_csv('out.csv', index=False)

        dn['Price']=Dmodel.predict(dt)
        #pr=dn['Price'].astype('int64')
        pr=dn['Price']*10
        #pr=pr[1]
        pr=round(pr, 2)
        pr=pr.to_string()
        pr=pr[1:]
        msg = "Price is Rs. "+pr+"      \n"+"\n"
        print(pr)
        return render_template('index.html', message=msg)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
