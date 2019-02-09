# https://www.hackerrank.com/challenges/time-conversion/problem


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    am_or_pm = s[-2:]
    time_in_12_hours_fmt = s[:-2].split(':')

    if am_or_pm == 'AM':
        if time_in_12_hours_fmt[0] == '12':
            time_in_12_hours_fmt[0] = '00'
    else:
        if time_in_12_hours_fmt[0] != '12':
            time_in_12_hours_fmt[0] = str(int(time_in_12_hours_fmt[0]) + 12)

    return ':'.join(time_in_12_hours_fmt)
