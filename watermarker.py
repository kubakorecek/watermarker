import os
import numpy as np


from PIL import ImageDraw
from PIL import ImageFont 
from PIL import Image

class WATERMARKER():
    '''simple utility to make watermark, the image of watermark
    should be on black background'''
    def __init__(self):
        self.bsDIR=os.path.abspath(os.curdir)  # Base dir
        self.inDIR=os.path.join(self.bsDIR,'IN')  # IN dir
        self.outDIR=os.path.join(self.bsDIR,'OUT_MARKED') # OUT dir
        self.resizeWDIR=os.path.join(self.bsDIR,'SIZE_OUT_MARKED') # RESIZE_OUT_MARKED dir
        self.resizeDIR=os.path.join(self.bsDIR,'SIZE_OUT') #RESIZE_OUT
        self.routDIR=os.path.join(self.bsDIR,'WRONG_SIZE') # WRONG_SIZE dir
        self.logoDIR=os.path.join(self.bsDIR,'LOGO')
        
        
        for i in [self.inDIR,self.outDIR,self.resizeWDIR,self.resizeDIR,self.routDIR,self.logoDIR]:
        
            self.mk(i)
        
        self.LOGO=os.listdir(self.logoDIR)
        self.IMAGES=os.listdir(self.inDIR) # LIST of Pictures
        
    def mk(self,directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        
    def utility_watermark(self,logo,opacity=35):
        ''' load logos by given choice'''
        
        #Load and convert WATERMARK image
        watermark_img=Image.open(os.path.join(
                                    str(self.logoDIR),
                                    str(logo))
                                ).convert("RGBA") 
        
        # Convert waterimage to black-white renderer
        mask=Image.new('L',watermark_img.size,color=int(opacity)) 
        
        # SET alpha vector
        watermark_img.putalpha(mask) 

        # VECTOR data from watermark
        datas=watermark_img.getdata()
        
        newData=[]
        
        #make black backgorund trnasparent
        for item in datas: 

            if item[0] == 0 and item[1] == 0 and item[2] == 0:
            
                newData.append((0, 0, 0, 0))
            
            else:
            
                newData.append((item))
                
        watermark_img.putdata(newData)
        
        
        #return re do transparent waterimage
        return watermark_img
        
    def utility_base_image(self,input):
        '''base imgae converter'''
        base_img=Image.open(os.path.join(
                                            str(self.inDIR),
                                            str(input))
                                        ).convert("RGBA")
        width,height=base_img.size
            
        return base_img,width,height,input

    
        
        
    def watermark_done(self,NumLogo,opacity,resizer,min_w=500,min_h=500):
        '''watermarker'''

        logo=self.LOGO[NumLogo]

        waterimage=self.utility_watermark(logo,opacity)

        for image in self.IMAGES:
            
            data_image=self.utility_base_image(image)

            if resizer=='change':

                sizer=(min_w,min_h)
                
                if min_w<=data_image[1] and min_h<=data_image[2]:
                
                    
                    
                    WATERMARKER.OUTPUTER('Water'
                        ,self.resizeWDIR
                        ,sizer
                        ,data_image[0]
                        ,image
                        ,waterimage)
                        

                else:
                    WATERMARKER.OUTPUTER('No Water'
                        ,self.routDIR
                        ,sizer
                        ,data_image[0]
                        ,image
                        )
                    pass
                
            elif resizer=='keep':
            
                sizer=(data_image[1],data_image[2])
                
                if min_w<=data_image[1] and min_h<=data_image[2]:
                    
                    
                    
                    WATERMARKER.OUTPUTER('Water'
                        ,self.outDIR
                        ,sizer
                        ,data_image[0]
                        ,image
                        ,waterimage)
                else:
                    WATERMARKER.OUTPUTER('No Water'
                        ,self.routDIR
                        ,sizer
                        ,data_image[0]
                        ,image
                        )

                    

    def check_size(self,min_w=500,min_h=500):
        
        for image in self.IMAGES:
            
            data_image=self.utility_base_image(image)
            
            sizer=(data_image[1],data_image[2])
            
            if min_w<=data_image[1] and min_h<=data_image[2]:
                    
                    
                    
                WATERMARKER.OUTPUTER('No Water'
                    ,self.resizeDIR
                    ,sizer
                    ,data_image[0]
                    ,image
                    )
            else:
                WATERMARKER.OUTPUTER('No Water'
                    ,self.routDIR
                    ,sizer
                    ,data_image[0]
                    ,image
                    )

    @staticmethod
    def OUTPUTER(mode,output,sizer,image,name,water_image=None):
        '''helping method'''
        if mode=='Water':
            image.thumbnail(sizer,Image.ANTIALIAS)
            
            water_image.thumbnail(sizer,Image.ANTIALIAS)
            #water_image.paste( (0,0,0), [0,0,water_image.size[0],water_image.size[1]])
            water_image.show()
                
            new=Image.new('RGB',sizer,(0,0,0,0))
                
            new.paste(image, (0,0))
            
            new.paste(water_image, (0,int(sizer[1]/4)),mask=water_image)
                
            new.save(os.path.join(output,name))
            

            
        elif mode =='No Water':
            image.thumbnail(sizer,Image.ANTIALIAS)
            
            new=Image.new('RGB',sizer,(0,0,0,0))
            
            new.paste(image, (0,0))
                        
            new.save(os.path.join(output,name))
            

    #def __init__(self,logo):
    
        
    
    
    
#a=WATERMARKER()
#print(a.IMAGES)
#print('tt',a.logoDIR)
#print(a.LOGO)
#for i in range(0,5):
    #a.utility_base_image(a.IMAGES[i])
    #a.utility_watermark(a.LOGO[i],35)
    
#a.watermark_done(a.LOGO[0],55,'resize_w')
