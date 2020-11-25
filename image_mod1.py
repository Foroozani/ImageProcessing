"""

@author: najmeh
"""

from PIL import Image
import os

# same path with images 
image1 = Image.open('image/dog1.jpeg')
image1.show()

#%%
# modify 
image1.save('dog11.png')  # change the image format 

#%% create a "pngs" folder 

for f in os.listdir('.'):   # give directory to get the files
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        i.save('pngs/{}.png'.format(fn))
        
#%% 
# resize each image and save it to 300 folder 

size_100 = (100,100)
size_200 = (200,200)

for f in os.listdir('image'):   # give directory to get the files
    if f.endswith('.jpeg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        
        i.thumbnail(size_100)    # it also keep the aspect ratio 
        i.save('100/{}_100.p{}'.format(fn, fext))    # rename but keep regular extension 
        
        i.thumbnail(size_200)    # it also keep the aspect ratio 
        i.save('200/{}_200.p{}'.format(fn, fext))    # rename but keep regular extension 
        
        
