def timeConversion(s):
    arr = s.split(":")
    arr.append(arr[-1][2:])
    arr[-2] = arr[-2][:2]
    if arr[-1] == "PM":
        if arr[0] != "12":
            new_hour = int(arr[0]) + 12
            if new_hour == 24:
                new_hour = "00"
            arr[0] = str(new_hour)
    else:
        if arr[0] == "12":
            arr[0] = "00"
    return arr[0] + ":" + arr[1] + ":" + arr[2]


if __name__ == '__main__':
    print(timeConversion("12:01:01PM"))