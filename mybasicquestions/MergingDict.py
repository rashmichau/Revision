# Merging two dictonaries
name1 ={"Rahul": 1,"Reema":2,"Seema":3,"rekha":4}
name2 ={"Amit":5,"Suraj":6,"Nagendra":7}
names =(name1|name2)
print(names)

namess={**name1,**name2}
print(namess)