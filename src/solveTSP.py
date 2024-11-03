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


def solveProblem(tsp_file, tour_file):
    print('Solving tsp for', tsp_file, '...')
    problem, solution = loadProblem(tsp_file, tour_file)
    start_time = time()

    calc_distance = calculateDistance(problem)

    end_time = time()
    best_distance = problem.trace_tours(solution.tours)[0]
    time_taken = end_time - start_time

    print('Time taken (s):', time_taken)
    print('bayg29 Calculated Tour Length:', calc_distance)
    print('bayg29 actual Tour Length:', best_distance)
    print('Gap %:', (calc_distance - best_distance)/calc_distance*100)


if __name__ == '__main__':
    path = os.path.dirname(os.path.dirname(__file__))
    solveProblem(path+'/data/test_data/bayg29.tsp',
                 path+'/data/test_data/bayg29.opt.tour')
    solveProblem(path+'/data/test_data/att48.tsp',
                 path+'/data/test_data/att48.opt.tour')
