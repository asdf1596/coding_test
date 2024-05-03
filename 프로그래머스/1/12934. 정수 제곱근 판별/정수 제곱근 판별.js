function solution(n) {
    var answer = 0;
    let i = parseInt(Math.sqrt(n));
    for(let a = 0;a<=i;a++){
        if(a*a==n){
            return ((a+1)*(a+1))
        }
    }
    return -1;
}