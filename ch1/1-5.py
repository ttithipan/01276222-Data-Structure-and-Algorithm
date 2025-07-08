bids = [int(bid) for bid in input("Enter All Bid : ").split()]
bids.sort()
if len(bids) < 2:
    print("not enough bidder")
elif bids[-1] == bids[-2]:
    print("error : have more than one highest bid")
else:
    print(f"winner bid is {bids[-1]} need to pay {bids[-2]}")