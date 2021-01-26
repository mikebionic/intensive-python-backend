# 'q' and 'a' are "question" and "answer"

qa_list = [["What is the capital of T-n? - ", "Ashgabat"],
		   ["7 x 8? - ", "56"],
		   ["President of Russia? - ", "Putin"],
		   ["Which CVS do we use? - ", "Git"],
		   ["Who is the best? - ", "I am"]]

qa_tuple = tuple((tuple(x) for x in qa_list)) # the same "qa_list", but tuple

qa_dict = dict(qa_list) # the same "qa_list", but dictionary


def list_version():
	# working with "qa_list"

	life = 3
	correct_answer = 0
	incorrect_answer = 0

	for i in range(len(qa_list)):
		if life != 0:
			answer = input(qa_list[i][0]).capitalize()
			if answer == qa_list[i][1]:
				correct_answer += 1
				print("Correct!\n")
			else:
				incorrect_answer += 1
				life -= 1
				print(f"Incorrect! You have {life} chance.\n")

	if life == 0:
		print("Fail")
	else:
		print(f"Your score is {correct_answer}.")


# with qa_tuple will be the same function

'''with qa_dict we change "for i in range(len(qa_list)):" to "for i in qa_dict:",
   "qa_list[i][0]" to "i" and "qa_list[i][1]:" to "qa_dict[i]:", others will be
   the same.
'''


if __name__ == "__main__":
	list_version()