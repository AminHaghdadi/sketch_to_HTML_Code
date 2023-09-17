# HTML Generator from Sketches 
![image](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![image](https://img.shields.io/badge/OpenAI-412991.svg?style=for-the-badge&logo=OpenAI&logoColor=white)
![image](https://img.shields.io/badge/-LangChain-32CD32?logo=LangChain&logoColor=white&style=for-the-badge)

This Python code provides a novel way for users to convert handwritten sketches into structured web content. It allows anyone to upload an image of their sketch, which is then processed using EasyOCR to recognize and locate any text within the drawing. The text and coordinate data is passed to an LLM. In this scenario, ChatGPT is utilized to ingest the unstructured sketch information and generate the corresponding HTML. While other powerful language models are available,chatGPT-3.5-turbo-16k was used although ChatGPT4 is well-suited for this task.

![screencapture-localhost-8501-2023-09-17-18_08_50](https://github.com/AminHaghdadi/sketch_to_HTML_Code/assets/87299853/5e92e4c7-cb54-490c-bbad-80464de276b7)

## Deployment

To deploy this project run

1:
```bash
  git clone https://github.com/AminHaghdadi/sketch_to_HTML_Code.git
```
2: install requirements:
```bash
  pip install -r requirement.txt 
```
3:

Enter your OpenAI API in keys.py 

4: Run in Terminal
```bash
streamlit run main.py
```
