function solution(num_list) {
    var answer = [0,0];
    for(let a = 0;a<num_list.length;a++){
        if(num_list[a] %2==0){
            answer[0]++;
        }else{
            answer[1]++;
        }
    }
    return answer;
}