from mrjob.job import MRJob


class CommonFriends(MRJob):

    def mapper(self, _, line):

        origin = line.split("->")[0]
        con = list(line.split("->")[1])

        for letter in con:
            pair = "".join(sorted([origin,letter]))
            yield sorted([origin,letter]),con



    def combiner(self, key, values):
         yield key, list(values)

    def reducer(self, key, values):
        u = values.next()
        yield key,list(set(u[0]).intersection(set(u[1])))


if __name__ == '__main__':
    CommonFriends.run()