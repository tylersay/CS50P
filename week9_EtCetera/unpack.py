############################
# Unpacking
############################

##########################
# # total(coins) will pass value only into galleons arguement
# # using "*" will unpack individual members of list
##########################
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) *29 + knuts

# coins = [100, 50, 25]
# print(f"{total(*coins)} knuts")




# ##########################
# ## using "**" will unpack individual members of dictionary,
# ## unpack keys-values
# ##########################
# def total(galleons, sickles, knuts):
#     return (galleons * 17 + sickles) *29 + knuts

# coins = {"galleons": 100, "sickles": 50, "knuts":25}
# print(f"{total(**coins)} knuts")



def f(*args, ** kwargs):
    print("Positional:", args)
    print("Named:", kwargs)
pennies = 10
f(100, 50, 25, pennies=7)