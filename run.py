from booking import Booking

# inst = Booking()
# inst.land_first_page()
with Booking(teardown=False) as bot:
    bot.land_first_page()
    # bot.change_currency(currency='USD')
    bot.select_place_to_go('Toronto')
    bot.select_date(check_in_date='2022-09-25',
                    check_out_date='2022-10-30', x=2)
    bot.select_adult(3)
    bot.click_search()
    bot.apply_filtrations()

    print('Completed !')
