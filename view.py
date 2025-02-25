df = pd.read_csv('/content/carbon emission mitigation 1.csv')

# change display settings to show all columns
pd.set_option('display.max_columns', None)

#rename
# rename columns: replace spaces with underscores
df.columns = df.columns.str.replace(' ', '_')

# convert Gender to Boolean-datatyp
df.rename(columns= {'Sex':'Gender'}, inplace = True)
df.head()

print("Full dataset shape is", df.shape)
##############################################

# Berechnet den maximalen Wert einer Spalte, wenn sie numerisch ist
def max_value(column):
    if pd.api.types.is_numeric_dtype(column):  # Überprüfe, ob der Datentyp numerisch ist
        return column.dropna().max() if not column.dropna().empty else np.nan
    return ""

# Gibt die einzigartigen Werte einer Spalte zurück, oder eine Range (falls es eine gibt)
def get_unique_values(column):
    if pd.api.types.is_integer_dtype(column):  # Überprüfe, ob der Datentyp eine Ganzzahl ist
        unique_vals = sorted(set(column.dropna()))
        min_val, max_val = column.min(), column.max()
        if unique_vals == list(range(min_val, max_val + 1)):
            return f"range({min_val},{max_val + 1})"
        return unique_vals
#        return f"between {min_val} and {max_val}"
    return sorted(set(column.dropna()))


def summary(df=df):
    summary_df = pd.DataFrame({
        'data type': df.dtypes.astype(str),
        'missing data': df.isna().sum(),
        'unique values': [get_unique_values(df[col]) for col in df.columns],
        'unique values max': [max_value(df[col]) for col in df.columns],
        'Cardinality': df.nunique()
    })
    return summary_df


# Sortiere nach 'data type' und dann nach 'number of unique values'
summary_df = summary(df).sort_values(by=['data type', 'Cardinality'])




max_length_col = len(str("'Stove', 'Oven', 'Microwave', 'Grill', 'Airfryer'"))+2
pd.set_option('max_colwidth', max_length_col + 1) #Set the Column Width #You can increase the width by passing an int. Or put at the max passing None:
#pd.set_option('max_colwidth', None) #Set the Column Width #You can increase the width by passing an int. Or put at the max passing None:
#pd.reset_option('max_colwidth') #Rückgängig machen

summary_df.loc['Vehicle_Type', 'unique values'] = ', '.join(['diesel', 'electric', 'hybrid', 'lpg', 'petrol']) #ist string statt Liste
#summary_df.loc['Vehicle_Type', 'unique values'] = ['diesel', 'electric', 'hybrid', 'lpg', 'petrol'] #macht Fehlermeldung

#change values for "Recycling" & "Cooking_With"

for headline in ["Recycling" ,"Cooking_With"]:
    unique_values= set([item for sublist in df[headline].unique() for item in eval(sublist)]) #eval - Convert string representation of list to an actual list

    summary_df.loc[headline,'unique values'] = str(unique_values)
    summary_df.loc[headline,'Cardinality'] = len(unique_values)


# Setze die maximale Breite einer Spalte auf None, um keine Begrenzung zu haben
#pd.set_option('display.max_colwidth', None)

summary_df

#describe__dataset

df.describe()
