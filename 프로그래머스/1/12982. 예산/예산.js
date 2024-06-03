function solution(d, budget) {
    var answer = 0;
    d.sort((a, b) => a - b);
    for(let a = 0;a<d.length;a++){
        if(budget-d[a]<0){
            return answer;
        }else{
            budget-=d[a];
            answer++;
        }
    }
    return answer;
}