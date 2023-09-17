from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from PIL import Image
import streamlit as st
from OCR import OCR_Processor
import streamlit.components.v1 as components
import os
from keys import openai_API
os.environ["OPENAI_API_KEY"] = openai_API


def ocr_process(img):
    processor=OCR_Processor()
    layout=processor.extract(img)
    return layout



llm = ChatOpenAI(model="gpt-3.5-turbo-16k",temperature=0.1, max_tokens=2096)

    


custom_prompt="""
    This is a layout of a handwriting website design, including text and their coordinates of four outer vertices. 
        Make an HTML modern sans-serif website that reflects these elements and decide which 
        CSS can be used to match their relative positions, try to use proper layout tags to match
         their font size and relative placement based on their coordinates. 
         Use <ul> and <li> if the elements look like as menu list. 
         Smartly use function tags like <button> <input> if their names look like that.
         Your design should be prior to the coordinates, 
         then you should also use some imagination for the layout and CSS from common web design principle.
         Remember, don't use absolute coordinates in your HTML source code. 
         Generate only source code file, no description: {layout}.\n
    """
    

prompt=PromptTemplate(template=custom_prompt,input_variables=['layout'])

def html_generation(layout):
    chain=LLMChain(llm=llm,prompt=prompt)
    output=chain.run(layout=layout)
    return output

if "html" not in st.session_state:
    st.session_state.html=""
if "image" not in st.session_state:
    st.session_state.image=""

def Run():
    html_code=""
    
    layouts=ocr_process(st.session_state.image)
    if layouts != []:
        html_code=html_generation(layouts)
    
    
    st.session_state.html=html_code
    st.session_state.image=st.session_state.image
    
st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>HTML generator from Sketch</h1>", unsafe_allow_html=True)

col1,col2=st.columns([0.5,0.5],gap='medium')

with col1:
    upload_file=st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if upload_file is not None:
        image_file_name=upload_file.name
        st.image(upload_file,caption="Uploaded Image", use_column_width=True)
        image=Image.open(upload_file)
        image.save(image_file_name)
        
        st.session_state.image=image_file_name
        st.button('Run',on_click=Run)

with col2:
    if st.session_state.html != "":
        with st.expander("See Source Code") :
            st.code(st.session_state.html)
            
        with st.container():
            components.html(st.session_state.html,height=600, scrolling=True)