const input = `35
111
135
32
150
5
106
154
41
7
27
117
109
63
64
21
138
98
40
71
144
13
66
48
12
55
119
103
54
78
65
112
39
128
53
140
77
34
28
81
151
125
85
124
2
99
131
59
60
6
94
33
42
93
14
141
92
38
104
9
29
100
52
19
147
49
74
70
84
113
120
91
97
17
45
139
90
116
149
129
87
69
20
24
148
18
58
123
76
118
130
132
75
110
105
1
8
86`;

const arr = input.split('\n').map(num => Number.parseInt(num)).sort((a, b) => a - b)

oneDifference = 0
threeDifference = 1
lastNum = 0

for (adapter of arr) {
    difference = adapter - lastNum
    lastNum = adapter
    if (difference === 1) {
        oneDifference += 1
    } else if (difference === 3) {
        threeDifference += 1
    }
}

console.log(`Answer 1 ${oneDifference * threeDifference}`)

let dTable = Array(arr[arr.length -1] ).fill(0);
dTable[0] = 1;
for (adapter of arr) {
    oneBack = dTable[Math.max(0, adapter - 1)]
    twoBack = dTable[adapter - 2] || 0
    threeBack = dTable[adapter - 3] || 0

    dTable[adapter] = oneBack + twoBack + threeBack
}
console.log(`Answer 2 ${dTable[dTable.length - 1]}`)

