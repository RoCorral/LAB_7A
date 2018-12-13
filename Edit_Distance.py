"""
@author Rocorral
ID: 80416750
Instructor: David Aguirre
TA: Saha, Manoj Pravakar
Assignment:Lab 7-A -Edit Distance
Last Modification: 12/12/2018
Program Purpose: The purpose of this program is to practice the
implementation of the dynamic algorythrm known as edit distance
"""

import io
def edit_distance_compute(word1, word2):
	"""takes in words from file and computes edit distance"""
	if len(word1)> len(word2): #less iterations of exterior for loops if its string is shorter
		word1,word2 =word2,word1 

	
	distance_array = range(len(word1)+1) #first row with edit distance from empty character
	i=0
	for i_letter in word2:
		distance = [i+1]#new row with value of edit distance from empty character
		j=0
		for j_letter in word1:
			if j_letter == i_letter:
				distance.append(distance_array[j]) # if equal apend the value at row above J to new row distance
			else:
				distance.append(1+ min(distance_array[j],distance_array[j+1],distance[-1]))#not equal find min of either row at index directly above or that -1 or this row -1
			j+=1
		distance_array=distance#update main array to compute next
		i+=1

		print distance_array
	return distance_array[-1] #returns last item




def read_file(file):
	for_edit_distance = io.open(file ,'r+', encoding = "UTF-8")
	for line in for_edit_distance:
		a = line.split(' ')
		word1 = a[0]
		word2 = a[1]
		print("edit distance between ",word1, " and ",word2, " is: ",edit_distance_compute(word1,word2))
read_file("words.txt")