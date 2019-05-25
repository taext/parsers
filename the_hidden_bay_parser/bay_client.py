import sys
import hiddenbay_parser as bay

def run(search_term, count):

    li, di = bay.run(search_term, count) 
    print("\n")
    for item in li:
        bay.print_please(item)
        print("\n")

if __name__ == '__main__':
    run(sys.argv[1], int(sys.argv[2]))
