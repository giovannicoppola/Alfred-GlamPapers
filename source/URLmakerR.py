### Friday, November 6, 2020, 9:13 AM, Biden just took over Trump in PA, and will probably be called as winner today
### exercise to write a python script to replace some characters and make a URL for the Glam Alfred workflow

import sys
import os

glam_stringFILE =  "glam_string.txt"

# getting the query from Alfred

myQuery = '+'.join(sys.argv[1:])

def log(s, *args):
    #function to log error messages 
    """Write string to STDERR."""
    if args:
        s = s % args
    print(s, file=sys.stderr)


def main():
    
    read_file = open(glam_stringFILE, "r")
    glam_string = read_file.read()
    #print (glam_string)
    glam_string = glam_string + "Review[Filter] AND ("
    URL_string = (glam_string.translate(str.maketrans({
        '(': '%28', 
        ' ': '+',
        '"': '%22',
        '[': '%5B',
        ']': '%5D',
        ':': '%3A',
        '\n': None,
        '\'': '%27',
        '&': '%26',
        ')': '%29'
        })))
    final_URL_string = "open https://pubmed.ncbi.nlm.nih.gov/?term=" + URL_string + myQuery + "%29+\&sort=pubdate\&size=50"
    #log (final_URL_string)
    os.system(final_URL_string)
    	
    	

if __name__ == '__main__':
    main()



