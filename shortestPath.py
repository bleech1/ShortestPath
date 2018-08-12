# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 21:25:45 2018

@author: Bleecher
"""

import xlrd
from point import point
from path import path

WORKBOOK_NAME = "Times.xlsx"
WORKSHEET_NAME = "Averages"
INF = 10000000

# Holds the shortest path and time for each combination
results = list(list())

# Keys are IDs for the places, values are their descriptions
placeIds = dict()

# List of the point objects
points = list()

def OpenExcel(workbookName, worksheetName):
    workbook = xlrd.open_workbook(workbookName)
    worksheet = workbook.sheet_by_name(worksheetName)
    numRows = worksheet.nrows - 1
    numCols = worksheet.ncols - 1
    return worksheet, numRows, numCols
    
def InitializePoints(numRows):
    for i in range(numRows):
        p = point(i + 1, INF, False, "")
        points.append(p)
    
def ResetPoints():
    for p in points:
        p.dist = INF
        p.processed = False
        p.pred = ""
        
def Dijkstra(row, col):
    return 1, 2
        
def CalculateShortestPaths():
    print("Calculating")
    worksheet, numRows, numCols = OpenExcel(WORKBOOK_NAME, WORKSHEET_NAME)
    # For each combo, create a point object for each point
    InitializePoints(numRows - 1)
    # Run through each combination of points
    for row in range(1, numRows):
        # Add the start point to the dictionary
        placeIds[row] = worksheet.cell(row, 0)
        for col in range(2, numCols):
            # Ignore if the start and dest are the same
            if (row == col):
                continue
            order, distance = Dijkstra(row, col)
            # Put the resulting path into results
            
            ResetPoints()
    
def FindShortestPath(start, end):
    print("Finding")
    # Don't do anything if start is end
    if (start == end):
        print("Start and end are the same")
        print("Don't go anywhere")
        print("You're at the destination")
        return []
    # For each part of path, convert to place description
    
    

if __name__ == "__main__":
    print("Calculating distances")
    CalculateShortestPaths()
    #placeIds[5] = "Back of Starr"
    #placeIds[10] = "Proc"
    for key, value in placeIds.items():
        print("Id: " + str(key), "\tValue: " + value.value)
    start = input("Where are you starting from?\n--> ")
    end = input("Where do you want to go?\n--> ")
    FindShortestPath(start, end)
