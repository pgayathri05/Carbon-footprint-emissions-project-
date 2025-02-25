X_pred = pd.DataFrame([
  ["overweight","female","pescatarian","daily","coal","walk/bicycle", np.nan,"often",230,"frequently",210,"large", 4,7,26,1,"No",False,1,0,0,True,0,0,1],
  ["obese","female","vegetarian","less frequently","natural gas","walk/bicycle", np.nan,"often",114,"rarely",9,"extra large",3,9,38,5,"No",False,1,0,0,False,1,0,1]
], columns=[ 'Body_Type', 'Gender', 'Diet', 'How_Often_Shower', 'Heating_Energy_Source',  'Transport', 'Vehicle_Type','Social_Activity','Monthly_Grocery_Bill',  'Frequency_of_Traveling_by_Air', 'Vehicle_Monthly_Distance_Km','Waste_Bag_Size','Waste_Bag_Weekly_Count', 'How_Long_TV_PC_Daily_Hour', 'How_Many_New_Clothes_Monthly', 'How_Long_Internet_Daily_Hour', 'Energy_efficiency','Glass', 'Metal', 'Plastic', 'Paper', 'Oven', 'Microwave', 'Grill', 'Stove'])

y_pred = model.predict(preprocessor.transform(X_pred)).round(0)
print("predicted CarbonEmission: ", y_pred)

X_pred



X_pred= df.loc[0:1, X.columns]
y_pred = model.predict(preprocessor.transform(X_pred)).round(0)
print("predicted CarbonEmission of first 2 persons: ", y_pred)

y_true = list(df.loc[0:1, 'CarbonEmission'])
print("actual CarbonEmission of first 2 persons: ", y_true)

X_pred
