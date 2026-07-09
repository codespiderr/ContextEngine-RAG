from pathlib import Path
import os

def chunker():
    chunk_path = "data/chunks/"
    path = Path("data/cleaned")
    chunk_number = 0
    for item in path.iterdir():
        print(item.name)
        with open(item.resolve(),'r',encoding="utf-8") as f:
            not_end = True
            while not_end:
                title = f.readline()
                context = f.readline()
                
                #with open(chunk_path+"chunk"+str(chunk_number),"w",encoding="utf-8") as c:
                tokens = 0
                c = open(chunk_path+"chunk"+str(chunk_number),"x",encoding="utf-8")
                c.write("Title: "+title)
                c.write("Context: "+context)
                c.write("chunk number: "+str(chunk_number))
                while tokens<256:
                    text1 = f.readline()
                    tokens += len(text1.split())
                    if text1 == "":
                        break
                    c.write(text1+str(tokens))
                    print(tokens)
                    
                
                chunk_number+=1

                #checking if file reached the end
                current_pos = f.tell()
                f.seek(0, os.SEEK_END)  
                end_pos = f.tell()    
                f.seek(current_pos)     
                print(current_pos,end_pos)
                if current_pos >= end_pos:
                    not_end = False
                    print("Cursor is at EOF")

if __name__ == "__main__":
    chunker()