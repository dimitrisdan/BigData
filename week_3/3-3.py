import pandas

movies = pandas.read_table("movies.dat",sep="::",index_col=False,names=["movie id","title","genre"],engine="python")
ratings = pandas.read_table("ratings.dat",sep="::",index_col=False,names=["user id","movie id","rating","timestamp"],engine="python")
users = pandas.read_table("users.dat",sep="::",index_col=False,names=["user id","gender","age", "occupation code", "zip"],engine="python")

movie_data = pandas.merge(pandas.merge(users,ratings),movies)
title_group = movie_data.groupby("title").size().order(ascending=False)
active_titles = title_group[title_group > 250].index

print title_group[:5]
print active_titles