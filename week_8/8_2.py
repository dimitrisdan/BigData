from mrjob.job import MRJob
from mrjob.step import MRStep


class EulerTour(MRJob):

    def mapper(self, _, line):
        nodes = line.split()
        for node in nodes:
            yield node, 1;

    def reducer(self, key, values):
        yield None, sum(values);

    def reducer_euler(self, _, edges):
        yield "Does the Graph has an Euler Tour?", self.is_even(edges);

    def steps(self):
        return [MRStep(mapper=self.mapper, reducer=self.reducer), MRStep(reducer=self.reducer_euler)];

    def is_even(self, num):
        for node in num:
            if node % 2 != 0:
                return False
        return True;

if __name__ == '__main__':
    EulerTour.run()