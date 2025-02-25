print("Number of Duplicates:", df.duplicated().sum())

df2 = df[['Cooking_With']].copy()
df2['Cooking_With_Grill'] = df2['Cooking_With'].apply(lambda x: 1 if "Grill" in x else 0)
df2['Cooking_With_Airfryer'] = df2['Cooking_With'].apply(lambda x: 1 if "Airfryer" in x else 0)

print("4992 people have both an air fryer and a grill, 5008 people have neither. No one has only one of the two devices.")
pd.DataFrame(df2.groupby(["Cooking_With_Airfryer","Cooking_With_Grill"]).size())
-----------------------------------------------------------------------------------------------------------------------------------
print("unique values:", set([item for sublist in df['Cooking_With'].unique() for item in eval(sublist)]))

# Remove "Airfryer" from the 'Cooking_With'-variable
df['Cooking_With'] = df['Cooking_With'].str.replace(", 'Airfryer'", "")

# Check if the removal was successful
print("unique values:", set([item for sublist in df['Cooking_With'].unique() for item in eval(sublist)]))
---------------------------------------------------------------------------------------------------------------------------
df.isna().sum()
-----------------------------------------------------------------------------------------------------------------------------
df_nan = df[["Transport","Vehicle_Type"]].copy()

df_nan['Vehicle_Type'] = df_nan['Vehicle_Type'].fillna('NaN') # to see the NaN in the code below

pd.DataFrame(df_nan.groupby(["Transport","Vehicle_Type"]).size())
------------------------------------------------------------------------------------------------------------------------------

#test: if "Transport"=="public transport" then "Vehicle Type"==NaN
assert df[df["Transport"]=="public"]["Vehicle_Type"].isna().all()  #wenn in der Liste alle True sind, kommt ein True raus dh stellt sicher das alle true sind #assert tut gar nichts bei True aber bei False macht Fehlermeldung und hört auf

#test: if "walk/bicycle" then "Vehicle Type"==NaN
assert df[df["Transport"]=="walk/bicycle"]["Vehicle_Type"].isna().all()  #wenn in der Liste alle True sind, kommt ein True raus dh stellt sicher das alle true sind #assert tut gar nichts bei True aber bei False macht Fehlermeldung und hört auf

#test: if "Transport"=="private" then "Vehicle Type"!=NaN
assert not ((df["Transport"]=="private") & (df["Vehicle_Type"].isna())).any() #any weil gibt es irgendein True? False heißt es gibt kein einziges True
------------------------------------------------------------------------------------------------------------------------------------
df3 = df[['Transport','Vehicle_Type']].copy()

df3['Transport_Vehicle_Type'] = df3['Vehicle_Type'].fillna(df3['Transport'])
df3['car_owner'] = (df3['Transport'] == 'private')  # aufpassen ob 'car' oder 'private' heißt

df3['Vehicle_Type'] = df3['Vehicle_Type'].fillna('NaN') # to see the NaN in the code below

# to see that: 'Transport_Vehicle_Type' & 'car_owner' hold the same information as 'Transport' & 'Vehicle_Type'.
pd.DataFrame(df3.groupby(['car_owner',"Transport","Vehicle_Type",'Transport_Vehicle_Type']).size())
--------------------------------------------------------------------------------------------------------------------------------------
print("The entries in Recycling are of type:", type(df['Recycling'][3]), "However for encoding we need to change the datatype to list.\nHere you see an example of an entry that clearly is of type string")
df['Recycling'][3]
----------------------------------------------------------------------------------------------------------------------------------
def create_dummy_variables_with_mlb(df, column_name):

    # because the data is stored as a string instead of a list
    df[column_name] = df[column_name].apply(eval)

    mlb = MultiLabelBinarizer()
    binarized_data = mlb.fit_transform(df[column_name])
    binarized_df = pd.DataFrame(binarized_data, columns=mlb.classes_)

    df = pd.concat([df, binarized_df], axis=1)
    df = df.drop(columns=column_name)

    return df

df = create_dummy_variables_with_mlb(df, 'Recycling')
df = create_dummy_variables_with_mlb(df, 'Cooking_With')

df.head()
------------------------------------------------------------------------------------------------------------------------------
numeric_features = ['Monthly_Grocery_Bill', 'Vehicle_Monthly_Distance_Km', 'Waste_Bag_Weekly_Count', 'How_Long_TV_PC_Daily_Hour', 'How_Many_New_Clothes_Monthly', 'How_Long_Internet_Daily_Hour']

nominal_multi_answer_features=['Glass','Metal','Paper','Plastic','Grill','Microwave','Oven','Stove']

# Ordinal Variables & Single-Select Nominal Features
categorical_features = ['Body_Type','Diet','How_Often_Shower','Social_Activity','Frequency_of_Traveling_by_Air','Waste_Bag_Size','Energy_efficiency'] + ['Gender','Heating_Energy_Source'] #,'Transport_Vehicle_Type']
-------------------------------------------------------------------------------------------------------------------------------------
all_columns=set(["CarbonEmission",'Vehicle_Type', 'Transport']).union(
    numeric_features,
    categorical_features,
    nominal_multi_answer_features)

assert all_columns  == set(df.columns.tolist())
---------------------------------------------------------------------------------------------------------------------------------------

