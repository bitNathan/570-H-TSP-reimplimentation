import tsplib95 as tsp
import os
from time import time
from augment_data import *


def calculateDistance(problem):
    distance = 0.0
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


def save_file_func(save_file, tsp_file, time_taken, calc_distance, best_distance, gap_percent):
    open_mode = 'a' if os.path.exists(save_file) else 'w'

    with open(save_file, open_mode) as file:
        file.write('{}\n'.format(tsp_file))
        file.write('    Time taken (s): '+str(time_taken)+'\n')
        file.write('    Calculated Tour Length:'+str(calc_distance)+'\n')
        file.write('    Actual Tour Length: '+str(best_distance)+'\n')
        file.write('    Gap %: '+str(round(gap_percent, 2))+'\n')
    print('Results saved to', save_file)


def solveProblem(tsp_file, tour_file, save_file=None):
    print('Solving tsp for', tsp_file, '...')
    problem, solution = loadProblem(tsp_file, tour_file)
    print(problem.as_name_dict())
    # for attribute in dir(problem):
    #     if not attribute.startswith('_'):
    #         print('ATTR:', attribute, getattr(problem, attribute))
    start_time = time()
    problem = augment_data(problem, solution, debug=True)
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
        save_file_func(save_file, tsp_file, time_taken, calc_distance, best_distance, gap_percent)


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(__file__))
    timestamp = time()

    # comment for testing
    save_file = path+'/solutions/manual_solutions_'+str(timestamp)+'.txt'
    save_file = None

    solveProblem(path+'/data/test_data/bayg29.tsp',
                 path+'/data/test_data/bayg29.opt.tour',
                 save_file)
    solveProblem(path+'/data/test_data/att48.tsp',
                 path+'/data/test_data/att48.opt.tour',
                 save_file)
