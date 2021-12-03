#!/usr/bin/env python3.8

"""
	You are a in-flight movie service provider. You are given a list of movie lengths and the duration of the flight. 
	Return a pair of (2) movies whose combined length is the highest and is less than or equal to flight duration. 
	If multiple such combinations are possible, return the pair which has the movie of longer longest duration.
"""

def movieServiceProvider(movie_duration_List, flight_duration):
	"""
		Assuming users will watch exactly two movies.
		assuming 2 movies do not have same length
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
				if (min_new, max_new) not in possible_pairs:
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
		using sorting
		O(n(log n))+ O(n/2) = O(n(log n)) time complexity
	"""
	def search():
		s = sorted(movie_duration_List)
		l = 0
		r = len(s)-1
		while l<r:
			if s[l] + s[r] <= flight_duration:
				yield s[l], s[r]
				l += 1
			else:
				r -= 1
	output = max(search(), key=sum)
	print(" ".join(map(str, output)))



movie_duration_List = [1, 3, 12, 27, 32, 39, 52, 67, 74, 75]
flight_duration = 77
print(21,77,(1, 76))
movieServiceProvider(movie_duration_List, flight_duration)
movieServiceProvider1(movie_duration_List, flight_duration)

# movie_duration_List = [90, 85, 75, 60, 120, 150, 125]
# flight_duration =  250
# print(19,245,(120, 125))
# movieServiceProvider(movie_duration_List, flight_duration)

# movie_duration_List = [90, 85, 75, 60, 155, 150, 125]
# flight_duration =  250
# print(18,245,(90, 155))
# movieServiceProvider(movie_duration_List, flight_duration)

# movie_duration_List = [90, 85, 75, 60, 120, 110, 110, 150, 125]
# flight_duration =  250
# print(26,245,(120, 125))
# movieServiceProvider(movie_duration_List, flight_duration)

# movie_duration_List = [95, 85, 75, 60, 120, 110, 110, 150, 125]
# flight_duration =  250
# print(26,245,(95, 150))
# movieServiceProvider(movie_duration_List, flight_duration)

# movie_duration_List = [1, 10, 25, 35, 60]
# flight_duration =  90
# print(9,85,(25, 60))
# movieServiceProvider(movie_duration_List, flight_duration)

# movie_duration_List = [20, 50, 40, 25, 30, 10]
# flight_duration =  90
# print(15,90,(40, 50))
# movieServiceProvider(movie_duration_List, flight_duration)

# movie_duration_List = [5, 55, 40, 20, 30, 30]
# flight_duration =  90
# print(10,85,(30, 55))
# movieServiceProvider(movie_duration_List, flight_duration)
