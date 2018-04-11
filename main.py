import pandas as pd
import math

path="D:/Tangui/2_Projet_total/base_client_et_commandes/dsi_customer_export_2018_02.csv"
clt=pd.read_csv(path, error_bad_lines=False,sep=";",encoding='utf-8')
clt=clt[~clt['clt_id'].isna()]
clt['clt_id'] = clt['clt_id'].astype(int)

path2=path.split(".csv")[0]+'_clean.csv'
clt.to_csv(path2,sep=";",encoding='utf-8')
# for i in range(0,len(clients_csv['clt_id'])):
#     if math.isnan(clients_csv['clt_id'][i]):