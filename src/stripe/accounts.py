def balance_accounts(accounts):
    transactions = []

    for i in range(len(accounts)):
        if accounts[i][1] < 100:
            less_than = accounts[i][1]
            lesser_difference = 100 - less_than

            for j in range(len(accounts)):
                if accounts[i][1] >= 100:
                    break
                if accounts[j][1] > 100:
                    greater_than = accounts[j][1]
                    greater_difference = greater_than - 100

                    if greater_difference >= lesser_difference:
                        transaction_amount = lesser_difference

                        accounts[i] = (accounts[i][0], accounts[i][1]+transaction_amount)
                        accounts[j] = (accounts[j][0], accounts[j][1]-transaction_amount)

                        transactions.append("from: {0}, to: {1}, amount: {2}".format(accounts[j][0], accounts[i][0],
                                                                                     transaction_amount))
                        break
                    else:
                        transaction_amount = greater_difference
                        accounts[i] = (accounts[i][0], accounts[i][1] + transaction_amount)
                        accounts[j] = (accounts[j][0], accounts[j][1] - transaction_amount)

                        transactions.append("from: {0}, to: {1}, amount: {2}".format(accounts[j][0], accounts[i][0],
                                                                                     transaction_amount))
                        j -= 1

    return transactions


if __name__ == "__main__":
    accounts = [("CA", 80), ("US", 140), ("GB", 110), ("DE", 120), ("FR", 70)]

    print(balance_accounts(accounts))
