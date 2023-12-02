let mp = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    '0':'0',
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
};
`two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen`.split('\n').map(x => {
    let first = [234789, 'a'];
    let last = [-1, 'a'];
    for (const [k,v] of Object.entries(mp)) {
        const xk = x.indexOf(k);
        if (xk < 0) continue;
        if (xk < first[0]) first = [xk, v];
        if (xk > last[0]) last = [xk, v];
    }
    console.log(first,last);
    return +(first[1] + last[1]);
}).reduce((a,b)=>a+b);