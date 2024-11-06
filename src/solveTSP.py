import tsplib95 as tsp
import os
from time import time


def calculateDistance(problem):
    distance = 0
    for node in problem.get_nodes():
        if node+1 <= problem.dimension:
            distance += problem.get_weight(node, node+1)
        else:
            distance += problem.get_weight(node, 1)
    return distance


def loadProblem(tsp_file, tour_file):
    problem = tsp.load(tsp_file)
    solution = tsp.load(tour_file)
    return problem, solution


def solveProblem(tsp_file, tour_file, save_file=None):
    print('Solving tsp for', tsp_file, '...')
    problem, solution = loadProblem(tsp_file, tour_file)
    start_time = time()

    calc_distance = calculateDistance(problem)

    end_time = time()
    best_distance = problem.trace_tours(solution.tours)[0]
    time_taken = end_time - start_time
    gap_percent = (calc_distance - best_distance)/calc_distance*100
    
    print('Time taken (s):', time_taken)
    print('bayg29 Calculated Tour Length:', calc_distance)
    print('bayg29 actual Tour Length:', best_distance)
    print('Gap %:', round(gap_percent, 2))
    
    if save_file:
        open_mode = 'a' if os.path.exists(save_file) else 'w'
        
        with open(save_file, open_mode) as file:
            file.write('{}\n'.format(tsp_file))
            file.write('    Time taken (s): '+str(time_taken)+'\n')
            file.write('    Calculated Tour Length:'+str(calc_distance)+'\n')
            file.write('    Actual Tour Length: '+str(best_distance)+'\n')
            file.write('    Gap %: '+str(round(gap_percent, 2))+'\n')
        print('Results saved to', save_file)
        


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(__file__))
    timestamp = time()
    
    save_file = path+'/solutions/manual_solutions_'+str(timestamp)+'.txt'
    
    solveProblem(path+'/data/test_data/bayg29.tsp',
                 path+'/data/test_data/bayg29.opt.tour',
                 save_file)
    solveProblem(path+'/data/test_data/att48.tsp',
                 path+'/data/test_data/att48.opt.tour',
                 save_file)
