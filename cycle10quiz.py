# Author: SCT (AMDG) 2/2/22

prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

# 1
def averge(prices, result): # Def dunction
    for x in prices: # find indv value of prices
        i = 0 # sets base index
        result += result + x[i] # adds each value to result
        i += 1 # counter
        final = result / (i - 1) # divides the list by total elements to get average
        return final

print(averge(prices, 0))


# 2
def price_5(prices, answer): # def function
    for i, v in enumerate(prices): # seperate index and value of prices to use
        i = 0 # sets base index as 0 to count
        answer += answer + (v[i] - 5) # adds answer list to each iteration of price subtracted by 5
        i += 1 # counts up for each iteration

print(price_5(prices))


# 3
def prep_sales(prices,sales, answer): # def function
    for x in prices: 
        for y in sales: # seperate value from both inputs
            i = 0 # base index as 0
            answer += y[i]+ 'item was sold for' + x[i] + '$' # sets up formating for final result
            i += 1 # counter
            return answer
    
print(prep_sales(prices, sales, 0))

price_mod = prices
# 4
def cost_40(prices, want): # def function
    for v in prices:
        i = 0 # base index
        if v[i] <= 40: # checks if greater than 40
            want += v
        else:
            want += v - 10 # checks if greater than 4o than subtracts 10
            i += 1
            return want

            

