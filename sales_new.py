#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import streamlit as st
import pickle


# In[ ]:


#loading the saved model
load_model=pickle.load(open('/home/saurabh/trained_model_new.sav','rb'))








# In[ ]:


#creating function for predection
def weekely_sales_predict(input_data):
#     input_data=(45,0,9,2,118221,50,3.046,10000,10000,10000,10000,5,4,2012,15)
    #changing input data into numpy array
    np_array=np.asarray(input_data)
    #reshape array as we are predecting for one instance
    input_reshaped=np_array.reshape(1,-1)
    predict=load_model.predict(input_reshaped)
    return predict
    
    
#def add_variables():
    # Define default variables
  
    # Create dropdown widget
    #variable_selection = st.selectbox('Select a variable', [ 'markdown1', 'markdown2', 'markdown3','markdown4'])

    # Set default values
   # variable_value = st.slider(variable_selection, value=defaults[variable_selection])  
    #MarkDown1 = st.slider('markdown1', value=5000)
   # MarkDown2= st.slider('markdown2', value=10000)
    #MarkDown3 = st.slider('markdown3', value=20000)
  #  MarkDown4 = st.slider('markdown4', value=5000)  
    
def main():
# Add custom CSS
   
    #st.set_page_config(page_title="My Streamlit App",page_icon=":smiley:",layout="wide",initial_sidebar_state="expanded",background_image="https://thumbs.dreamstime.com/z/aisle-view-tesco-lotus-supermarket-nonthaburi-thailand-august-august-world-s-second-58488775.jpg")

   
  
    #giving title 
    image = st.image("https://png.pngtree.com/background/20210710/original/pngtree-shopping-mall-supermarket-selection-merchandise-poster-background-material-picture-image_1048684.jpg")
    #add_variables()
    st.title("WEEKELY SALES PREDECTION WEB APP")
    
    
    #getting input data from user
    store =st.text_input("which store do you want")
    Isholiday =st.text_input("status of weekely holiday")
    Dept =st.text_input("which department(1-98)")
   # Type =st.text_input("which type of department(1/2/3)")
  # import streamlit as st

    type_options = ["1", "2", "3"]
    Type = st.selectbox("Select department type", type_options)
    if Type:
        st.write(f"You selected department type {Type}.")
    Size =st.text_input("sq.ft size of your department")
    Temprature =st.text_input("temperature")
    Fuel_Price =st.text_input("fuel_price")
    markdown1=st.text_input("offer1")
    markdown2=st.text_input("offer2")
    markdown3=st.text_input("offer3")
    markdown4=st.text_input("offer4")
    Date_month =st.text_input("which day of week")
    Date_day=st.text_input("which month")
  #  year=st.text_input("which year")
   # date_day=st.text_input("which day_date")
    
    #code for predection
    sales= ''
    
    #creating button for predection
    
    if st.button("sales predection result"):
        #sales=weekely_sales_predict([store_number,holiday_status,department_no,type_department,size_department,temprature_weekely_average ,fuel_price_dollars,dayofweek,month,year,date_day])
         sales=weekely_sales_predict([store, Isholiday, Dept, Type, Size, Temprature,
       Fuel_Price, markdown1, markdown2, markdown3, markdown4,
       Date_month, Date_day])
    
    
    st.success(sales)

    
    
if __name__ == '__main__':
    main()

