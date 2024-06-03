function solution(array, commands) {
    var answer = [];
    for(let a = 0;a<commands.length;a++){
        let list1 = array.slice();
        if(commands[a][0] == commands[a][1]){
            list1 = [list1[commands[a][0]-1]];
        }else{
            list1 = (list1.slice(commands[a][0]-1,commands[a][1])).sort((a, b) => a - b);
            
        }
        answer.push(list1[commands[a][2]-1]);
    }
    return answer;
}