function solution(left, right) {
    var answer = 0;
    for(let a = left;a<=right;a++){
        if(count(a)%2==0){
            answer+=a;
        }else{
            answer-=a;
        }
    }
    return answer;
}
function count(n){
    let i = 0;
    for(let y = 1;y<=n;y++){
        if(n%y==0){
            i++;
        }
    }
    return i;
}