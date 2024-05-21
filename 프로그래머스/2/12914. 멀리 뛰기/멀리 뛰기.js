function try3(n){
    if(n == 1) return 1;
    if(n==2) return 2;
    let try4 = 1;
    let try5 = 2;
    let ans = 0;
    for(let a = 2;a<n;a++){
        ans = (try4+try5)%1234567;
        try4 = try5;
        try5 = ans;
    }
    return ans;
}
function solution(n) {
    var answer = 0;
    answer = try3(n);
    return answer;
}
