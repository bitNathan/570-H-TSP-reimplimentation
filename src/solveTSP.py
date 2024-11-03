import tsplib95 as tsp
import os
from time import time

def solveProblem(problem):
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

if __name__ == '__main__':  
    path = os.path.dirname(os.path.dirname(__file__))
    print('Solving tsp for bayg29...')
    
    problem, solution = loadProblem(path+'/data/extracted/bayg29.tsp',
        path+'/data/extracted/bayg29.opt.tour')
    
    start_time = time()
    
    calc_distance = solveProblem(problem)
    
    end_time = time()
    best_distance = problem.trace_tours(solution.tours)[0]
    time_taken = end_time - start_time
    
    print('Time taken (s):', time_taken)
    print('bayg29 Calculated Tour Length:', calc_distance)
    print('bayg29 actual Tour Length:', best_distance)
    print('Gap %:', (calc_distance - best_distance)/calc_distance*100)
