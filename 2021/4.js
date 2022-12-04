fetch("https://adventofcode.com/2021/day/4/input").then(x=>x.text()).then(data=>{
    const lines = data.split('\n').filter(x=>x);
    let draws = lines.splice(0, 1)[0].split(',').map(x=>+x);
    let board;
    let earliest = 26;
    let latest = 0;
    let sum = 0;
    let sum2 = 0;
    let wins = [];
    for(let x = 0; x < 5; x ++){
        wins.push([...new Array(5)].map((_,i)=>i+x*5));
        wins.push([...new Array(5)].map((_,i)=>x+i*5));
    }
    // wins.push([...new Array(5)].map((_,i)=>i*6));
    // wins.push([...new Array(5)].map((_,i)=>i*4+4));
    
    while((board = lines.splice(0, 5).join(' ').split(/ +/).filter(x=>x).map(x=>+x)).length){
        // console.log(board);
        for(let i = 0; i < draws.length; i ++){
            let call = draws[i];
            const j = board.indexOf(call);
            // console.log(call, j, board[j]);
            board[j] = -1;
            let win = false;
            for(let pattern of wins){
                if(pattern.filter(i => board[i] < 0).length >= 5){
                    win = true;
                    // console.log("win", pattern);
                    break;
                }
            }
            if(win){
                if(i < earliest){
                    earliest = i;
                    sum = board.filter(x=>x>=0).reduce((a,b)=>a+b);
                    // console.log(board);
                }
                if(i > latest){
                    latest = i;
                    sum2 = board.filter(x=>x>=0).reduce((a,b)=>a+b);
                }
                break;
            }
        }
    }
    console.log(draws[earliest]*sum, draws[latest]*sum2);
    // console.log(sum1, sum2);
});