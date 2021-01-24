'''
Tools for cooperation with Homeworlds Live sit

Example log string:

Players: south,north
Winner: none
h,g3C,b1C,y3C
h,r2C,b1B,g3B
b,y1A,1
b,g1A,2
b,y1B,1
b,g1B,2
d,y1A,g2C
t,g1B,y1C
b,y2A,3
b,g1B,2
t,y1B,g1C
d,g1B,b3C
b,g2A,1
s,g3B;b,g2B,4;b,g3A,4;b,g3B,2

t,g3A,r3C

Example map string:

{
    "map": {
    "b1A": null,
    "b1B": {"at": 2, "owner": null},
    "b1C": {"at": 1, "owner": null},
    "b2A": null,
    "b2B": null,
    "b2C": null,
    "b3A": null,
    "b3B": null,
    "b3C": {"at": 4, "owner": null},

    "g1A": {"at": 2, "owner": "north"},
    "g1B": {"at": 4, "owner": "north"},
    "g1C": {"at": 1, "owner": "south"},
    "g2A": {"at": 1, "owner": "south"},
    "g2B": {"at": 4, "owner": "north"},
    "g2C": {"at": 3, "owner": null},
    "g3A": null,
    "g3B": {"at": 2, "owner": "north"},
    "g3C": {"at": 1, "owner": null},

    "r1A": null,
    "r1B": null,
    "r1C": null,
    "r2A": null,
    "r2B": null,
    "r2C": {"at": 2, "owner": null},
    "r3A": null,
    "r3B": null,
    "r3C": {"at": 4, "owner": "north"},

    "y1A": {"at": 3, "owner": "south"},
    "y1B": null,
    "y1C": {"at": 2, "owner": "north"},
    "y2A": {"at": 3, "owner": "south"},
    "y2B": null,
    "y2C": null,
    "y3A": null,
    "y3B": null,
    "y3C": {"at": 1, "owner": "south"}
    },
"homeworldData": {"south":1,"north":2}
}
'''
