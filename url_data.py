        from PIL import Image, ImageDraw, ImageFile
import requests


with open('urls.txt') as urls:
    nums = set([])
    for i in urls:
        nums.add(i[:-1])
nums = list(nums)

file_url = open('urls_data.txt', 'w')

I=-1
while I<len(nums):
    try:
        I = I + 1
        r = requests.get(nums[I])
        with open('pic.jpg', 'w+b') as pic:
            pic.write(r.content)

                    
        pic = Image.open('pic.jpg')
        pic = pic.convert('RGB')
        pic = pic.save('pic.jpg')
        pic = Image.open('pic.jpg')
        pic = pic.resize((100, 100))
        pix_pic = pic.load()           
                        
        r = []
        g = []
        b = []
        for y in range(100):
            for x in range(100):
                r.append(pix_pic[x, y][0])
                g.append(pix_pic[x, y][1])
                b.append(pix_pic[x, y][2])

        avg_r = sum(r) / len(r)
        avg_g = sum(g) / len(g)
        avg_b = sum(b) / len(b)

        url_data=[nums[I], str(int(avg_r)), str(int(avg_g)), str(int(avg_b))]
        file_url = open('urls_data.txt', 'a')
            
        for i in url_data:
            file_url.write(i+'\n')
        file_url.close()
            

    except OSError:
        continue 


