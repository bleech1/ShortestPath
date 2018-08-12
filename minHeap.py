class minHeap:
    from math import *
    def __init__(self):
        self.minHeap = [] 

    def BuildHeap(self, pointArray):
        for point in range(pointArray):
            self.Insert(point)
    
    def Insert(self, point):
        count = len(self.minHeap)
        # If heap is empty, need to insert null point so that indices start at 1
        if (count == 0):
            self.minHeap.append(point(null, null, null))
            count ++
        # Appending point, will now be at index count
        self.minHeap.append(point)
        PropagateUp(count)

    def DeleteMin(self):
        # Save min (index 1) then move last element up and propagate down
        temp = self.minHeap[1]
        self.minHeap[1] = self.minHeap[len(self.minHeap) + 1]
        self.minHeap = self.minHeap[ : -1]
        __PropagateDown(1)

    def DecreaseKey(self, id, dist):
        # Find the right point, change its distance, propagate
        for i in range(len(self.minHeap)):
            if id != self.minHeap[i].id:
                continue
            self.minHeap[i].dist = dist
            # Since can only decrease point's distance, only need to
            # propagate up after changing the distance
            __PropagateUp(i)
        
    def __PropagateUp(self, index):
        distance = self.minHeap[index].dist
        while (distance < self.minHeap[floor(index / 2)].dist):
            temp = self.minHeap[index]
            self.minHeap[index] = self.minHeap[floor(index / 2)]
            self.minHeap[floor(index / 2)] = temp
            index = self.minHeap[floor(index / 2)]

    def __PropagateDown(self, index):
        distance = self.minHeap[index].dist
        count = len(self.minHeap)
        # If has no children, then stop
        if (count < 2 * count):
            pass
        # If only has a left child, check if need to swap
        elif (count < (2 * count + 1)):
            if (distance > self.minHeap[index * 2].dist):
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[index * 2]
                self.minHeap[index * 2] = temp
        # If has both children, then swap with left or right if need be, then
        # recursively propogate to the children
        else:
            if (distance > self.minHeap[index * 2].dist):
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[index * 2]
                self.minHeap[index * 2] = temp
                index = index * 2
                __PropagateDown(self, index)
            elif (distance > self.minHeap[index * 2 + 1].dist):
                temp = self.minHeap[index]
                self.minHeap[index] = self.minHeap[index * 2 + 1]
                self.minHeap[index * 2 + 1] = temp
                index = index * 2 + 1
                __PropagateDown(self, index)













