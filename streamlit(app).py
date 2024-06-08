import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('preprocessed_Alpha (3).csv')

st.image('streamlit image.jpeg')

st.title('Alpha')

st.image('fashion.png')

st.sidebar.title('Alpha Dataset')
menu=st.sidebar.radio('Menu',['About the Dataset','EDA'])
if menu=='About the Dataset':
    st.write('Shape of the Dataset:',data.shape)
    st.header('Tabular Data of Alpha')
    if st.checkbox('Tabular Data'):
        st.table(data.head(20))
    st.header('Statistical Summary')
    if st.checkbox('Statistics'):
        st.table(data.describe())
    if st.header('Correlation Graph'):
        fig,ax=plt.subplots(figsize=(20,10))
        data_num=data.select_dtypes(include=['int64','float64'])
        sns.heatmap(data_num.corr(),annot=True,cmap='coolwarm')    
        st.pyplot(fig)

if menu=='EDA':
    st.title('Data Visualisation')
    st.header('Target Variable: Sold')
    graph=st.selectbox('Different Types of Plots',['Bar Plot','Scatter Plot','Box Plot','Histogram'])
    if graph=='Bar Plot':
        variable=st.selectbox('Choose Variable',['target gender','product_category','product_season','product_condition','brand_name','product_material','seller_badge','seller_country'])
        if variable=='target gender':
            st.subheader('Product Sold by target Gender')
            fig,ax=plt.subplots(figsize=(10,5))
            sns.barplot(x='target gender',y='sold',data=data)
            st.pyplot(fig)
        if variable=='product_category':
            st.subheader('Product Sold by Category')
            fig,ax=plt.subplots(figsize=(10,5))
            sns.barplot(x='target gender',y='sold',data=data,hue='product_category')
            st.pyplot(fig)
        if variable=='product_season':
            st.subheader('Product Sold by Product Season')
            fig,ax=plt.subplots(figsize=(10,5))
            sns.barplot(x='product_season',y='sold',data=data,hue='product_category')
            st.pyplot(fig)
        if variable=='product_condition':
            st.subheader('Product Sold by Product Condition')
            fig,ax=plt.subplots(figsize=(10,5))
            sns.barplot(x='product_condition',y='sold',data=data)
            st.pyplot(fig)
        if variable=='brand_name':
            st.subheader('Product Sold by Brand Name')
            fig,ax=plt.subplots(figsize=(15,7.5))
            sns.barplot(x='brand_name',y='sold',data=data)
            plt.xticks(rotation=90)
            st.pyplot(fig)
        if variable=='product_material':
            st.subheader('Product Sold by Product Material')
            fig,ax=plt.subplots(figsize=(15,7.5))
            sns.barplot(x='product_material',y='sold',data=data)
            plt.xticks(rotation=90)
            st.pyplot(fig)
        if variable=='seller_badge':
            st.subheader('Product Sold by Seller Badge')
            fig,ax=plt.subplots(figsize=(10,5))
            sns.barplot(x='seller_badge',y='sold',data=data)
            st.pyplot(fig)
        if variable=='seller_country':
            st.subheader('Product Sold by Seller Country')
            fig,ax=plt.subplots(figsize=(15,7.5))
            sns.barplot(x='seller_country',y='sold',data=data)
            st.pyplot(fig)
    if graph=='Box Plot':
        st.subheader('Box Plot of Product Like Count by Product Category and Sold')
        fig,ax=plt.subplots(figsize=(10,5))
        sns.boxplot(x=data['product_like_count'],y=data['product_category'],hue=data['sold'])
        st.pyplot(fig)
        st.subheader('Box Plot of Product Like Count by Brand Name')
        fig,ax=plt.subplots(figsize=(10,5))
        sns.boxplot(x=data['product_like_count'],y=data['brand_name'])
        st.pyplot(fig)
        st.subheader('Box Plot of Price by Brand Name')
        fig,ax=plt.subplots(figsize=(15,7.5))
        sns.boxplot(x=data['price_usd'],y=data['brand_name'])
        st.pyplot(fig)
        st.subheader('Box Plot of Seller Price by Seller Country')
        fig,ax=plt.subplots(figsize=(15,7.5))
        sns.boxplot(x=data['seller_price'],y=data['seller_country'])
        st.pyplot(fig)
    if graph=='Histogram':
        st.subheader('Distribution of Price in USD')
        fig,ax=plt.subplots(figsize=(10,5))
        sns.histplot(data['price_usd'],kde=True,bins=30)
        st.pyplot(fig)
        st.subheader('Distribution of Seller Country')
        fig,ax=plt.subplots(figsize=(10,5))
        sns.histplot(data['seller_country'],kde=True)
        plt.xticks(rotation=90)
        st.pyplot(fig)
    if graph=='Scatter Plot':
        st.subheader('Scatterplot of Seller no.of followers by Sellers Products Sold')
        fig,ax=plt.subplots(figsize=(10,6))
        sns.scatterplot(x=data['seller_num_followers'],y=data['seller_products_sold'],hue=data['seller_badge'])
        st.pyplot(fig)        