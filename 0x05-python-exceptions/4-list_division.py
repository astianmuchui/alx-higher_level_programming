#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new = []
    res = 0

    for i in range(list_length):

        try:
            res = my_list_1[i] / my_list_2[i]

        except IndexError:

            res = 0
            print("Out of range")
            pass

        except ZeroDivisionError:
            res = 0
            print("division by zero")
            pass

        except TypeError:
            res = 0
            print("wrong type")
            pass

        except Exception:
            res = 0
            pass

        finally:
            new.append(res)

    return (new)
