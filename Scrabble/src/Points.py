#!/usr/bin/python

#import libraries
import sys
import Constants as c

class Points:
    def __init__(self):
        self.points = 0
        
    #======================================================
    # This function takes in every word from the sorted_results list and uses a hashmap/dictionary to associate every
    # letter with its corresponding Scrabble point score
    # Input: sorted_results
    # Output: final_point_results
    #======================================================
    def associatePointScore(self, sorted_results):
        
        self.sorted_results = sorted_results
        self.sum = 0
        self.final_point_results = []    #2D list
        self.tile = ''
        
        for x in range(0, len(self.sorted_results)):
            for self.tile in self.sorted_results[x]:
                if (self.tile == '-'): #taking care of indices created for speeding up search algo, return 0 points for them
                    break     
                else: 
                    self.sum += c.TILE_POINTS[self.tile]
            self.final_point_results.append([self.sorted_results[x], self.sum])
            self.sum = 0

        return self.final_point_results

#def sortFinalResults(final_results):    print final_results