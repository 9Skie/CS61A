Friends = ["Kevin", "Victor", "Christoph", "John", "Antonio", "Henry" ]

print("So who is a friend of mine?")
print("I already have a list in mind, let me think... " + str(Friends))

Friends.append("Kibeom")
print("Hmm, something feels missing from here. Kibeom! how can I forget him! so it should be... " + str(Friends))

Friends.remove("John")
print("Sure, John and I were good friends before, but we never got in touch with each other later, so he's off, and now... "+ str(Friends))

Friends.clear()
print("All of us have seperated into our own paths and no longer intertwine with each other, so... farewell, momories of the past. ")
print("So who is a friend of mine? How many friends do I have? " + str(Friends.count("true friend"))+ ", no-one ever.")

print("No one has ever stepped into this closed heart.")
print("None.")

############
# Now at Scie, I feel like a numb wooden puppet doing the same repetative work just for the funny assumption of capabalities of a person "grades"
# All that surrounds me is disgust and hate to this nihilistic world, only comprised of cold blooded machines that only cares for kpi and gpa
############

Friends2 = Friends.copy()
print("Even in a coming new semester at a new school, it will still be " + str(Friends2.count("true friend")))