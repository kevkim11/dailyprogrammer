"""
https://www.reddit.com/r/dailyprogrammer/comments/5j6ggm/20161219_challenge_296_easy_the_twelve_days_of/

Description:
Python 2.7.6
Print out the lyrics of The Twelve Days of Christmas
We want to have our source code as small as possible.

Input:
No Input

Output:
On the first day of Christmas
my true love sent to me:
1 Partridge in a Pear Tree

On the second day of Christmas
my true love sent to me:
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the third day of Christmas
my true love sent to me:
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the fourth day of Christmas
my true love sent to me:
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the fifth day of Christmas
my true love sent to me:
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the sixth day of Christmas
my true love sent to me:
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the seventh day of Christmas
my true love sent to me:
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the eighth day of Christmas
my true love sent to me:
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the ninth day of Christmas
my true love sent to me:
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the tenth day of Christmas
my true love sent to me:
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the eleventh day of Christmas
my true love sent to me:
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree

On the twelfth day of Christmas
my true love sent to me:
12 Drummers Drumming
11 Pipers Piping
10 Lords a Leaping
9 Ladies Dancing
8 Maids a Milking
7 Swans a Swimming
6 Geese a Laying
5 Golden Rings
4 Calling Birds
3 French Hens
2 Turtle Doves
and 1 Partridge in a Pear Tree
"""
if __name__ == "__main__":
    days = ["first", "second", "third", "fourth", "fifth", "sixth",
            "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gifts = ["Partridge in a Pear Tree", "Turtle Doves", "French Hens", "Calling Birds", "Golden Rings",
             "Geese a Laying", "Swans a Swimming", "Maids a Milking", "Ladies Dancing", "Lords a Leaping",
             "Pipers Piping", "Drummers Drumming"]
    for i, day in enumerate(days):
        print "On the %s day of Christmas" % day
        print "my true love sent to me:"
        list_of_enumerates = list(enumerate(gifts))
        for ii, gift in list_of_enumerates[i::-1]:
            if day!="first" and ii==0:
                print ("and %s " + str(gift)) % str(ii + 1)
            else:
                print ("%s " + str(gift)) % str(ii + 1)
        print
