function solution(n) {
    var answer = 0;
    let try1 = [0,1]
    if(n == 0) return 0;
    if(n==1) return 1;
    for(let a = 2;a<=n;a++){
        try1.push((try1[a-2]+try1[a-1])%1234567)
    }
    answer = try1[try1.length-1];
    return answer;
}