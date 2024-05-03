function solution(number) {
    let num = number;
    var answer = 0;
    for(let a = 0;a<num.length;a++){
        for(let b = a+1;b<num.length;b++){
            for(let c = b+1;c<num.length;c++){
                if(num[a]+num[b]+num[c]==0){
                    answer++;
                }
            }
        }
    }
    return answer;
}