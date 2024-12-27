import os
import csv

def vote_analysis(data_set):

    vote_count = 0
    candidates = []
    can_count = []
    vote_dict = {}

    py_bank_csv = os.path.join("c:\\Users\\stoyt\\Desktop\\data_bootcamp\\Python_Challenge\\Starter_Code\\PyPoll\\Resources", data_set)


    with open(py_bank_csv) as py_bank:

        csvreader = csv.reader(py_bank, delimiter=",")
        csv_header = next(csvreader, None)

        for row in csvreader:
            vote_count += 1
            candidate = row[2]

            if candidate not in candidates:
                candidates.append(candidate)

            can_count.append(candidate)

        for candidate in candidates:
            vote_dict[candidate] = 0
            
            for name_count in can_count:
                if candidate == name_count:
                    vote_dict[candidate] += 1

            votes = vote_dict[candidate]

            percentage = (votes / vote_count) * 100

            vote_dict[candidate] = {"votes": votes, "percentage": percentage}

    winner = max(vote_dict, key=lambda x: vote_dict[x]['votes'])

    output = [
        ("Election Results"),
        ("------------------"),
        (f"Total Votes: {vote_count}"),
        ("------------------"),
        *[f"{candidate}: {vote_dict[candidate]['percentage']:.3f}% ({vote_dict[candidate]['votes']})" for candidate in vote_dict],
        ("------------------"),
        (f"Winner: {winner}")
        ]
    
    result ="\n".join(output)

    with open("election_analysis.txt", "w") as text_file:
        text_file.write(result)

    return result

print(vote_analysis("election_data.csv"))