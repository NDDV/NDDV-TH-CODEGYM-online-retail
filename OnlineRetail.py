#%%
import pandas as pd
data=pd.read_csv('OnlineRetail.csv', encoding = "ISO-8859-1")
data.head()

# %%
data.info()

# %%
country = data.Country.unique()
print ("số lượng các quốc gia: " + str(country.size))

# %%
data['total'] = data['Quantity'] * data['UnitPrice'] 

total_invoices = data['total'].sum()
print ("số lượng hóa đơn bán ra: "+ str (total_invoices.size))
print ("Tổng doanh thu: " + str(total_invoices.sum()))

# %%
quantity_product = data.groupby(['StockCode', 'Description'])['Quantity'].sum().sort_values(ascending= False)
quantity_product.head(10)

# %%
quantity_product = data.groupby(['StockCode', 'Description'])['total'].sum().sort_values(ascending= False)
quantity_product.head(10)