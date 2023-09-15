"""6 kyu
Statistics for an Athletic Association
81416289% of 1,4403,012 of 8,804g9644 Issues Reported
 Python
3.11
VIM
EMACS
Instructions
Output
You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete.
Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:
"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
Each part of the string is of the form: h|m|s where h, m, s
(h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits.
Substrings in the input string are separated by ,  or ,.
To compare the results of the teams you are asked for giving three statistics; range, average and median.
Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.
Mean or Average : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.
Median : In statistics, the median is the number separating the higher half of a data sample from the lower half.
The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value
and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations.
f there is an even number of observations, then there is no single middle value;
the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).
Your task is to return a string giving these 3 values. For the example given above, the string result will be
"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"
of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`
where hh, mm, ss are integers (represented by strings) with each 2 digits.
Remarks:
if a result in seconds is ab.xy... it will be given truncated as ab.
if the given string is "" you will return ""
FUNDAMENTALSSTRINGSSTATISTICSMATHEMATICSDATA SCIENCE"""

from datetime import datetime, timedelta
strg="01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"
def stat(strg):
    if not strg =="":
        race_results= list(strg.split(", "))
        def listToString(s, char):
            str1 = ""
            for ele in s:
                str1 += ele+char
            return str1[:-1]
        def uniform_format(race_results, char):
            uniform_f_results=[]
            for s in race_results:
                result=list(s.split('|'))
                new_result=[]
                for unit in result:
                    if len(unit)==1:
                        new_unit="0"+unit
                    else:
                        new_unit=unit
                    new_result.append(new_unit)
                new_result=listToString(new_result,char)
                uniform_f_results.append(new_result)
            return uniform_f_results

        race_results=uniform_format(race_results, ":")
        def time_converter(time_str):
            time_object=datetime.strptime(time_str, "%H:%M:%S").time()
            return time_object

        race_results_dt=[]
        for time in race_results:
            race_results_dt.append(time_converter(time))

        race_result_delta=[]
        for t in race_results_dt:
            race_result_delta.append(timedelta(hours=t.hour, minutes=t.minute, seconds=t.second))
        race_result_delta.sort()

        def minmax(val_list):
            min_val = min(val_list)
            max_val = max(val_list)
            return (min_val, max_val)

        def chop_microseconds(delta):
            return delta - timedelta(microseconds=delta.microseconds)

        min_val ,max_val = minmax(race_result_delta)
        range= max_val-min_val
        mean= sum(race_result_delta,timedelta())/len(race_result_delta)
        mid = len(race_result_delta)//2
        median=(race_result_delta[mid]+race_result_delta[~mid])/2

        range_str= f"{chop_microseconds(range)}".replace(":","|")
        if len(range_str)==7:
            range_str="0"+range_str
        else:
            range_str

        mean_str=f"{chop_microseconds(mean)}".replace(":","|")
        if len(mean_str)==7:
            mean_str="0"+mean_str
        else:
            mean_str
        median_str=f"{chop_microseconds(median)}".replace(":","|")
        if len(median_str)==7:
            median_str="0"+median_str
        else:
            median_str

        return f"Range: {range_str} Average: {mean_str} Median: {median_str}"
    else:
        return strg

print(stat(strg))
























