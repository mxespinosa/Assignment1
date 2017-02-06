def MakeFile():
    f = open("image.ppm","w")
    f.write("P3 512 512 255")
    for y in range (512):
        for x in range (512):
            if (x>225 and x<286) or (y>225 and y<286):
                r = 0;
                g = 0;
                b = 0;
            if (x<=225 and y<=225):
                r= 255;
                g= 255 - (x%256)
                b= 255 - (x%256)
            if (y>=286 and x>=286):
                r = 255
                g = 255
                b = 255 - (x%256)
            if (y>=286 and x<=225):
                r = 255 - (x%256)
                g = 255 - (x%256)
                b = 255
            if (y<=225 and x>=286):
                r = 255 - (x%255)
                g = 255
                b = 255 - (x%255)
            f.write(" "+str(r)+" "+str(g)+" "+str(b)+"\n")



MakeFile()
