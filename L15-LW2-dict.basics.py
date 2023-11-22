# python type / dict

# * dict - keyed collection (collection of key=value pairs)

# formula value = {unique key : value}

# indexed (list) -> homogenous

todo = {
    # key        :      value
    "2021-04-02" :  "Become a dev",
    "2021-04-01" :  "Learn Pyton",
    "2021-04-03" :  "Earn a million"
}

todo["2021-04-10"] = "Be sad!!!"
todo["2021-04-10"] = "Be happy!!!"

print (todo)
print (todo["2021-04-10"])
