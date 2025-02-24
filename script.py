import os
import glob

dirs = ["Season 1"]

def gen_txt(inputFileExtension = "srt"):
    for dirname in dirs:
        files = glob.glob("./" + dirname + "/*." + inputFileExtension)
        for file in files:
            filename = os.path.basename(file)
            print(filename)
            outputfilename = os.path.splitext(filename)[0] + ".txt"
            outputFilePath = "./" + dirname + "/" + outputfilename
            with open(file, 'r', encoding="utf-8-sig") as filecontent:
                newcontent = ""
                n = 1
                for line in filecontent:
                    try:
                        subnum = int(line)
                        if subnum == n:
                            n += 1
                            newcontent += "\n"
                        else:
                            newcontent += line
                    except:
                        newcontent += line
                with open(outputFilePath, "w", encoding="utf-8") as f:
                    f.write(newcontent)

def build_srt():
    if not os.path.exists("./build"):
        os.mkdir("./build")

    for dirname in dirs:
        if not os.path.exists("./build/" + dirname):
            os.mkdir("./build/" + dirname)
        files = glob.glob("./" + dirname + "/*.txt")
        for file in files:
            filename = os.path.basename(file)
            print(filename)
            outputfilename = os.path.splitext(filename)[0] + ".srt"
            outputFilePath = "./build/" + dirname + "/" + outputfilename
            with open(file, 'r', encoding="utf-8-sig") as filecontent:
                newcontent = ""
                i = 0
                lines = [line for line in filecontent]
                n = 1
                while i < len(lines):
                    if len(lines[i].strip()) > 0:
                        newcontent += str(n) + "\n"
                        n += 1
                        while i < len(lines) and len(lines[i].strip()) > 0:
                            newcontent += lines[i]
                            i += 1
                        newcontent += "\n"
                    else:
                        i += 1
                with open(outputFilePath, "w", encoding="utf-8") as f:
                    f.write(newcontent)
                
                
if __name__ == "__main__" :
    import sys
    if sys.argv[1] == "build":
        build_srt()
    elif sys.argv[1] == "gentxt":
        gen_txt()
    elif sys.argv[1] == "cleantxt":
        gen_txt("txt")
    else:
        print("Unknown command", sys.argv[1])