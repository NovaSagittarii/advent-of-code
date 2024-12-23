function sec(x) {
    for (let i = 0; i < 2000; ++i) {
        x ^= (x<<6);
        x &= 16777215;
        x ^= (x>>5);
        x &= 16777215;
        x ^= (x<<11);
        x &= 16777215;
    }
    return x;
}
`(INPUT)`.split('\n').map(x => sec(+x)).reduce((a,b)=>a+b)