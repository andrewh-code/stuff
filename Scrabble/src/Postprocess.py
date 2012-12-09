#!/usr/bin/python

#import libraries
import sys
from operator import itemgetter

class Postprocess:
    def __init__(self):
        self.sort = 0
        
    def resultsByPoints(self, final_results):
        self.final_results = final_results
        self.final_results_by_points = []
        
        final_results_by_points = sorted(final_results, key=itemgetter(1))
        
        return final_results_by_points
    
    def resultsByPointsReverse(self, final_results):
        self.final_results = final_results
        self.final_results_by_points = []
        
        final_results_by_points = sorted(final_results, key=itemgetter(1), reverse=True)

        return final_results_by_points
        
    def resultsByLength(self,final_results):
        self.final_results = final_results
        self.final_results_by_points = []
        
        final_results_by_points = final_results.sort()
        print final_results_by_points
        return final_results_by_points
        
    def resultsByLengthReverse(self, final_results):
        self.final_results = final_results
        self.final_results_by_points = []
        
        final_results_by_points = final_results.sort(reverse=True)
        print final_results_by_points
        return final_results_by_points