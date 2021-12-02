#!/usr/bin/env python3.8

"""
	You are a in-flight movie service provider. You are given a list of movie lengths and the duration of the flight. 
	Return a pair of (2) movies whose combined length is the highest and is less than or equal to flight duration. 
	If multiple such combinations are possible, return the pair which has the movie of longer longest duration.
"""

def movieServiceProvider(movie_duration_List, flight_duration):
	"""
		Assuming users will watch exactly two movies.
		O(n2) time complexity
	"""
	possible_pairs = []
	max_sum = 0
	max_sum_max_index = None
	for i in range(len(movie_duration_List)):
		for j in range(len(movie_duration_List)):
			if (i != j and movie_duration_List[i] + movie_duration_List[j] <= flight_duration):
				min_new = min(movie_duration_List[i], movie_duration_List[j])
				max_new = max(movie_duration_List[i], movie_duration_List[j])
				sum_new = min_new+ max_new
				possible_pairs.append((min_new, max_new))
				if sum_new >= max_sum:
					if sum_new == max_sum:
						if max_sum_max_index != None and possible_pairs[max_sum_max_index][1] < max_new:
							max_sum_max_index = len(possible_pairs)-1
					else:
						max_sum = sum_new
						max_sum_max_index = len(possible_pairs)-1
	print("movie lengths :", movie_duration_List, "flight duration : ", flight_duration)
	print("Total count of possible pair of movies : ",len(possible_pairs))
	print("all possible pair of movies : ",possible_pairs)
	print("Best possible movie length : ", max_sum)
	print("Best possible movie duration : ", possible_pairs[max_sum_max_index])
	print("-"*200)

def movieServiceProvider1(movie_duration_List, flight_duration):
	"""
		Assuming users will watch exactly two movies.
		using hash function
		O(1) time complexity
	"""
	hash_movie = {}
	for i in range(len(movie_duration_List)):
		match = flight_duration - movie_duration_List[i]
		if hash_movie[match] == True:
			pass


movie_duration_List = [27, 1,10, 39, 12, 52, 32, 67, 76]
flight_duration = 77
movieServiceProvider(movie_duration_List, flight_duration)

movie_duration_List = [90, 85, 75, 60, 120, 150, 125]
flight_duration =  250
movieServiceProvider(movie_duration_List, flight_duration)
movie_duration_List = [90, 85, 75, 60, 155, 150, 125]
flight_duration =  250
movieServiceProvider(movie_duration_List, flight_duration)
movie_duration_List = [90, 85, 75, 60, 120, 110, 110, 150, 125]
flight_duration =  250
movieServiceProvider(movie_duration_List, flight_duration)
movie_duration_List = [95, 85, 75, 60, 120, 110, 110, 150, 125]
flight_duration =  250
movieServiceProvider(movie_duration_List, flight_duration)
movie_duration_List = [1, 10, 25, 35, 60]
flight_duration =  90
movieServiceProvider(movie_duration_List, flight_duration)
movie_duration_List = [20, 50, 40, 25, 30, 10]
flight_duration =  90
movieServiceProvider(movie_duration_List, flight_duration)
movie_duration_List = [5, 55, 40, 20, 30, 30]
flight_duration =  90
movieServiceProvider(movie_duration_List, flight_duration)