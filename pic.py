import random

from PIL import Image, ImageDraw, ImageFile
import requests


Image.MAX_IMAGE_PIXELS = None
ImageFile.LOAD_TRUNCATED_IMAGES = True

with open('urls_data.txt') as urls:
    nums = list([])
    for i in urls:
        nums.append(i[:-1])


square = Image.new('RGB', (10000, 10000), 'white')
square.save('square.jpg')
square = Image.open("square.jpg")



edge=40

main_pic = Image.open("main_pic.jpg")
main_pic = main_pic.resize((10000, 10000))
main_pic.save('main_pic.jpg')
main_pic = Image.open("main_pic.jpg")
pix = main_pic.load()


rand_choice=[]
K=1
for i in range(int(len(nums)/4)-1):
    rand_choice.append(K)
    K=K+4

G = 0
J = 100

for j in range(100):
    C = 0
    S = 100
    
    
    for i in range(100):

        coefficient_r = 1000
        coefficient_g = 1000
        coefficient_b = 1000

        
        
        r = []
        g = []
        b = []
        for y in range(10000):
            for x in range(10000):
                if x >= C and x < S and y >= G and y < J:
                    r.append(pix[x, y][0])
                    g.append(pix[x, y][1])
                    b.append(pix[x, y][2])
                                        
                if x % 100 == 0 and y % 100 == 0 and x != 0 and y != 0 and len(r) !=0:
                    average_r = sum(r) / len(r)
                    average_g = sum(g) / len(g)
                    average_b = sum(b) / len(b)
        
        while abs(coefficient_r) > edge or abs(coefficient_g) > edge or abs(coefficient_b) > edge:
            try:
                I = random.choice(rand_choice)
                
                
                avg_r=nums[I]
                avg_g=nums[I+1]
                avg_b=nums[I+2]

                coefficient_r = int(avg_r) - int(average_r)
                coefficient_g = int(avg_g) - int(average_g)
                coefficient_b = int(avg_b) - int(average_b)
                

                if abs(coefficient_r) <= edge and abs(coefficient_g) <= edge and abs(coefficient_b) <= edge:
                    rand_choice.remove(I)
                    r = requests.get(nums[I-1])
                    with open('pic.jpg', 'w+b') as pic:
                        pic.write(r.content)

                    pic = Image.open('pic.jpg')
                    pic = pic.convert('RGB')
                    pic = pic.save('pic.jpg')
                    pic = Image.open('pic.jpg')
                    pic = pic.resize((100, 100))
                             
     
                    O = 0 + (100 * i)
                    P = 0 + (100 * j)
                    print(O,P)

                    C = C + 100
                    S = S + 100
                    
                    if C == 9900:
                        G = G + 100
                        J = J + 100
                    
                    square.paste(pic, (O, P))
                    square.save('square.jpg')


                    #del nums[I-1],nums[I],nums[I+1],nums[I+2]

            except OSError:
                continue 
#square.save('square.jpg')
square.show()





