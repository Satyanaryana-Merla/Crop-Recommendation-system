import streamlit as st
import sklearn
from joblib import dump, load
import pandas as pd

def pred(feat):
	feat=pd.DataFrame(feat)
	clf=load('GNBClassifier.pkl')
	pred=clf.predict(feat)
	st.success('Recommended crop is {}'.format(str(pred[0]).upper()))
	st.success('Accuracy of prediction is: {}%'.format(99.54))


def main():
	page_bg_img = """
	<style>div.stButton > button:first-child {
	background-color: #00cc00;color:white;font-size:20px;height:3em;width:100%;border-radius:10px 10px 10px 10px;
	}
	</style>
	"""
	st.markdown(page_bg_img, unsafe_allow_html= True)
	html_temp = """ 
    <div style ="padding:13px;margin:15px 0px;background-color:yellow;">
    <h1 style ="color:black;text-align:center;">Crop Recommendation using ML</h1>
    </div>
    <h4 style ="text-align:center;padding:20px 0px">Enter the details of your soil and we will recommend you what is the crop best suited for your soil and help you maximise your profits!</h4>
    """
	st.image('./img-wg-crops.jpg')
	st.markdown(html_temp, unsafe_allow_html = True)
	N=st.text_input("Ratio of Nitrogen Content in Soil", "")
	P=st.text_input("Ratio of Phosphorous Content in Soil", "")
	K=st.text_input("Ratio of  Potassium Content in Soil", "")
	temp=st.text_input("Temperature in degree Celsius", "")
	hum=st.text_input("Humidity (relative in %)", "")
	ph=st.text_input("pH of Soil", "")
	rain=st.text_input("Rainfall (in mm)", "")
	l=[[N, P, K, temp, hum, ph, rain]]
	col1,col2,col3=st.columns([0.3,1.2,0.3])
	with col1:
		st.empty()
	with col2:
		if st.button("Recommend"):
			pred(l)
	with col3:
		st.empty()

if __name__=='__main__':
	main()
