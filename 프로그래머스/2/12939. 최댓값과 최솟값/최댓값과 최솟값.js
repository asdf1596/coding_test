function solution(s) {
    var answer = '';
    let min = 0;
    let max = 0;
    let nums = s.split(" ");
    for(let a = 0;a<nums.length;a++){
        nums[a] = parseInt(nums[a]);
    }
    min = nums[0];
    max = nums[0];
    for(let a = 0;a<nums.length;a++){
        if(nums[a] > max){
            max = nums[a];
        }
        if(nums[a] < min){
            min = nums[a];
        }
    }
    answer = min + " "+max;
    return answer;
}