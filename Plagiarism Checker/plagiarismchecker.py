from difflib import SequenceMatcher

with open("Plagiarism Detection/demo1.txt") as one_file, open(
    "Plagiarism Detection/demo2.txt"
) as two_file:
    data_file1 = one_file.read()
    data_file2 = two_file.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f"The Plagiarized Content is {matches*100}%")
