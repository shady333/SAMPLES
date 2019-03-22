def fibonachi(number):
    if number == 0:
        return 0;
    if number == 1:
        return 1;
    else:
        return fibonachi(number - 1) + fibonachi(number -2);
