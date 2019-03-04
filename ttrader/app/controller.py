from app.account import Account
from app.view import View 
from app.util import get_price, gen_api_key
import time 

view = View()


def run():
    welcome_homepage()


def welcome_homepage():
    while True:  
        selection = view.welcome_screen()
        if selection not in ["1","2","3"]:
            view.improper_selection()
            continue 

        if selection == "1":
            username, balance, api = view.get_username(), view.add_balance(), gen_api_key()

            # if password != confirm_password:
            #     view.improper_password()
            #     continue  
            # if not balance.isdigit() or int(balance) < 0:
            #     view.improper_balance()
            #     continue
            
            account = Account(username = username, balance = balance, api_key=api)
            # hashed_pw = Account.set_password(account, password)
            # account.save()
            logged_in_homepage(account)
            return 
        elif selection == "2":
            username, api_key = view.get_username(), view.get_api_key()
            logged_in_account = Account.api_auth(username=username, api_key=api_key)
            
            if logged_in_account:
                logged_in_homepage(logged_in_account)
                return
            else:
                view.wrong_key()
                continue
        elif selection == "3":
            view.goodbye()
            return


def logged_in_homepage(account):
    
    while True:
        selection = view.logged_in_screen(account.username, account.balance,account.api_key)
        
        if selection not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            view.improper_selection()
            time.sleep(3)
        
        if selection == "1":
            positions = Account.get_positions(account)
            if positions:
                view.positions_username(account.username)
                for position in positions:
                    time.sleep(1)
                    view.positions(account, position)
                    time.sleep(1)
        elif selection == "2":
            deposit = view.deposit_funds()
            if not deposit.isdigit() or int(deposit) < 1:
                view.improper_balance()
                time.sleep(3)
            else:
                account.balance = int(account.balance) +  int(deposit)
                account.save()
                continue
        elif selection == "3":
            ticker_request = view.request_ticker_symbol()
            ticker_response = get_price(ticker_request)
            if type(ticker_response) == list:
                view.return_ticker_symbol_price(ticker_response)
                time.sleep(3)
            else:
                view.improper_ticker()
                time.sleep(3)
        elif selection == "4":
            ticker = view.request_ticker_symbol()
            current_price = get_price(ticker)
            share_amount = view.sell_shares()
            # Account.buy(account, ticker, share_amount, current_price)
            try:
                Account.buy(account, ticker, share_amount, current_price)
            except ValueError:
                    # time.sleep(1)
                    view.insufficient_funds()
                    view.clear_screen()
        
            # try:
            #     current_price = current_price[1]
            # except TypeError:
            #     view.oops()
            # total_cost = int(current_price) * int(share_amount)
            # if current_price and share_amount.isdigit() and total_cost < account.balance:
            #     Account.buy(account, ticker, share_amount, current_price[1], total_cost)
            # elif total_cost > account.balance:
            #     view.oops()
            #     time.sleep(3)
            # else:
            #     view.improper_ticker()
            #     time.sleep(3)
            # while True:
            #     try:
            #     except TypeError:
            #         view.oops()
            #         time.sleep(3)
            #         view.clear_screen()
            # else:

            #     view.improper_ticker()
            #     time.sleep(3)
        elif selection == '5':
            ticker = view.request_ticker_symbol()
            shares = view.sell_shares()
            try:
                Account.sell(account, ticker, shares)
            except ValueError:
                    view.oops()
                    time.sleep(3)
                    view.clear_screen()
            # else:
            #     view.improper_ticker()
            #    if amount.current_value > amount:
            #        amount += amount.current_value
            #        Account.sell(account, ticker, amount)

        elif selection == "6":
            selection = view.select_trade_option(account.username)
            
            if len(selection) != 1 or selection.lower() not in ["a", "b", "c"]:
                view.improper_selection()
                time.sleep(3)
            elif selection.lower() == "a":
                account_trades = Account.get_trades(account)
                for trade in account_trades:
                    view.show_trades(account.username, trade)
                    time.sleep(3)
            elif selection.lower() == "b":
                ticker_symbol = view.request_ticker_symbol()
                account_trades_by_ticker = Account.trades_for(account, ticker_symbol)
                
                if account_trades_by_ticker:
                    for trade in account_trades_by_ticker:
                        view.show_trades(account.username, trade)
                        time.sleep(3)

                else:
                    view.improper_ticker()
                    time.sleep(3)
            elif selection.lower() == "c":
                continue
        elif selection == "7":
            view.goodbye()
            welcome_homepage()
            return
        elif selection == "8":
            view.goodbye()
            return
        


"""TODO 
   develop the view for the login screen and the controller options for it
   see the below for inspiration
""" 



"""
Sample execution

Welcome to Terminal Trader!
    
    1. create account
    2. login
    3. quit

Your choice: 2.


Main Menu:

    1. see balance & positions
    2. deposit money
    3. look up stock price
    4. buy stock
    5. sell stock
    6. trade history

etc.


you should have useful output if a user inputs a stock that does not exist

you should not allow a user to spend money they don't have or sell
shares they don't have

your display of positions or trades should be well-formatted, don't
just print a python list
"""
