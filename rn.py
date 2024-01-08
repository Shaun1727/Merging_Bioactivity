import pandas as pd 

assay_data = pd.read_csv("./BROAD_assay_data_filtered_89_inchi.csv") 
print(assay_data)
# columns_drop = assay_data.columns[1:-1]
# df_dropped = assay_data.drop(columns=columns_drop, inplace=False)
# # print(columns_drop)
# CP_features = pd.read_csv("./BROAD_CP_filtered_15272(1).csv") 

# assay_and_cp_features_along_with_smiles = pd.merge(df_dropped,CP_features)

# assay_and_cp_features_along_with_smiles.to_csv("assay_and_cp_features_along_with_smiles.csv") 