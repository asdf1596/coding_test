function solution(board) {
    var answer = 0;
    let check = [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]];
    let len = board.length-1;
    let mine = [];
    for(let y = 0;y<=len;y++){
        for(let x = 0;x<=len;x++){
            if(board[y][x] == 1){
                mine.push([y,x]);
            }
        }
    }
    //console.log(mine);
    for(let a = 0;a<mine.length;a++){
        for(let b = 0;b<check.length;b++){
            // console.log([mine[a][0]+check[b][0],mine[a][1]+check[b][1]]);
            let newy = mine[a][0]+check[b][0];
            let newx = mine[a][1]+check[b][1];
            if(toCheck(board, newy, newx, len)){
                board[mine[a][0]+check[b][0]][mine[a][1]+check[b][1]] = 1;
            }
        }
    }
    for(let y = 0;y<=len;y++){
        for(let x = 0;x<=len;x++){
            if(board[y][x] == 0){
                answer++;
            }
        }
    }
    //console.log(board);
    return answer;
}
function toCheck(b, newy, newx, len){
    if(newx >= 0 && newx <= len && newy >= 0 && newy <= len){
        return true;
    }else{
        return false;
    }
    //console.log(witch);
    return 0;
}