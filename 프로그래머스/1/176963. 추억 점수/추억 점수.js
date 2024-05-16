//이거 왜 시간제한 안걸리지
function solution(name, yearning, photo) {
    var answer = [];
    for(let a = 0;a<photo.length;a++){
        answer.push(0);
        for(let b = 0;b<photo[a].length;b++){
            for(let c = 0;c<name.length;c++){
                if(name[c] == photo[a][b]){
                    answer[a]+=yearning[c];
                }
            }
        }
    }
    return answer;
}