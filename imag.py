#Edits an image

from PIL import Image


obj = Image.open("431.png")
#print(obj.size)
#print(obj.format)
width,height=obj.size
area=(width*0.4,height*0.35,width*0.6,height*0.65)
#obj.show()
c_img = obj.crop(area)
#r_img=obj.resize((200,200))
#r_img.show()
#r_img.save('pyt','jpg')

c_img.show()

c_img.save('size1','jpeg')
