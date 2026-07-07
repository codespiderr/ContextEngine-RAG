from pathlib import Path

def chunker():
    chunk_path = "data/chunks/"
    path = Path("data/cleaned")
    chunk_number = 0
    for item in path.iterdir():
        with open(item.resolve(),'r') as f:
            title = f.readline()
            context = f.readline()
            open(chunk_path+"chunk"+str(chunk_number),"x")
            with open(chunk_path+"chunk"+str(chunk_number),"w") as c:
                tokens = 0
                c.write("Title: "+title)
                c.write("Context: "+context)
                c.write("chunk number: "+str(chunk_number))
                while tokens<512:
                    break
                chunk_number+=1
            break
            

        break

if __name__ == "__main__":
    chunker()