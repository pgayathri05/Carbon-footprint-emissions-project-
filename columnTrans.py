# for 'Vehicle_Type' and 'Transport':
def transport_custom_impute(X):
    # Ersetze NaN in Vehicle_type mit den Werten aus Transport
    X['Transport_Vehicle_Type'] = X['Vehicle_Type'].fillna(X['Transport'])
    return X[['Transport_Vehicle_Type']]

transport_pipeline = Pipeline(steps=[
    ('transport_imputer', FunctionTransformer(transport_custom_impute, validate=False)),
    ('onehot', OneHotEncoder(drop="first"))
])

preprocessor = ColumnTransformer(transformers=[
        ("numerical", MinMaxScaler(), numeric_features),
        ("transport_vehicletype", transport_pipeline, ['Vehicle_Type', 'Transport']),
        ("categorical", OneHotEncoder(drop="first"), categorical_features)
    ],remainder="passthrough")

X = df.drop(["CarbonEmission"], axis=1)
X_transformed = preprocessor.fit_transform(X)

# To see the ColumnTransformer
preprocessor

------------------------------------------------------------------------------------------------------------------------
def get_passthrough_columns(column_transformer, X):
    """
    Extracts the columns that are passed through without transformation in the ColumnTransformer.

    Args:
        column_transformer (ColumnTransformer): Fitted ColumnTransformer object.
        X (pd.DataFrame): Original DataFrame before transformation.

    Returns:
        List[str]: List of column names that are passed through.
    """
    passthrough_indices = column_transformer.transformers_[-1][-1]
    return X.columns[passthrough_indices].tolist()


def get_identity_columns(column_transformer, begin_index, end_index):
    """
    Extracts the columns from the ColumnTransformer that remain unchanged in terms of their structure,
    meaning they undergo transformations but  the column number remains the same.

    Args:
        column_transformer (ColumnTransformer): Fitted ColumnTransformer object.
        begin_index (int): Starting index of the identity transformers.
        end_index (int): Ending index (exclusive) of the identity transformers.

    Returns:
        List[str]: List of column names that remain unchanged in number.
    """
    col_names = []
    for _, _, col in column_transformer.transformers_[begin_index:end_index]:
        col_names.extend(col)  # Collect all untransformed column names
    return col_names


def get_onehot_encoded_columns(column_transformer, begin_index, end_index):
    """
    Extracts the OneHotEncoded feature names for the specified transformers in the ColumnTransformer.

    Args:
        column_transformer (ColumnTransformer): Fitted ColumnTransformer object.
        begin_index (int): Starting index of the ordinal encoders.
        end_index (int): Ending index (exclusive) of the ordinal encoders.

    Returns:
        List[str]: List of one-hot encoded feature names.
    """
    ohe_feature_names = []
    for col_name, _, col_list in column_transformer.transformers_[begin_index:end_index]:
        ohe_features = column_transformer.named_transformers_[col_name].get_feature_names_out(col_list).tolist()
        ohe_feature_names.extend(ohe_features)
    return ohe_feature_names
  ------------------------------------------------------------------------------------------------------
# Spaltenanzahl bleibt gleich
# name of the first transformers (transformers index 0 till excluding index 1)
numeric_features = get_identity_columns(preprocessor, 0, 1)

# ❌ hier fehlt noch Spaltennnamen für OneHot-Encoding für Transport_Vehicle_Type❌
# Transport-Pipeline Features
transport_encoder = preprocessor.named_transformers_['transport_vehicletype'].named_steps['onehot']
transport_feature_names = transport_encoder.get_feature_names_out(['Transport_Vehicle_Type']).tolist()

# Spaltenanzahl erhöht
# name of the transformers index 1 till excluding index -1 (excluding passthrough) ❌habe von 1 auf 2 geändert wegen Transport_Vehicletyp. stimmt das? ❌
dummy_categorical_features = get_onehot_encoded_columns(preprocessor, 2, -1)

# name of the first three transformers index -1
passthrough_columns = get_passthrough_columns(preprocessor, X)

transformed_feature_names = numeric_features + transport_feature_names + dummy_categorical_features + passthrough_columns

X_transformed = pd.DataFrame(X_transformed, columns=transformed_feature_names)
--------------------------------------------------------------------------------------------------------------------
X_transformed.head()
-------------------------------------------------------------------------------------------------------------------
df.head()
------------------------------------------------------------------------------------------------------------------
