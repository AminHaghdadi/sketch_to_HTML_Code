import easyocr
class OCR:
    def __init__(self):
        self.reader=easyocr.Reader(['en'],gpu=True)

    def extract_ocr(self,img):
        result=self.reader.readtext(img)
    
        out_put=[]
        for original_list,key,_ in result :
            values=[corr for sublist in original_list for corr in sublist]
            formatted_dict={key:values}
            out_put.append(formatted_dict)
        return out_put

ocr=OCR()
print(ocr.extract_ocr("test.jpg"))