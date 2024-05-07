function solution(price, money, count) {
    var answer = 0;
    for(let a = 1;a<=count;a++){
        answer+=(price*a);
    }
    if(answer < money) return 0;
    return answer-money;
}