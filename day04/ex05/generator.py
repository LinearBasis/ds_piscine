import sys
import resource

def get_list_of_rating(filename):
    with open(filename, 'r') as f:
        line = "None"
        while line != "":
            a = f.readline()
            yield a
    return a

def main():
    if len(sys.argv) != 2:
        return 0
    for i in get_list_of_rating(sys.argv[1]):
        pass
    
    usage = resource.getrusage(resource.RUSAGE_SELF)
    print(f'Peak Memory Usage = {round((usage.ru_maxrss / (1024**3)), 3)} GB')
    print(f'User Mode Time + System Mode Time = {round((usage.ru_utime + usage.ru_stime), 2)}s')

if __name__ == "__main__":
    main()