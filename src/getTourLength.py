import tsplib95
import os

def getTourLength(tsp_file, tour_file):
    # print('Tracing Tour file:', tour_file)
    try:
        solution = tsplib95.load(tour_file)
        problem = tsplib95.load(tsp_file)
    except:
        print('File not found:')
        return -1
    
    traces = problem.trace_tours(solution.tours)
    
    # print('Num tours = ', len(traces))
    # print('    (Presumably 1 but not guaranteed apparently)')
    return traces[0]

if __name__ == '__main__':   
    path = os.path.dirname(os.path.dirname(__file__))
    
    print('bayg29 Tour Length:', getTourLength(path+'/data/extracted/bayg29.tsp', path+'/data/extracted/bayg29.opt.tour'))
    
    print('att48 Tour Length:', getTourLength(path+'/data/extracted/att48.tsp', path+'/data/extracted/att48.opt.tour'))
    