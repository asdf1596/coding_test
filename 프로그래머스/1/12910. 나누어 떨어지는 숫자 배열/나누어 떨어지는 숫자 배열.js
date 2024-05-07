function solution(arr, divisor) {
    var answer = [];
    let try1 = arr.length;
    let try2 = 0;
    for(let a = 0;a<try1;a++){
        if(arr[a]%divisor != 0){
            arr[a] = -1;
        }
        if(arr[a]!=-1){
            answer.push(arr[a]);
        }
    }
    if(answer.length == []) return [-1];
    return answer.sort(function (a, b) {
  return a - b;
});
}