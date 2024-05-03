function solution(n, wires) {
    let min = wires.length+1;
    let count = 0;
    const visit=new Array(9).fill(false);
    const graph = Array.from({length:n+1}, () => []);
    for(let i = 0;i<wires.length;i++){
        graph[wires[i][0]].push(wires[i][1]);
        graph[wires[i][1]].push(wires[i][0]);
        
    }
    function dfs(start, ban){
        visit[start] = true;
        ++count;
        for(let a of graph[start]){
            if(!visit[a]){
                if(a!==ban){
                    dfs(a,ban);
                }
            }
        }
        return count;
    }
    for(let [first, second] of wires){
        count = 0;
        let one = dfs(first,second);
        count = 0;
        let two = dfs(second, first);
        visit.fill(false);
        min = Math.min(Math.abs(one-two), min);
    }
    return min;
}
