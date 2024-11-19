""" from PyPDF2 import PdfMerger

pdfs = ['1.pdf', '2.pdf', '3.pdf']
merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("x.pdf")
merger.close()
 """

import os
from PyPDF2 import PdfMerger

# Let the user input the directory
directory = input("请输入PDF文件夹路径: ")  # 提示用户输入目录路径

# Initialize PdfMerger
merger = PdfMerger()

# Iterate over all PDF files in the specified directory
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.pdf'):
        filepath = os.path.join(directory, filename)
        merger.append(filepath)

# Output merged PDF
output_path = os.path.join(directory, "AAA_Fianl.pdf")
merger.write(output_path)
merger.close()

print(f"合并完成，输出文件为: {output_path}")
