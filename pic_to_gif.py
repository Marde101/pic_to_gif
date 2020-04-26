from PIL import Image
import imageio

# Declare path of the picture. e.q. below
path = 'C:/Users/*user*/Desktop/picture.png'

# Declare where the single pictures will be saved. e.q. below
path_pictures = 'C:/Users/*user*/Desktop/pictures/'

# Declare path of where the pic will be posted. e.q. below
gif_path = 'C:/Users/*user*/Desktop/gif.gif'

# Declare name of the gif. e.q. below
gifname = 'name.gif'

# Declare how many pixels will be shown per frame. 
# Use 1 for no frame loss
divider=20

# If you original picture has transparent mode = 1, otherwise mode = 0.
# If mode is set to anything else than 1 or 0 the script won't run. 
mode = 1

namelist=[]

def createGif():
    with imageio.get_writer(gif_path+gif.name,
                             mode='I') as writer:
        for filename in namelist:
            image = imageio.imread(filename)
            writer.append_data(image)
            print(filename)

def createPicsOne(str):
    im = Image.open(str)
    width, height = im.size
    im_new = Image.new('RGB', im.size, 0xffffff)
    rows=[]
    cols=[]
    for x in range(width):
        for y in range(height):
            r,g,b,i = im.getpixel((x,y))
            asd = [r,g,b,i]
            cols.append(asd)
        rows.append(cols)
        cols=[]

    for z in range(width):
        if z%divider == 0:
            im_new = Image.new('RGB', im.size, 0xffffff)
            for x in range(width):
                for y in range(height):
                    if x > z:
                        r,g,b,i = rows[z][y]
                        im_new.putpixel((x,y), (r,g,b,i))
                    else:
                        r,g,b,i = rows[x][y]
                        im_new.putpixel((x,y), (r,g,b,i))
            im_new.save(+'/pic%s.png'%z)
            namelist.append(path_pictures+'/pic%s.png'%z)

    createGif()

def createPics(str):
    im = Image.open(str)
    width, height = im.size
    im_new = Image.new('RGB', im.size, 0xffffff)
    rows=[]
    cols=[]
    for x in range(width):
        for y in range(height):
            r,g,b,i = im.getpixel((x,y))
            asd = [r,g,b,i]
            cols.append(asd)
        rows.append(cols)
        cols=[]

    for z in range(width):
        if z%divider == 0:
            im_new = Image.new('RGB', im.size, 0xffffff)
            for x in range(width):
                for y in range(height):
                    if x > z:
                        r,g,b,i = rows[z][y]
                        im_new.putpixel((x,y), (r,g,b,i))
                    else:
                        r,g,b,i = rows[x][y]
                        im_new.putpixel((x,y), (r,g,b,i))
            im_new.save(+'/pic%s.png'%z)
            namelist.append(path_pictures+'/pic%s.png'%z)
            
    createGif()

if mode==1:
    createPicsOne(path)
elif mode==0:
    createPics(path)
    
