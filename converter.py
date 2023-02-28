import os
"""
* This function takes in two integers, the first one is year, the second is number of documents another 
* The function requiers documents to have specific names 
* <year>_<number>.pdf
* e.g. 2020_1.pdf, 2020_2
"""
def custom_convert_function(year: int, number_of_docs: int):
    for num in range(1, number_of_docs+1):
        os.system(f"convert -density 300 {year}_{num}.pdf -alpha off rus_{num}.tiff")
        os.system(f"tesseract rus_{num}.tiff rus_trans_{year}_{num} -l rus")



if __name__ == "__main__":
    custom_convert_function(2018, 4)
    custom_convert_function(2019, 8)
