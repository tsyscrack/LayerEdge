import os
from eth_account import Account

if __name__ == '__main__':
    # account = Account.create()
    # print('%s,%s'%(account.address,account.key.hex()))
    file_name = 'accounts.txt'
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        j=1
        n = 1000

        for i in range(n):
            Account.enable_unaudited_hdwallet_features()
            account, mnemonic = Account.create_with_mnemonic()
            num = '第%d个钱包' % j
            print(num)
            line =('%s' % (account.key.hex())) #mnemonic助记词
            print(line)
            j = j + 1
            with open(file_name, 'a') as f:
                f.write(line + '\n')