import os
import statistics as stcs 
import csv

bank_data = os.path.join('Resources','budget_data.csv')

no_months = [] # List of Months
profit_count = [] # A list with just profits
loss_count = [] # A list with just losses
ProLo_count = [] # A list including profits and losses
ch_rate_list = [] # A list of the changes 
#i = 0

with open(bank_data) as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    header = next(csvread) #Jumps the header

    # Creating the Profit, Loss, and Profit/Loss list
    for rows in csvread:
        no_months.append(rows[0])

        if int(rows[1]) > 0:
            profit_count.append(int(rows[1]))
            
        else:
            loss_count.append(int(rows[1]))
        
        ProLo_count.append(int(rows[1]))
    
    # Creating the Change list
    for i, element in enumerate(ProLo_count):
       
         if i > 0:
             ch_rate = ProLo_count[i]-ProLo_count[i-1]
             ch_rate_list.append(ch_rate)

    # Obtaining the indexes of Max and Min to match with month
    max_chng = ch_rate_list.index(max(ch_rate_list))
    min_chng = ch_rate_list.index(min(ch_rate_list))  

    print(f'Financial analysis')
    print('----------------------')
    print(f'Total months: {len(no_months)}')
    print(f'Total Profit/Loss: {"${:,.0f}".format(sum(ProLo_count))}')
    print(f'Average Change: {"${:,.2f}".format(round(stcs.mean(ch_rate_list),2))}')
    print(f'The greatest increse in profit was: {no_months[max_chng+1]} with {"${:,.0f}".format(max(ch_rate_list))}')
    print(f'The greatest decrease in profit was: {no_months[min_chng+1]} with {"${:,.0f}".format(min(ch_rate_list))}')

    

        
