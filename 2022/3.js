// part 1
fetch("https://adventofcode.com/2022/day/3/input").then(x=>x.text()).then(data=>{
    let sum = 0;
    const lines = data.split('\n').filter(x=>x);
    for(const line of lines){
        let dupe = {};
        let dict = {};
        for(let i = 0; i < line.length; i ++){
            if(i < line.length/2) dict[line[i]] = 1;
            else if(dict[line[i]]){
                // console.log(line[i]);
                dupe[line[i]] = 1;
            }
        }
        for(const c of Object.keys(dupe)){
            // console.log(sum);
            sum += c.toLowerCase().charCodeAt(0) - "a".charCodeAt(0) + 1 + (c == c.toUpperCase() ? 26 : 0);
        }
    }
    console.log(sum);
});

// part 2
fetch("https://adventofcode.com/2022/day/3/input").then(x=>x.text()).then(data=>{
    /*data=`vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw`;*/
    let sum = 0;
    const lines = data.split('\n').filter(x=>x);
    for(let i = 0; i < lines.length; i += 3){
        let dict = {};
        for(let j = 0; j < 3; j ++){
            const line = lines[i+j];
            for(const c of new Set(line.split(''))) dict[c] = (dict[c]||0) + 1;
        }
        // console.log(dict);
        // console.log(Object.entries(dict).sort((a,b) => b[1]-a[1]));
        const c = Object.entries(dict).sort((a,b) => b[1]-a[1])[0][0];
        // console.log(sum);
        sum += c.toLowerCase().charCodeAt(0) - "a".charCodeAt(0) + 1 + (c == c.toUpperCase() ? 26 : 0);
    }
    console.log(sum);
});