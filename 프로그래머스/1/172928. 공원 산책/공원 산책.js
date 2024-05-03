function solution(park, routes) {
    var answer = [];
    let x = 0;
    let y = 0;
    let err = 0;
    var map = [];
    var task = [];
    var start = [0,0];
    var move = [[0,1],[0,-1],[1,0],[-1,0]];
    for(let a = 0;a<park.length;a++){
        map.push([]);
        for(let b = 0;b<park[a].length;b++){
            if(park[a].substr(b,1) == "S"){
                start[0] = a;
                start[1] = b;
            }
            map[a].push(park[a].substr(b, 1));
        }
    }
    for(let a = 0;a<routes.length;a++){
        task.push(routes[a].split(" "));
        task[a][1] = parseInt(task[a][1])
    }
    for(let a = 0;a<task.length;a++){
        err = 0;
        switch(task[a][0]){
                case "E":
                    y = move[0][0];
                    x = move[0][1];
                    break
                case "W":
                    y = move[1][0];
                    x = move[1][1];
                    break
                case "S":
                    y = move[2][0];
                    x = move[2][1];
                    break
                default:
                    y = move[3][0];
                    x = move[3][1];
                    break
        }
        for(let b = 1;b<=task[a][1];b++){
            if(start[0]+(y*b) < 0 || start[1]+(x*b) < 0 || start[0]+(y*b) >= map.length || start[1]+(x*b) >= map[0].length || map[start[0]+(y*b)][start[1]+(x*b)] == "X"){
                console.log(start[0]+(y*b), start[1]+(x*b), start);
                err = 1;
                break;
            }
        }
        if(!err){
            console.log("문제없음");
            start = [start[0]+(y*task[a][1]), start[1]+(x*task[a][1])]
        }
        console.log(start);
        
    }
    console.log(map);
    console.log(start);
    answer = start;
    return answer;
}