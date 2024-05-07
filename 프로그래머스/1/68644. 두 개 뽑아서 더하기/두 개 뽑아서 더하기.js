function solution(numbers) {
    var answer = [];
    let try1 = 0;
    while(try1 != numbers.length){
        for(let a = try1;a<numbers.length;a++){
            if(answer.indexOf(numbers[a] + numbers[try1]) == -1 && a!=try1){
                answer.push(numbers[a] + numbers[try1]);
            }
        }
        try1++;
    }
    return answer.sort(function(a, b)  {
  return a - b;
});
}