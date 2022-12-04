fetch("https://adventofcode.com/2022/day/4/input").then(x=>x.text()).then(data=>{
    let sum1 = 0, sum2 = 0;
    const lines = data.split('\n').filter(x=>x);
    for(const line of lines){
        const [a,b,c,d] = line.split(/-|,/).map(x=>+x);
        if((a >= c && b <= d) || (a <= c && b >= d)) sum1 ++;
        if((b >= c && a <= d) || (d >= a && c <= b)) sum2 ++;
    }
    console.log(sum1, sum2);
});