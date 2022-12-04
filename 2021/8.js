fetch("https://adventofcode.com/2021/day/8/input").then(x=>x.text()).then(data=>{
    data2=`be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce`.replace(/\|\n/g, '| ');
    // 1 - 2*
    // 4 - 4*
    // 7 - 3*
    // 8 - 7*
    // 6 - 6 => doesnt match 1, 6|1 =/= 6
    // 3 - 5 => matches 1, 3|1 == 3
    // 5 - 5 => similar 6, 6|5 == 6
    // 9 - 6 => 5|1 == 9
    // 0 - 6 => last 6 -- matches 1, 0|1 == 0
    // 2 - 5 => last 5 --
    let sum1 = 0, sum2 = 0;
    const lines = data.split('\n').filter(x=>x);
    for(const line of lines){
        let [a,b] = line.split(' | ').map(x=>x.split(' '));
        // console.log(a,b);
        let buckets = [...new Array(10)].map(()=>[]);;
        let unique = a.map(x => {
            buckets[x.length].push(x.split('').map(c => 1<<(c.charCodeAt(0)-'a'.charCodeAt(0))).reduce((a,b)=>a+b));
        });
        let known = [];
        known[1] = buckets[2][0];
        known[4] = buckets[4][0];
        known[7] = buckets[3][0];
        known[8] = buckets[7][0];
        known[6] = buckets[6].filter(x => (x|known[1]) != x)[0];
        known[3] = buckets[5].filter(x => (x|known[1]) == x)[0];
        known[5] = buckets[5].filter(x => (x|known[6]) == known[6])[0];
        known[9] = known[5]|known[1];
        known[0] = buckets[6].filter(x => x!=known[6] && x!=known[9])[0];
        known[2] = buckets[5].filter(x => x!=known[3] && x!=known[5])[0];
        // console.log(known);
        let num = 0;
        for(const str of b){
            const digit = str.split('').map(c => 1<<(c.charCodeAt(0)-'a'.charCodeAt(0))).reduce((a,b)=>a+b);
            // console.log(digit);
            sum1 += [1,4,7,8].filter(x => known[x] == digit).length;
            num = 10*num + Math.max(0, known.indexOf(digit));
            // if(known.indexOf(digit)<0)console.log("!!");
        }
        // console.log(num);
        sum2 += num;
    }
    console.log(sum1, sum2);
});