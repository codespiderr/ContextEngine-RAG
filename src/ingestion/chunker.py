from pathlib import Path
import os

def chunker():
    chunk_path = "data/chunks/"
    path = Path("data/cleaned")
    chunk_number = 0
    carryover = ""
    open(chunk_path+"temp","w",encoding="utf-8")
    for item in path.iterdir():

        with open(item.resolve(),'r',encoding="utf-8") as f:
            not_end = True
            while not_end:
                title = f.readline()
                context = f.readline()
                
                #with open(chunk_path+"chunk"+str(chunk_number),"w",encoding="utf-8") as c:
                tokens = 0
                c = open(chunk_path+"chunk"+str(chunk_number),"x",encoding="utf-8")
                temp = open(chunk_path+"temp","r+",encoding="utf-8",errors="ignore")
                #c.write("Title: "+title)
                #c.write("Context: "+context)
                #c.write("chunk number: "+str(chunk_number))
                c.write(carryover)
                c.write("/n")
                c.write("Carry Over complete")
                while tokens<256:
                    text1 = f.readline()
                    tokens += len(text1.split())
                    if text1 == "":
                        break
                    if tokens>132:
                        print("writing line to temp",chunk_number)
                        temp.write(text1)
                    c.write(text1)
                    temp.seek(0)
                carryover = temp.read()
                chunk_number+=1
                temp.close()
                c.close()

                current_pos = f.tell()
                f.seek(0, os.SEEK_END)  
                end_pos = f.tell()    
                f.seek(current_pos)     
                if current_pos >= end_pos:
                    not_end = False

if __name__ == "__main__":
    chunker()