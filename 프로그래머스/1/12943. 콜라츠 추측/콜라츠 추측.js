function solution(num) {
    var answer = num;
    let a = 0;
    while(true){
        if(answer == 1) break;
        if(a>500){
            return -1;
        }
        if(answer%2==0){
            a++;
            answer/=2;
        }else{
            a++;
            answer*=3;
            answer+=1;
        }
    }
    return a;
}