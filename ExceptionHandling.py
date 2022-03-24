try:
    age = 10
    if age<18:
        raise ValueError("Not eligible for vote")
    else:
        print("eligible for vote")
except ZeroDivisionError as e:
    print("Exception occured = > " + str(e))
except ValueError as e:
    print("Exception => "+ str(e))
except:
    print("Exception occured")
else:
    print("Program executed successfuly...")


finally:
    print("Harman Ltd")