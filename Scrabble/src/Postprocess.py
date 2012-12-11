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
        
        for x in range(0, len(final_results)):
            final_results[x].append(len(final_results[x][0]))
            
        final_results = sorted(final_results, key=itemgetter(2), reverse = False)
        print final_results
        
        for x in range(0, len(final_results)):
            final_results[x].pop(2)
            
        return final_results
        
    def resultsByLengthReverse(self, final_results):
        self.final_results = final_results
        self.final_results_by_points = []
        
        for x in range(0, len(final_results)):
            final_results[x].append(len(final_results[x][0]))
            
        final_results = sorted(final_results, key=itemgetter(2), reverse = True)
        print final_results
        
        for x in range(0, len(final_results)):
            final_results[x].pop(2)
        
        return final_results