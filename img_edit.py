from PIL import Image

python1 = Image.open("python1.jpg")
python2= Image.open("python1280.jpg")

#print(python.mode)
r1, g1, b1 = python1.split()
r2, g2, b2 = python2.split()

new_imag = Image.merge("RGB",(r1,g2,b2))
new_imag.show()
#r.show()
#g.show()
#b.show()


#python.show()