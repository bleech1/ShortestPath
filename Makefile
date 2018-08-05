.PHONY: all
all: findPath

.PHONY: findPath
findPath: shortestPath.py 
	python ./shortestPath.py

.PHONY: clean
clean:
	rm -f middWalk
