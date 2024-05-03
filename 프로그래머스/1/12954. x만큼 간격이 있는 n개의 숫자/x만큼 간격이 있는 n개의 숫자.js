function solution(x, n) {
    var answer = [];
    let b = 1;
    answer.push(x);
    for(let a = 2;a<n+1;a++){
        answer.push(a*x);
    }
    return answer;
}