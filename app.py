import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px


df = pd.read_csv("/content/train.csv",date_parser='date')

st.set_page_config(
  page_title = 'Real-Time data science Dashboard',

  page_icon = '✅',
    
  layout='wide'  

)

st.title("Real-Time/ Live Data Science Dashboard")

family_filter = st.sidebar.selectbox("Select the family", str(pd.unique(df['family'])).title())


placeholder = st.empty()

df = df[df['family'] == family_filter]

for seconds in range(200):
    
    #df['sales_new'] = df['sales'] * np.random.choice(range(1,5))
    
    #df['onpromotion_new'] = df['onpromotion'] * np.random.choice(0.1,0.4)
    
    # Creating KPIs
    #df['sales_new'] = pd.fillna(pd.to_numeric(df['sales'], errors='coerce'), df.sales.mean)
    avg_sales = np.mean(df['sales'])
    
    
    count_stores = int(df.store_nbr.count() + np.random.choice(range(1,10)))
    
    avg_promotion = np.mean(df.onpromotion)


    with placeholder.container():
        
        kpi1, kpi2, kpi3 = st.columns(3)
        
        kpi1.metric(label="Sales", value= f"$ {round(avg_sales)}", delta= round(avg_sales) )
  
        kpi2.metric(label="Stores count", value= round(count_stores), delta= -5 + count_stores)
                    
        kpi3.metric(label="Promotion percentage", value= f"{round(avg_promotion,3) * 100} %", delta= - round(avg_promotion) * 100 )
                    
                    
    # Create two columns for charts 
    
    fig_col_1, fig_col_2 = st.columns(2)
    
    with fig_col_1:
        
        st.markdown("### First Chart")
        
        fig = px.density_heatmap(data_frame=df,y='onpromotion', x='sales')
        
        st.write(fig)
        
    with fig_col_2:
        
        st.markdown("### Second Chart")
        
        fig = px.bar(data_frame=df, y='sales', x='date')
        
        st.write(fig)
           
            
    st.markdown("### Detailed Data View")
    
    st.dataframe(df)
    
    time.sleep(1)

    if __name__ == '__main__':
       st.run_server(debug=True)
                    