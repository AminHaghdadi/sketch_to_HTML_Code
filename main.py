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
    
custom1="""
    just print{layout}
"""
prompt=PromptTemplate(template=custom_prompt,input_variables=['layout'])

def html_generation(image):
    layout=ocr_process(image)
    chain=LLMChain(llm=llm,prompt=prompt)
    output=chain.run(layout=layout)
    print(output)
    
