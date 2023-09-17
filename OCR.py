import easyocr

class OCR_Processor:
    def __init__(self):
        self.reader=easyocr.Reader(['en'],gpu=True)
        
    def extract(self,img):
        result = self.reader.readtext(img)
        
        output=[]
        
        for final_list,key,_ in result :
            cordinate=[corr for sublist in final_list for corr in sublist]
            
            formatted_dict={key:cordinate}
            
            output.append(formatted_dict)
            
        return output
