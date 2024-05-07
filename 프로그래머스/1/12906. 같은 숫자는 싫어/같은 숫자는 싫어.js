function solution(arr)
{
    var answer = [];
    let try1 = 0;
    for(let a = 0;a<arr.length;a++){
        if(a== 0){
            try1 = arr[a];
        }else{
            if(arr[a] == try1){
                try1 = arr[a];
                arr[a] = -1;
            }else{
                try1 = arr[a];
            }
        }
    }
    for(let a = 0;a<arr.length;a++){
        if(arr[a] != -1){
            answer.push(arr[a]);
        }
    }
    return answer;
}