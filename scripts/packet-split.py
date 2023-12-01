##takes a file as a parameter(output from driver call) and uses split-image() into four
import split_image as split
import os
packet_name = input("file name")
file = "../images/output/"+packet_name+".jpg"
def quad_split(file,packet_name):
   # os.mkdir("/images/packets/"+packet_name)
    split.split_image(file, 2, 2, False,False,False,"../images/packets/"+packet_name)
    print("Done. Packet found at "+ "/images/packets/"+packet_name)
quad_split(file,packet_name)
