function solution(n, arr1, arr2) {
    var answer = [];
    
    for(let a = 0; a < n; a++) {
        let binary1 = arr1[a].toString(2).padStart(n, '0');
        let binary2 = arr2[a].toString(2).padStart(n, '0');
        let line = "";
        
        for(let b = 0; b < n; b++) {
            line += (parseInt(binary1[b]) | parseInt(binary2[b])) ? "#" : " ";
        }
        
        answer.push(line);
    }
    
    return answer;
}
