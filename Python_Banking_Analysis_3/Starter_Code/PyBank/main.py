import os
import csv

def bank_analysis(data_set):

    month_count = 0
    total = 0
    changes = []
    month_change = 0
    max_month_change = 0
    max_decrease = 0

    py_bank_csv = os.path.join("c:\\Users\\stoyt\\Desktop\\data_bootcamp\\Python_Challenge\\Starter_Code\\PyBank\\Resources", data_set)


    with open(py_bank_csv) as py_bank:

        csvreader = csv.reader(py_bank, delimiter=",")

        csv_header = next(csvreader, None)

        prev_value = None

        for row in csvreader:
            month_count += 1
            total += int(row[1])

            if prev_value is not None:
                month_change = int(row[1]) - prev_value
                changes.append(month_change)
                if month_change > max_month_change:
                    max_month_change = month_change
                    month_inc = row[0]
                elif month_change < max_decrease:
                    max_decrease = month_change
                    month_dec = row[0]
            prev_value = int(row[1])

    avg_change = round(sum(changes) / len(changes), 2)

    output = [
            ("Financial Analysis"),
            ("------------------"),
            (f"Total months: {month_count}"),
            (f"Total: ${total}"),
            (f"Average Change: ${avg_change}"),
            (f"Greatest Increase in Profits: {month_inc} ${max_month_change}"),
            (f"Greatest Decrease in Profits: {month_dec} ${max_decrease}")
    ]
    
    result ="\n".join(output)

    with open("financial_analysis.txt", "w") as text_file:
        text_file.write(result)

    return result

print(bank_analysis("budget_data.csv"))      